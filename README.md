# 🌶️ DevjaniMasala – A Django-Based Masala Business Portfolio

DevjaniMasala is a clean and simple **Python Django** web application designed to manage a masala/spice business portfolio. Built with Django’s powerful admin and authentication system, this project allows admins to securely manage spice products, update listings, and provide a smooth user experience for viewing product details. While currently a portfolio management system, it’s designed with future scalability in mind.

---

## 🛠️ Installation & Setup Guide

### 1. Clone the Repository

`git clone https://github.com/SaharFatimaDevjani/Devjanimasala.git`  
`cd Devjanimasala`

### 2. Create & Activate Virtual Environment

- **Windows:**  
  `python -m venv venv`  
  `venv\Scripts\activate`

- **macOS/Linux:**  
  `python3 -m venv venv`  
  `source venv/bin/activate`

### 3. Install Dependencies

`pip install -r requirements.txt`

### 4. Apply Database Migrations

`python manage.py migrate`

### 5. Create a Superuser (Admin Account)

`python manage.py createsuperuser`  
Follow the prompts to set username and password.

### 6. Run the Development Server

`python manage.py runserver`

### 7. Open in Browser

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the site locally.

---

## 🚀 Key Features

- **Secure User Authentication:** Login and logout functionality to protect admin features.  
- **Admin Panel:** Easily add, edit, or delete spice product listings via Django’s built-in admin interface.  
- **Product Management:** Manage detailed spice product information including name, description, and pricing.  
- **Responsive Design:** Simple and clean UI built with Django templates and CSS for a smooth user experience.  
- **Extensible Architecture:** Structured to allow future enhancements like customer-facing pages or e-commerce features.

---

## 📌 Tech Stack

- Python 3.x  
- Django 4.x  
- SQLite (default database)  
- Django Templates (HTML/CSS)

---

## 🙏 Credits

Built and maintained by **Sahar Fatima Devjani**. Special Thanks to  Sir Sannad Bilal (CodeGirls).

---

Feel free to fork, contribute, or raise issues. Feedback is always welcome! 😊
