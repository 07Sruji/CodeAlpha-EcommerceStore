# CodeAlpha Task 1 - ShopEase

A polished Django e-commerce store for the CodeAlpha internship task.

## Features
- Product listing with real product images
- Search and category filters
- Product details
- Shopping cart with quantity updates/removal
- Registration, login and logout
- Checkout and order processing
- My Orders
- SQLite database
- Django admin for products and orders
- Responsive HTML/CSS/JavaScript UI

## Windows PowerShell setup

```powershell
cd CodeAlpha_EcommerceStore
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_products
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

The demo product images are loaded from Unsplash image URLs. Internet access is needed for those remote images. You can later replace `image_url` values in the admin with your own local images if required.
