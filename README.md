# Sticky Notes App (Django Mini Project)

This project is a simple Sticky Notes web application built using Django.
The main idea of this app is to allow users to create, manage, and organize their personal notes online.

Each user can register, log in, and then create their own notes.
All notes are private, meaning one user cannot see another user’s notes.

---

## Features

- User registration and login system
- Create new notes
- Edit existing notes
- Delete notes with confirmation
- Each note has a custom background color
- Notes are user-specific (private)
- Simple and clean user interface

---

## Technologies Used

- Python
- Django
- SQLite (default database)
- HTML, CSS
- Bootstrap (for styling)

---

## How to Run the Project

Follow these steps:

1. Install Django:
   pip install django

2. Go to the project folder:
   cd sticky_project

3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

4. (Optional) Create admin user:
   python manage.py createsuperuser

5. Start the server:
   python manage.py runserver

6. Open in browser:
   http://127.0.0.1:8000/

---

## How It Works

- First, the user registers an account
- Then logs in using username and password
- After login, the user is redirected to the notes page
- User can create, edit, and delete notes
- Each note belongs to the logged-in user only

---

## Important Concepts Used

- Django Models for database
- ModelForms for handling forms
- Function-based views
- Authentication system (login/logout)
- Template inheritance
- CRUD operations (Create, Read, Update, Delete)

---

## Extra Improvements

- Notes are displayed with colors like sticky notes
- Clean UI using Bootstrap
- Delete confirmation added

---

## Author

Name: Muhammad Nadeem
Roll Number: 22P-9366

---
