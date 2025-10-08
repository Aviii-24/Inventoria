# Inventoria (Django + MySQL + Jinja Templates)

A full-stack **Django web application** with user authentication, CRUD operations, and dynamic frontend using **Jinja templates**. Users can register, log in, add new products, edit, delete, search, and view products through a responsive interface.

---

## 🛠️ Features

- **User Authentication:** Login and logout functionality for secure access.
- **Product Management:** Create, Read, Update, Delete (CRUD) operations for products.
- **Search Products:** Search products by name or category.
- **Dynamic Frontend:** Built using **Django templates (Jinja2)** and **Bootstrap** for responsive UI.
- **Database Integration:** Fully functional backend using **MySQL** and Django ORM.
- **Media & Static Files:** Support for images and static assets.

---

## ⚙️ Tech Stack

**Backend:** Django, Django ORM, MySQL, Django Authentication  
**Frontend:** Django Templates (Jinja2), HTML, CSS, Bootstrap  
**Environment & Tools:** Python 3.x, Virtual Environment (venv), Git/GitHub

---

## 📂 Project Structure
```bash
DJANGO MODULE/
├── ProductDashboard/
│ ├── pycache/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── media/
│ └── images/
├── product/
│ ├── pycache/
│ ├── migrations/ <-- CLOSED
│ ├── static/ <-- CLOSED
│ ├── templates/ <-- CLOSED
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── manage.py
└── README.md
```



---

## 🚀 Installation & Setup

1️⃣ **Clone the repository**
```bash
git clone https://github.com/your-username/product-management-system.git
cd product-management-system
```
2️⃣ Create a virtual environment and activate it
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Configure MySQL database
```bash
Create a database in MySQL, e.g., product_db

Update settings.py DATABASES section with your MySQL credentials:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
5️⃣ Run migrations
```bash
python manage.py migrate
```
6️⃣ Create superuser
```bash
python manage.py createsuperuser
```
7️⃣ Run the server
```bash
python manage.py runserver
```
Access the application at http://127.0.0.1:8000/

🖥️ Usage

Register/Login: Users can create an account or log in.

Add Product: Use the “Add Product” page to create a new product entry.

Edit/Delete Product: Update or remove products directly from the dashboard.

Search Products: Search for products by name or category.

View Products: Display all products in a tabular or card layout.

👨‍💻 Author

Avinash Satalkar
https://www.linkedin.com/in/avinash-satalkar-10a934230/
