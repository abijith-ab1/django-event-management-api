Sure, here is a more detailed README file structured differently for your project:

---

# Event Management System

A comprehensive Event Management System built with Django Rest Framework (DRF) that facilitates user authentication, event creation and management, registration handling, and generating reports.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Users](#users)
  - [Events](#events)
  - [Registrations](#registrations)
  - [Reports](#reports)
  - [Counts](#counts)
- [Postman Collection](#postman-collection)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- User authentication using JWT
- Role-based access control
- Create, view, update, and delete events
- Register for events
- Send email notifications for events
- Generate reports for users and events
- Count events and registrations

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django Rest Framework 3.12+
- djangorestframework-simplejwt 4.8+

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/event-management-system.git
cd event-management-system
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## Usage

### Authentication

- Obtain Token: `POST /api/token/`
- Refresh Token: `POST /api/token/refresh/`

### Users

- List Users: `GET /api/users/` (Admin only)
- Create User: `POST /api/users/`
- Retrieve User: `GET /api/users/<id>/` (Admin only)
- Update User: `PUT /api/users/<id>/` (Admin only)
- Delete User: `DELETE /api/users/<id>/` (Admin only)

### Events

- List Events: `GET /api/events/`
- Create Event: `POST /api/events/` (Authenticated users only)
- Retrieve Event: `GET /api/events/<id>/` (Authenticated users only)
- Update Event: `PUT /api/events/<id>/` (Authenticated users only)
- Delete Event: `DELETE /api/events/<id>/` (Authenticated users only)

### Registrations

- List Registrations: `GET /api/registrations/` (Authenticated users only)
- Create Registration: `POST /api/registrations/` (Authenticated users only)
- Retrieve Registration: `GET /api/registrations/<id>/` (Authenticated users only)
- Update Registration: `PUT /api/registrations/<id>/` (Authenticated users only)
- Delete Registration: `DELETE /api/registrations/<id>/` (Authenticated users only)

### Reports

- User Report: `GET /api/reports/users/` (Admin only)
- Event Report: `GET /api/reports/events/` (Admin only)

### Counts

- Event and Registration Counts: `GET /api/count/` (Admin only)

## Postman Collection

Here are some example Postman requests:

### Obtain JWT Token

- **URL**: `http://localhost:8000/api/token/`
- **Method**: POST
- **Body** (raw, JSON):
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

### Create Event

- **URL**: `http://localhost:8000/api/events/`
- **Method**: POST
- **Headers**:
  - `Authorization: Bearer <your_token>`
  - `Content-Type: application/json`
- **Body** (raw, JSON):
  ```json
  {
    "name": "Tech Conference",
    "description": "An annual conference for tech enthusiasts.",
    "date": "2024-08-01T10:00:00Z"
  }
  ```
