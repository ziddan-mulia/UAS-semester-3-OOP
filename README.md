# 🛒 AZIDMart - E-commerce Platform

**Sistem manajemen toko online modern berbasis Flask dengan integrasi API eksternal.**

![Flask](https://img.shields.io/badge/Flask-3.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Deskripsi Project

AZIDMart adalah platform e-commerce lengkap yang dibangun menggunakan **Python Flask** sebagai backend dan **Bootstrap 5** sebagai frontend. Sistem ini mengintegrasikan **DummyJSON API** sebagai sumber data produk, menyediakan pengalaman belanja online yang real-time dan responsif.

**Tujuan Project:**

- Implementasi Flask framework dengan REST API integration
- Membangun sistem e-commerce functional dengan fitur lengkap
- Menerapkan responsive design dan modern UI/UX
- Demonstrasi kemampuan fullstack development

## ✨ Fitur Utama

### ✅ Core Features

- **Dashboard Real-time** - Statistik produk & kategori
- **Katalog Produk** - 100+ produk dengan filter & search
- **Detail Produk** - Informasi lengkap dengan gallery
- **Multi-Kategori** - 6 kategori terorganisir
- **Responsive Design** - Optimal di semua device

### 🎨 UI/UX Features

- Modern gradient design dengan animasi CSS3
- Bootstrap 5 components dengan custom styling
- Interactive product cards dengan hover effects
- Intuitive navigation & user flow

### 🔧 Technical Features

- REST API integration dengan DummyJSON
- Dynamic routing & parameter handling
- Error handling & fallback system
- Template inheritance untuk code reuse

## 🛠️ Teknologi yang Digunakan

### **Backend:**

- **Python 3.8+** - Bahasa pemrograman utama
- **Flask 3.0.0** - Web framework minimalis
- **Requests 2.31.0** - HTTP client untuk API calls

### **Frontend:**

- **HTML5** - Struktur halaman web
- **CSS3** - Styling dengan animations & gradients
- **Bootstrap 5.3.0** - Responsive framework
- **JavaScript** - Interaktivitas dasar
- **Bootstrap Icons** - Icon library gratis

### **API & Data:**

- **DummyJSON API** - Sumber data produk real-time
- **REST Architecture** - API communication pattern

## 📁 Struktur Project

flask_azidmart_api/
├── templates/
│ ├── 404.html
│ ├── 500.html
│ ├── about.html
│ ├── base.html
│ ├── categories.html
│ ├── detail.html
│ ├── index.html
│ ├── products.html
│ └── users.html
├── app.py
├── README.md
├── requirements.txt
└── venv/ (virtual environment)
├── bin/ (atau Scripts/ di Windows)
├── lib/
├── include/
└── pyvenv.cfg

## 🚀 Cara Instalasi & Menjalankan

### **Prasyarat:**

- Python 3.8 atau lebih baru
- pip (Python package manager)
- Git (untuk cloning repository)

### **Step-by-Step:**

1. **Clone repository:**

```bash
git clone https://github.com/username/flask_azidmart_api.git
cd flask_azidmart_api
Buat virtual environment (recommended):

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Jalankan aplikasi:

bash
python app.py
Buka browser:

text
http://localhost:5000
📡 API Endpoints yang Digunakan
AZIDMart menggunakan DummyJSON API dengan endpoint berikut:
Endpoint	Method	Deskripsi
/products	GET	Semua produk (100 items)
/products/{id}	GET	Detail produk by ID
/products/categories	GET	Daftar semua kategori
/products/category/{name}	GET	Produk berdasarkan kategori
/products/search?q={query}	GET	Pencarian produk

🎯 Fitur Implementasi Teknis
1. Flask Routing System
python
@app.route('/products')
def products():
    # Filter produk berdasarkan kategori & search
    category = request.args.get('category', 'all')
    search = request.args.get('search', '')
    # ... filter logic
2. Dynamic Filtering
Filter by kategori (electronics, fashion, home, dll)
Real-time search dengan keyword matching
URL parameter handling untuk bookmarkable filters

3. Currency Conversion
python
# Konversi USD → IDR (1 USD = Rp 15.000)
product['price_idr'] = product['price'] * 15000

4. Template Inheritance
html
<!-- base.html -->
{% block content %}{% endblock %}
<!-- products.html -->
{% extends "base.html" %}
{% block content %}...{% endblock %}

5. Error Handling
Graceful degradation jika API down
Custom error pages (404, 500)
Image fallback system

📊 Halaman yang Tersedia
/ - Dashboard dengan statistik
/products - Katalog produk dengan filter
/products?category=electronics - Filter by kategori
/products?search=laptop - Search produk
/product/{id} - Detail produk lengkap
/categories - Overview semua kategori
/about - Tentang project & tim

🎨 Design System
Color Palette:
Primary: #1E3C72 (Dark Blue)
Secondary: #2A5298 (Blue)
Accent: #FFD700 (Gold)
Background: #F8FAFC (Light Gray)
Text: #1F2937 (Dark Gray)
Typography:
Headings: Segoe UI / Montserrat
Body: Segoe UI / Open Sans
Monospace: Consolas (code snippets)

Animations:
CSS3 transitions & transforms
Hover effects pada product cards
Gradient backgrounds dengan smooth transitions

📝 Untuk Developer
Menambahkan Fitur Baru:
Tambah route baru di app.py
Buat template HTML di templates/
Update navigation di base.html jika perlu
Test dengan python app.py
Modifikasi Styling:
Global styles di base.html block extra_css
Page-specific styles di masing-masing template
Gunakan Bootstrap utility classes untuk rapid styling

Debugging:
# Enable debug mode
app.run(debug=True)

# Check logs di terminal
# Flask akan show error details
🤝 Kontribusi
Project ini dibuat untuk tujuan akademik (UAS Web OOP). Untuk kontribusi:
Fork repository
Create feature branch (git checkout -b feature/AmazingFeature)
Commit changes (git commit -m 'Add some AmazingFeature')
Push to branch (git push origin feature/AmazingFeature)
Open Pull Request

👥 Tim Pengembang
Nama	NIM	Role
Asep Suhaedi	312410230	Fullstack Developer
Ziddan Mulia Perdana	312410275	Fullstack Developer
Mata Kuliah: Pemrograman Orinetasi Objek
Tahun: 2026
Semester: Ganjil

📄 License
Project ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail.

text
MIT License

Copyright (c) 2025 AZIDMart Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
🙏 Acknowledgements
DummyJSON - Untuk API produk gratis yang realistis
Flask Documentation - Dokumentasi framework yang excellent
Bootstrap Team - Untuk amazing CSS framework
Bootstrap Icons - Untuk icon library yang gratis

❓ FAQ
Q: Apakah butuh database?
A: Tidak, data diambil real-time dari DummyJSON API.

Q: Bisakah di-deploy ke production?
A: Ya, dengan beberapa adjustment (database, authentication, dll).

Q: Bagaimana cara ganti API source?
A: Ubah API_BASE variable di app.py.

Q: Apakah responsive di mobile?
A: Ya, menggunakan Bootstrap 5 grid system.

Q: Bisa ditambah payment gateway?
A: Ya, architecture siap untuk integrasi lebih lanjut.

⭐ Jika project ini membantu, beri star di GitHub!

Happy Coding! 🚀
# AZIDMart - E-commerce Flask

## 🎯 Overview
- Flask + Bootstrap + DummyJSON API
- 100+ produk real-time
- Filter & search system
- Responsive design

## 🚀 Quick Start
git clone [repo]
cd flask_azidmart_api
pip install -r requirements.txt
python app.py
📞 Contact
Email: team@azidmart.dev
GitHub: https://github.com/Zeppinhere30
        https://github.com/ziddan-mulia

```
