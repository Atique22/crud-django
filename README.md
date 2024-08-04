# Django MongoDB CRUD API

This project is a simple Django application that provides CRUD operations via REST API, using MongoDB without relying on Django's ORM and models.

## Features

- Create, Read, Update, and Delete items in MongoDB.
- REST API endpoints for CRUD operations.
- Uses `pymongo` for MongoDB interactions.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- pymongo

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/django-mongodb-crud-api.git
    cd django-mongodb-crud-api
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

