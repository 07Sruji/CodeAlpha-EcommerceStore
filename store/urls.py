from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "product/<int:pk>/",
        views.product_detail,
        name="product_detail"
    ),

    path(
        "cart/",
        views.cart,
        name="cart"
    ),

    path(
        "cart/add/<int:pk>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    path(
        "cart/update/<int:pk>/",
        views.update_cart,
        name="update_cart"
    ),

    path(
        "cart/remove/<int:pk>/",
        views.remove_from_cart,
        name="remove_from_cart"
    ),

    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),

    path(
        "order-success/<int:order_id>/",
        views.order_success,
        name="order_success"
    ),

    path(
        "orders/",
        views.my_orders,
        name="my_orders"
    ),

    # Cancel Order
    path(
        "orders/<int:order_id>/cancel/",
        views.cancel_order,
        name="cancel_order"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),
]