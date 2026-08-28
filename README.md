# 📚 BookVerse — Bookstore Management System

**Task ID:** PY-EC-003 | **Domain:** E-Commerce Bookstore | **Framework:** Django + MySQL (SQLite by default)
**Internship:** Virtual Python Full Stack Internship — 7-Day Self-Paced Task

A complete, production-style bookstore management system built with Django,
featuring book catalog & search, inventory management, shopping cart,
checkout with simulated payments, order tracking, reviews & ratings, and a
wishlist — all styled with Bootstrap 5.

---

## ✅ Features Implemented

| Feature | Details |
|---|---|
| **Book Catalog** | Categories, authors, genres, full-text search, sorting, pagination |
| **Inventory Management** | Live stock tracking, low-stock alerts, staff dashboard, manual restock |
| **Shopping Cart** | Add/remove/update quantities, live totals, stock-aware quantity caps |
| **Checkout** | Address form (with saved-address autofill), COD/Card/UPI/Net Banking (simulated) |
| **User Authentication** | Register, login, logout, profile editing, avatar upload, multiple saved addresses |
| **Order Management** | Order history, live status timeline, cancel-with-restock |
| **Reviews & Ratings** | 1–5 star reviews, verified-purchase badge, auto-recalculated book rating |
| **Wishlist** | One-click add/remove, dedicated wishlist page |

---

## 🚀 Quick Start (One-Click Setup)

**No MySQL installation required** — the project runs on SQLite out of the box.

### macOS / Linux
```bash
chmod +x setup.sh
./setup.sh
```

### Windows
```bat
setup.bat
```

This will automatically:
1. Create a Python virtual environment
2. Install all dependencies
3. Run database migrations
4. Seed demo data (categories, authors, 28 books with generated cover art, users, a sample order)
5. Launch the development server at **http://127.0.0.1:8000/**

### Subsequent runs
Once setup has run once, just use:
```bash
./run.sh      # macOS/Linux
run.bat       # Windows
```

---

## 🔑 Demo Login Credentials

| Role | Username | Password | Notes |
|---|---|---|---|
| Admin / Staff | `admin` | `admin123` | Full Django admin + Inventory dashboard access |
| Customer | `customer` | `customer123` | Has a sample delivered order and 3 reviews already |

Admin panel: **http://127.0.0.1:8000/admin/**
Staff inventory dashboard: **http://127.0.0.1:8000/staff/inventory/**

---

## 🗄️ Switching to MySQL

By default the app uses SQLite (`db.sqlite3`) so it runs anywhere with zero
setup. To switch to MySQL (as specified in the task's tech stack), see the
step-by-step guide in **[switch_to_mysql.md](switch_to_mysql.md)** — it's a
one-environment-variable change (`USE_MYSQL=True`) plus installing
`mysqlclient`.

---

## 🛠️ Manual Setup (if you prefer not to use the scripts)

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

To reset and reseed demo data at any time:
```bash
python manage.py seed_data --flush
```

---

## 🧰 Technology Stack

**Backend:** Django 4.x, Python 3.8+
**Database:** SQLite (default) / MySQL 8.x (optional, via `USE_MYSQL=True`)
**Frontend:** HTML5, Bootstrap 5, Bootstrap Icons, vanilla JavaScript
**Images:** Book covers and author/avatar placeholders are generated locally
with **Pillow** at seed time — no external API keys or internet downloads required.

---

## 📁 Project Structure

```
BookVerse/
├── bookverse/          # Project settings, root URLs
├── accounts/           # Profile, addresses, register/login/logout
├── catalog/            # Books, categories, genres, authors, reviews, inventory dashboard
├── cart/               # Shopping cart
├── orders/             # Checkout, orders, payment simulation, status history
├── wishlist/           # Wishlist
├── templates/          # All HTML templates (Bootstrap 5)
├── static/             # CSS, JS, placeholder image
├── media/              # Uploaded/generated book covers, author photos, avatars
├── requirements.txt    # SQLite-mode dependencies
├── requirements-mysql.txt
├── switch_to_mysql.md
├── setup.sh / setup.bat
└── run.sh / run.bat
```

---

## 📝 Notes for Evaluation

- All models (`Book`, `Category`, `Genre`, `Author`, `Review`, `Cart`,
  `CartItem`, `Order`, `OrderItem`, `OrderStatusHistory`, `Address`,
  `Profile`, `WishlistItem`) are implemented with the Django ORM and
  registered in the Django admin for easy inspection/grading.
- Stock is automatically decremented on order placement and restored on
  order cancellation.
- Reviews are restricted to customers who have actually purchased the book
  (`verified_purchase=True`), matching real-world e-commerce behavior.
- Payment methods (Card/UPI/Net Banking) are **simulated** for demo
  purposes — no real payment gateway is integrated, and this is clearly
  labeled in the checkout UI.
- The whole flow (browse → search/filter → cart → checkout → order → review
  → wishlist) has been smoke-tested end-to-end via Django's test client.
