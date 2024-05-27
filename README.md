
# Virtual Car Dealership

This is a Django-based web application for managing a virtual car dealership. It includes features for user authentication, managing car listings, and more.

## Features

- User Authentication (Login, Registration)
- Car Listings Management
- Admin Interface for Managing Data

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Database](#database)
- [Static and Media Files](#static-and-media-files)
- [Running the Project](#running-the-project)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- Virtualenv
- Git

### Clone the Repository

git clone https://github.com/yourusername/virtual-car-dealership.git
cd virtual-car-dealership


### Create and Activate Virtual Environment

python -m venv env
source env/bin/activate  # On Unix or MacOS
# or
env\Scripts\activate  # On Windows

### Install Dependencies

pip install -r requirements.txt

## Usage

### Setting Up Environment Variables

Create a `.env` file in the project root and add the following:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

### Apply Migrations

python manage.py migrate

### Create a Superuser

python manage.py createsuperuser

### Run the Development Server

python manage.py runserver

### Access the Application

Open your browser and navigate to `http://127.0.0.1:8000`

## Project Structure

VIRTUAL-CAR-DEALERSHIP/
│
├── accounts/                   # App directory for user accounts
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── cars/                       # App directory for car listings
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── dealership/                 # Project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── env/                        # Virtual environment directory
│
├── static/                     # Static files directory
│   ├── css/
│   │   └── styles.css
│   └── images/
│       ├── banner.png
│       └── logo.svg
│
├── templates/                  # Templates directory
│   └── user_authentication/
│       ├── login.html
│       ├── register.html
│       └── base.html
│
├── user_authentication/        # App directory for authentication
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── .env                        # Environment variables file
├── .gitignore                  # Git ignore file
├── db.sqlite3                  # SQLite database file
├── manage.py                   # Django management script
├── README.md                   # Readme file
└── requirements.txt            # Project dependencies

## Environment Variables

The `.env` file should include:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

## Database

The project uses SQLite by default, which is suitable for development and testing. For production, consider using a more robust database like PostgreSQL.

## Static and Media Files

### Static Files

Static files (CSS, JavaScript, images) are stored in the `static` directory. To collect static files into a single location for production, run:

python manage.py collectstatic

### Media Files

Media files uploaded by users are stored in the `media` directory. Ensure `MEDIA_URL` and `MEDIA_ROOT` are correctly set in `settings.py`:

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

## Running the Project

### Development Server

To start the development server, run:

python manage.py runserver

Then open your browser and go to `http://127.0.0.1:8000`.

### Production Server

For production, you should use a WSGI server like Gunicorn along with a web server like Nginx. Ensure you configure your settings accordingly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.