# Django MongoDB CRUD API (ORM)

This project is a simple Django application that provides CRUD operations via REST API, using DB with Django's ORM and models.

you can configure your Django project to use different databases. Just update the requirements.txt and settings.py to match the database you're using, and the rest of your code remains the same.

## Features

- Create, Read, Update, and Delete items in MongoDB.
- REST API endpoints for CRUD operations.
- DB interactions.

## Requirements

- Python 3.x
- Django
- Django REST Framework


## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Atique22/crud-django.git
    cd crud-django
    ```

2. **Create and activate a virtual environment:**

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Update MongoDB connection settings:**

    Update `MONGODB_URI` in `settings.py` to match your MongoDB configuration.

5. **Run the server:**

    ```sh
    python manage.py runserver
    ```

## API Endpoints

- `GET /api/items/` - List all items
- `POST /api/items/create/` - Create a new item
- `GET /api/items/<id>/` - Retrieve an item by ID
- `PUT /api/items/<id>/update/` - Update an item by ID
- `DELETE /api/items/<id>/delete/` - Delete an item by ID

