# Django Hotel Reservation System 🏨  

This is an **open-source** Django-based hotel reservation system that integrates with **MongoDB** using `djongo`. The project includes a frontend for user interaction and a backend that handles reservations, guest details, and payment information. However, there's an issue with MongoDB connectivity that needs fixing. **Contributions are welcome!** 🚀  

###
![ScreenShot Tool -20250129080502](https://github.com/user-attachments/assets/70f6aea5-db47-49cc-ab45-aad03a408a51)
###

## 📌 Features  
✅ User-friendly reservation form  
✅ Stores guest details, stay details, and payment info  
✅ Uses Django's ModelForm for easy form handling  
✅ MongoDB as the database (via `djongo`)  
✅ Open for collaboration to fix MongoDB connection issues  

---

## 🛠️ Project Structure  

```
myapp/ 
│── manage.py             # Django project management script
│── myapp/                # Main Django app
│   │── settings.py       # Django settings (MongoDB configured)
│   │── urls.py           # URL configurations
│   └── wsgi.py           # WSGI application
│
└── userform/             # App handling user reservations
    │── models.py         # Database models (HotelReservation)
    │── forms.py          # Django ModelForm for reservations
    │── views.py          # Views for handling form submission
    │── templates/        # HTML templates (reservation form)
    └── urls.py           # App-specific routes
```

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository  

```sh
git clone https://github.com/your-username/django-hotel-reservation.git
cd django-hotel-reservation
```

### 2️⃣ Create a Virtual Environment  

```sh
python3 -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```

### 3️⃣ Install Dependencies  

```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up MongoDB Connection  

Ensure **MongoDB** is running and update the credentials in `settings.py`:  

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'django',  
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'username': 'your-username',
            'password': 'your-password',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}
```

### 5️⃣ Run Migrations  

```sh
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start the Django Server  

```sh
python manage.py runserver
```

Visit **`http://127.0.0.1:8000/reservation/`** in your browser.

---

## 🐞 Issue: MongoDB Connection Not Working  

Currently, **MongoDB integration with Django (`djongo`) is not working**. The issue might be related to:  
- Incorrect authentication settings  
- `djongo` version compatibility  
- MongoDB not allowing remote connections  

If you have experience with Django + MongoDB, **please contribute!** 🙌  

---

## 🤝 How to Contribute  

1. **Fork** the repository  
2. Create a **new branch** (`fix-mongodb-connection`)  
3. Commit your changes  
4. Open a **Pull Request**  

---

## 📜 License  

This project is **open-source** and available under the **MIT License**.

---

### 💡 Contributors  

👤 **Your Name** – _Rohan Kumar_  
✉️ Contact: dev@rkatkam.com  

If you can help with MongoDB, feel free to **submit a PR or open an issue!** 🚀
