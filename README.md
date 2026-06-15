# Doctor Appointment Booking System

A web-based Doctor Appointment Booking System developed using Django. This application allows users to register, log in, browse available doctors, and book appointments online.

Features

* User Registration and Login
* Doctor Listing Page
* Doctor Profile Display
* Appointment Booking Form
* Appointment Registration and Storage
* Success Confirmation Page
* Admin Panel for Database Management

Tech Stack

Frontend
* HTML5
* CSS3
* Bootstrap

Backend
* Python
* Django

Database
* SQLite3

Additional Libraries
Pillow (Required for handling image uploads using Django ImageField)

## Project Structure

fullstack1405/
│
├── manage.py
├── db.sqlite3
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── myapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
├── static/
└── media/

Database Models

##Userinfo

Stores user account details.

| Field    | Type      |
| -------- | --------- |
| email    | CharField |
| password | CharField |

### Doctorinfo

Stores doctor information.

| Field          | Type       |
| -------------- | ---------- |
| doctor_name    | CharField  |
| doc_img        | ImageField |
| specialization | CharField  |

### Register

Stores appointment details.

| Field            | Type      |
| ---------------- | --------- |
| doctor_name      | CharField |
| patient_name     | CharField |
| appointment_date | DateField |
| reason           | TextField |

## Installation Guide

1. Clone the Repository

git clone <repository-url>
cd fullstack1405

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

Windows
venv\Scripts\activate

Linux / macOS
source venv/bin/activate

4. Install Dependencies

pip install django pillow

5. Create Database Migrations

python manage.py makemigrations

6. Apply Migrations

python manage.py migrate

7. Run the Development Server

python manage.py runserver

Application Workflow

1. User creates an account.
2. User logs into the system.
3. User browses available doctors.
4. User selects a doctor.
5. User fills in appointment details.
6. Appointment is stored in the database.
7. Success page confirms the booking.

Admin Panel Access

To access the Django Admin Panel:
http://127.0.0.1:8000/admin/

Create an admin account first:
python manage.py createsuperuser

## Future Enhancements

* Django Authentication System
* Password Encryption using Django Auth
* Email Notifications
* Doctor Availability Scheduling
* Appointment Cancellation
* Online Payment Integration
* Patient Dashboard
* Doctor Dashboard
* Appointment History
* Responsive Mobile Design

## Learning Outcomes

This project demonstrates:

* Django Project Structure
* URL Routing
* Models and Database Integration
* Form Handling
* Template Rendering
* CRUD Operations
* Media File Uploads
* User Authentication Concepts
* Django Admin Configuration

## License

This project was developed for educational and learning purposes.

Feel free to modify and extend the project according to your requirements.
