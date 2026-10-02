from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = "Add and update demo products in the store"

    def handle(self, *args, **kwargs):

        products = [

            # =========================
            # AUDIO
            # =========================

            {
                "name": "AirFlex Wireless Headphones",
                "description": "Comfortable wireless headphones with clear sound and long battery life.",
                "price": 2499,
                "category": "Audio",
                "stock": 25,
                "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "BassPro Bluetooth Speaker",
                "description": "Portable Bluetooth speaker with powerful bass and compact design.",
                "price": 1899,
                "category": "Audio",
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "SoundBeat Earbuds",
                "description": "Compact wireless earbuds designed for everyday listening.",
                "price": 1599,
                "category": "Audio",
                "stock": 35,
                "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Studio Pro Headphones",
                "description": "Over-ear headphones with immersive audio and comfortable ear cushions.",
                "price": 3299,
                "category": "Audio",
                "stock": 18,
                "image_url": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "MiniPod Wireless Speaker",
                "description": "Small portable speaker perfect for travel and casual listening.",
                "price": 1299,
                "category": "Audio",
                "stock": 40,
                "image_url": "https://images.unsplash.com/photo-1608156639585-b3a032ef9689?auto=format&fit=crop&w=600&q=80"
            },

            # =========================
            # SMART DEVICES
            # =========================

            {
                "name": "Pulse Smart Watch",
                "description": "Modern smartwatch with activity tracking and notification support.",
                "price": 3999,
                "category": "Smart Devices",
                "stock": 20,
                "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "FitTrack Smart Band",
                "description": "Lightweight fitness band for everyday activity and workout tracking.",
                "price": 1799,
                "category": "Smart Devices",
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1557935728-e6d1eaabe558?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "TimeX Smart Watch",
                "description": "Stylish smartwatch with a bright display and fitness features.",
                "price": 4499,
                "category": "Smart Devices",
                "stock": 15,
                "image_url": "https://images.unsplash.com/photo-1544117519-31a4b719223d?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Smart Home Hub",
                "description": "Compact smart hub for managing compatible home devices.",
                "price": 2999,
                "category": "Smart Devices",
                "stock": 12,
                "image_url": "https://images.unsplash.com/photo-1558008258-3256797b43f3?auto=format&fit=crop&w=600&q=80"
            },

            # =========================
            # SHOES
            # =========================

            {
                "name": "Urban Classic Sneakers",
                "description": "Comfortable everyday sneakers with a clean urban design.",
                "price": 2799,
                "category": "Shoes",
                "stock": 25,
                "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Street Runner Shoes",
                "description": "Lightweight running shoes designed for everyday comfort.",
                "price": 3199,
                "category": "Shoes",
                "stock": 22,
                "image_url": "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Classic White Sneakers",
                "description": "Minimal white sneakers that match casual everyday outfits.",
                "price": 2499,
                "category": "Shoes",
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Trail Outdoor Shoes",
                "description": "Durable outdoor shoes designed for walking and light adventures.",
                "price": 3599,
                "category": "Shoes",
                "stock": 18,
                "image_url": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?auto=format&fit=crop&w=600&q=80"
            },

            # =========================
            # BAGS
            # =========================

            {
                "name": "Metro Laptop Backpack",
                "description": "Spacious backpack with a dedicated laptop compartment.",
                "price": 1999,
                "category": "Bags",
                "stock": 25,
                "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Travel Explorer Backpack",
                "description": "Durable travel backpack with multiple storage compartments.",
                "price": 2499,
                "category": "Bags",
                "stock": 20,
                "image_url": "https://images.unsplash.com/photo-1622560480605-d83c853bc5c3?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Classic Leather Backpack",
                "description": "Elegant backpack with a classic leather-inspired finish.",
                "price": 3299,
                "category": "Bags",
                "stock": 15,
                "image_url": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Everyday Shoulder Bag",
                "description": "Simple and practical shoulder bag for daily use.",
                "price": 1499,
                "category": "Bags",
                "stock": 28,
                "image_url": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=600&q=80"
            },

            # =========================
            # CLOTHING
            # =========================

            {
                "name": "Classic Cotton T-Shirt",
                "description": "Soft cotton T-shirt with a comfortable regular fit.",
                "price": 699,
                "category": "Clothing",
                "stock": 50,
                "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Premium Casual Shirt",
                "description": "Smart casual shirt suitable for everyday and semi-formal occasions.",
                "price": 1299,
                "category": "Clothing",
                "stock": 35,
                "image_url": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Comfort Hoodie",
                "description": "Warm and comfortable hoodie for casual everyday wear.",
                "price": 1599,
                "category": "Clothing",
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Classic Denim Jacket",
                "description": "Timeless denim jacket with a versatile casual look.",
                "price": 2199,
                "category": "Clothing",
                "stock": 20,
                "image_url": "https://images.unsplash.com/photo-1543076447-215ad9ba6923?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Relaxed Fit Jeans",
                "description": "Comfortable denim jeans with a relaxed everyday fit.",
                "price": 1799,
                "category": "Clothing",
                "stock": 35,
                "image_url": "https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=600&q=80"
            },

            # =========================
            # ACCESSORIES
            # =========================

            {
                "name": "Classic Leather Wallet",
                "description": "Slim wallet with multiple compartments for cards and cash.",
                "price": 899,
                "category": "Accessories",
                "stock": 40,
                "image_url": "https://images.unsplash.com/photo-1627123424574-724758594e93?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Minimalist Sunglasses",
                "description": "Stylish sunglasses with a simple modern frame.",
                "price": 999,
                "category": "Accessories",
                "stock": 35,
                "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Everyday Wrist Watch",
                "description": "Classic analog wrist watch with a clean minimalist dial.",
                "price": 1899,
                "category": "Accessories",
                "stock": 20,
                "image_url": "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Urban Baseball Cap",
                "description": "Comfortable casual cap suitable for everyday outdoor use.",
                "price": 599,
                "category": "Accessories",
                "stock": 45,
                "image_url": "https://images.unsplash.com/photo-1521369909029-2afed882baee?auto=format&fit=crop&w=600&q=80"
            },

            # =========================
            # HOME & LIFESTYLE
            # =========================

            {
                "name": "Ceramic Coffee Mug",
                "description": "Simple ceramic mug for coffee, tea and everyday drinks.",
                "price": 399,
                "category": "Home & Lifestyle",
                "stock": 50,
                "image_url": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Modern Table Lamp",
                "description": "Minimal table lamp designed for a warm and modern workspace.",
                "price": 1299,
                "category": "Home & Lifestyle",
                "stock": 25,
                "image_url": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Reusable Water Bottle",
                "description": "Durable reusable bottle suitable for school, office and travel.",
                "price": 699,
                "category": "Home & Lifestyle",
                "stock": 45,
                "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Soft Comfort Cushion",
                "description": "Soft decorative cushion designed to add comfort to your room.",
                "price": 599,
                "category": "Home & Lifestyle",
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=600&q=80"
            },

            # =========================
            # ELECTRONICS
            # =========================

            {
                "name": "Slim Wireless Keyboard",
                "description": "Compact wireless keyboard with a clean modern design.",
                "price": 1499,
                "category": "Electronics",
                "stock": 25,
                "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Precision Wireless Mouse",
                "description": "Ergonomic wireless mouse designed for smooth everyday use.",
                "price": 899,
                "category": "Electronics",
                "stock": 35,
                "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "HD Webcam",
                "description": "Compact HD webcam for online classes, meetings and video calls.",
                "price": 1999,
                "category": "Electronics",
                "stock": 20,
                "image_url": "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Portable Power Bank",
                "description": "Compact power bank for charging smartphones while travelling.",
                "price": 1299,
                "category": "Electronics",
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1609592424629-7f6f9f9d1a91?auto=format&fit=crop&w=600&q=80"
            },
        ]

        created_count = 0
        updated_count = 0

        for item in products:
            product, created = Product.objects.update_or_create(
                name=item["name"],
                defaults=item
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{created_count} new products added."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{updated_count} existing products updated."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Total products in store: {Product.objects.count()}"
            )
        )
