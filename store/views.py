from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, Order, OrderItem


def home(request):

    products = Product.objects.all().order_by("-created_at")

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category__iexact=category)

    categories = Product.objects.values_list(
        "category",
        flat=True
    ).distinct()

    return render(
        request,
        "store/home.html",
        {
            "products": products,
            "categories": categories,
            "query": query
        }
    )


def product_detail(request, pk):

    product = get_object_or_404(Product, pk=pk)

    return render(
        request,
        "store/product_detail.html",
        {
            "product": product
        }
    )


def _cart_data(request):

    raw = request.session.get("cart", {})

    cart = {}

    total = Decimal("0")

    for pid, qty in raw.items():

        try:

            product = Product.objects.get(pk=int(pid))

            qty = max(
                1,
                min(
                    int(qty),
                    product.stock
                )
            )

            cart[product] = qty

            total += product.price * qty

        except (
            Product.DoesNotExist,
            ValueError,
            TypeError
        ):

            continue

    return cart, total


def cart(request):

    cart_items, total = _cart_data(request)

    return render(
        request,
        "store/cart.html",
        {
            "cart_items": cart_items.items(),
            "total": total
        }
    )


def add_to_cart(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    if product.stock < 1:

        messages.error(
            request,
            "This product is out of stock."
        )

        return redirect(
            "product_detail",
            pk=pk
        )

    cart = request.session.get(
        "cart",
        {}
    )

    key = str(pk)

    cart[key] = min(
        int(cart.get(key, 0)) + 1,
        product.stock
    )

    request.session["cart"] = cart

    messages.success(
        request,
        f"{product.name} added to your cart."
    )

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "home"
        )
    )


def update_cart(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    cart = request.session.get(
        "cart",
        {}
    )

    qty = int(
        request.POST.get(
            "quantity",
            1
        )
    )

    if qty <= 0:

        cart.pop(
            str(pk),
            None
        )

    else:

        cart[str(pk)] = min(
            qty,
            product.stock
        )

    request.session["cart"] = cart

    return redirect("cart")


def remove_from_cart(request, pk):

    cart = request.session.get(
        "cart",
        {}
    )

    cart.pop(
        str(pk),
        None
    )

    request.session["cart"] = cart

    return redirect("cart")


@login_required
def checkout(request):

    cart_items, total = _cart_data(request)

    if not cart_items:

        messages.info(
            request,
            "Your cart is empty."
        )

        return redirect("home")

    if request.method == "POST":

        full_name = request.POST.get(
            "full_name",
            ""
        ).strip()

        address = request.POST.get(
            "address",
            ""
        ).strip()

        phone = request.POST.get(
            "phone",
            ""
        ).strip()

        if not all(
            [
                full_name,
                address,
                phone
            ]
        ):

            messages.error(
                request,
                "Please fill in all delivery details."
            )

        else:

            with transaction.atomic():

                for product, qty in cart_items.items():

                    product.refresh_from_db()

                    if product.stock < qty:

                        messages.error(
                            request,
                            f"Not enough stock for {product.name}."
                        )

                        return redirect("cart")

                order = Order.objects.create(

                    user=request.user,

                    full_name=full_name,

                    address=address,

                    phone=phone,

                    total=total
                )

                for product, qty in cart_items.items():

                    OrderItem.objects.create(

                        order=order,

                        product=product,

                        quantity=qty,

                        price=product.price
                    )

                    product.stock -= qty

                    product.save(
                        update_fields=["stock"]
                    )

                request.session["cart"] = {}

            return redirect(
                "order_success",
                order_id=order.id
            )

    return render(
        request,
        "store/checkout.html",
        {
            "cart_items": cart_items.items(),
            "total": total
        }
    )


@login_required
def order_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "store/order_success.html",
        {
            "order": order
        }
    )


@login_required
def my_orders(request):
    orders = request.user.orders.exclude(
        status="Cancelled"
    ).prefetch_related(
        "items__product"
    ).order_by("-created_at")

    return render(
        request,
        "store/orders.html",
        {"orders": orders}
    )


@login_required
def cancel_order(request, order_id):

    if request.method == "POST":

        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
        )

        if order.status != "Cancelled":

            order.status = "Cancelled"

            order.save()

            messages.success(
                request,
                f"Order #{order.id} has been cancelled."
            )

    return redirect("my_orders")


def register(request):

    if request.user.is_authenticated:

        return redirect("home")

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        confirm = request.POST.get(
            "confirm_password",
            ""
        )

        if not username or not email or not password:

            messages.error(
                request,
                "Please fill in all fields."
            )

        elif password != confirm:

            messages.error(
                request,
                "Passwords do not match."
            )

        elif User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

        else:

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            login(
                request,
                user
            )

            return redirect("home")

    return render(
        request,
        "store/register.html"
    )


def login_view(request):

    if request.user.is_authenticated:

        return redirect("home")

    if request.method == "POST":

        user = authenticate(
            request,
            username=request.POST.get(
                "username",
                ""
            ),
            password=request.POST.get(
                "password",
                ""
            )
        )

        if user:

            login(
                request,
                user
            )

            return redirect("home")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "store/login.html"
    )


def logout_view(request):

    logout(request)

    return redirect("home")