from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import random

app = Flask(__name__)

# API Base URL
API_BASE_URL = "https://dummyjson.com"

# Data kategori untuk AZIDMart (toko serba ada)
AZIDMART_CATEGORIES = {
    'electronics': 'Elektronik',
    'fashion': 'Fashion',
    'home': 'Perlengkapan Rumah',
    'beauty': 'Kecantikan',
    'groceries': 'Bahan Makanan',
    'sports': 'Olahraga'
}

# GANTI bagian ini di app.py (sekitar baris 25-65):

# Data kategori untuk AZIDMart (toko serba ada)
AZIDMART_CATEGORIES = {
    'electronics': 'Elektronik',
    'fashion': 'Fashion',
    'home': 'Perlengkapan Rumah',
    'beauty': 'Kecantikan',
    'groceries': 'Bahan Makanan',
    'sports': 'Olahraga'
}

# Mapping kategori DummyJSON ke kategori AZIDMart
CATEGORY_MAPPING = {
    # Electronics
    'smartphones': 'electronics',
    'laptops': 'electronics',
    'tablets': 'electronics',
    'mobile-accessories': 'electronics',
    'televisions': 'electronics',
    
    # Fashion (dari berbagai kategori DummyJSON)
    'tops': 'fashion',
    'womens-dresses': 'fashion',
    'womens-shoes': 'fashion',
    'mens-shirts': 'fashion',
    'mens-shoes': 'fashion',
    'mens-watches': 'fashion',
    'womens-watches': 'fashion',
    'womens-bags': 'fashion',
    'womens-jewellery': 'fashion',
    'sunglasses': 'fashion',
    'jewellery': 'fashion',
    
    # Home
    'furniture': 'home',
    'home-decoration': 'home',
    'lighting': 'home',
    'kitchen-accessories': 'home',
    
    # Beauty
    'fragrances': 'beauty',
    'skincare': 'beauty',
    'beauty': 'beauty',
    
    # Groceries
    'groceries': 'groceries',
    
    # Sports (dari automotive & motorcycle)
    'automotive': 'sports',
    'motorcycle': 'sports',
    'vehicle': 'sports',
    'sports': 'sports',
    
    # Default fallback
    'others': 'electronics'
}

# Icon untuk setiap kategori
CATEGORY_ICONS = {
    'electronics': 'bi-cpu',
    'fashion': 'bi-tshirt',
    'home': 'bi-house-door',
    'beauty': 'bi-flower2',
    'groceries': 'bi-basket2',
    'sports': 'bi-bicycle'
}

# GANTI function ini di app.py:

def transform_to_azidmart_product(product):
    """Transform product data menjadi produk AZIDMart"""
    # Harga dalam Rupiah (konversi dari USD)
    usd_price = product.get('price', 10)
    idr_price = usd_price * 15000  # 1 USD = 15,000 IDR
    
    # Map kategori
    original_category = product.get('category', 'others')
    azidmart_category = CATEGORY_MAPPING.get(original_category, 'electronics')
    
    # Brand lokal AZIDMart
    local_brands = ['AZID Premium', 'AZID Basic', 'AZID Pro', 'AZID Lifestyle']
    
    # Icon berdasarkan kategori
    icon = CATEGORY_ICONS.get(azidmart_category, 'bi-box')
    
    return {
        'id': product.get('id'),
        'title': product.get('title', 'Produk AZIDMart'),
        'description': product.get('description', 'Produk berkualitas dari AZIDMart.'),
        'price_idr': round(idr_price, 2),
        'price_usd': usd_price,
        'discountPercentage': product.get('discountPercentage', 0),
        'rating': product.get('rating', 4.0),
        'stock': product.get('stock', 50),
        'category': AZIDMART_CATEGORIES.get(azidmart_category, 'Elektronik'),
        'original_category': azidmart_category,
        'category_icon': icon,
        'thumbnail': product.get('thumbnail', 'https://via.placeholder.com/300x200?text=AZIDMart'),
        'images': product.get('images', []),
        'brand': random.choice(local_brands),
        'warranty': 'Garansi 1 Tahun',
        'origin': 'Indonesia'
    }

def fetch_api(endpoint):
    """Fetch data dari DummyJSON API"""
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching API: {e}")
        return None


@app.template_filter('format_currency')
def format_currency(value):
    """Format angka menjadi format mata uang Indonesia"""
    try:
        return "{:,.0f}".format(float(value)).replace(",", ".")
    except:
        return str(value)

@app.route('/')
def index():
    """Dashboard AZIDMart"""
    products_data = fetch_api('/products?limit=50')
    
    if products_data:
        azidmart_products = [transform_to_azidmart_product(p) for p in products_data.get('products', [])]
        
        stats = {
            'total_products': len(azidmart_products),
            'total_categories': len(AZIDMART_CATEGORIES),
            'total_stock': sum([p['stock'] for p in azidmart_products]),
            'total_value': sum([p['price_idr'] * p['stock'] for p in azidmart_products])
        }
    else:
        # Data dummy untuk demo
        stats = {
            'total_products': 156,
            'total_categories': 6,
            'total_stock': 2450,
            'total_value': 1250000000
        }
    
    return render_template('index.html', stats=stats, current_year=datetime.now().year)

@app.route('/products')
def products():
    """Halaman daftar produk AZIDMart"""
    category = request.args.get('category', 'all')
    search = request.args.get('search', '')
    
    products_data = fetch_api('/products?limit=100')
    
    azidmart_products = []
    if products_data:
        azidmart_products = [transform_to_azidmart_product(p) for p in products_data.get('products', [])]
    
    if category != 'all':
        azidmart_products = [p for p in azidmart_products if p['original_category'] == category]
    
    if search:
        azidmart_products = [p for p in azidmart_products if search.lower() in p['title'].lower()]
    
    return render_template('products.html', 
                         products=azidmart_products, 
                         categories=AZIDMART_CATEGORIES,
                         current_category=category,
                         search_query=search)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """Detail produk AZIDMart"""
    product_data = fetch_api(f'/products/{product_id}')
    
    if not product_data:
        # Produk dummy jika API error
        dummy_product = {
            'id': product_id,
            'title': f'Produk AZIDMart #{product_id}',
            'description': 'Produk berkualitas tinggi dari AZIDMart dengan garansi resmi.',
            'price': 99.99,
            'discountPercentage': 10,
            'rating': 4.5,
            'stock': 50,
            'category': 'electronics',
            'thumbnail': 'https://via.placeholder.com/500x300?text=AZIDMart+Product',
            'images': [],
            'brand': 'AZID Premium'
        }
        azidmart_product = transform_to_azidmart_product(dummy_product)
        related_products = []
    else:
        azidmart_product = transform_to_azidmart_product(product_data)
        
        # Related products
        related = fetch_api(f'/products/category/{product_data["category"]}?limit=4')
        related_products = []
        if related:
            related_products = [transform_to_azidmart_product(p) for p in related.get('products', [])]
        related_products = [p for p in related_products if p['id'] != product_id][:3]
    
    return render_template('detail.html', product=azidmart_product, related=related_products)

# GANTI route categories di app.py:

@app.route('/categories')
def categories():
    """Kategori produk AZIDMart"""
    products_data = fetch_api('/products?limit=100')
    
    category_stats = []
    
    for cat_key, cat_name in AZIDMART_CATEGORIES.items():
        if products_data:
            # Hitung produk per kategori asli
            azidmart_products = [transform_to_azidmart_product(p) for p in products_data.get('products', [])]
            count = len([p for p in azidmart_products if p['original_category'] == cat_key])
        else:
            # Random count jika API error
            count = random.randint(15, 40)
        
        # Icon berdasarkan kategori
        icon = CATEGORY_ICONS.get(cat_key, 'bi-box')
        
        category_stats.append({
            'name': cat_name,
            'key': cat_key,
            'total': count,
            'icon': icon
        })
    
    return render_template('categories.html', categories=category_stats)
@app.route('/about')
def about():
    """Tentang AZIDMart"""
    return render_template('about.html')

@app.route('/users')
def users():
    """Pelanggan AZIDMart"""
    users_data = fetch_api('/users?limit=15')
    
    azidmart_users = []
    if users_data:
        for user in users_data.get('users', []):
            membership_tiers = ['Gold Member', 'Silver Member', 'Bronze Member', 'Regular']
            azidmart_users.append({
                'id': user.get('id'),
                'name': f"{user.get('firstName', '')} {user.get('lastName', '')}",
                'email': user.get('email'),
                'phone': user.get('phone'),
                'membership': random.choice(membership_tiers),
                'total_purchases': random.randint(5, 50),
                'total_spent': random.randint(500000, 5000000)
            })
    else:
        # Dummy data
        azidmart_users = [
            {'id': 1, 'name': 'Budi Santoso', 'email': 'budi@email.com', 'membership': 'Gold Member', 'total_purchases': 45},
            {'id': 2, 'name': 'Sari Dewi', 'email': 'sari@email.com', 'membership': 'Silver Member', 'total_purchases': 28},
            {'id': 3, 'name': 'Ahmad Fauzi', 'email': 'ahmad@email.com', 'membership': 'Bronze Member', 'total_purchases': 15},
        ]
    
    return render_template('users.html', users=azidmart_users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)