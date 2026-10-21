# Django Support Ticket API

A REST API built with Django and Django REST Framework for managing support tickets, with token-based authentication, ticket status tracking, health monitoring, logging, and automated tests.

## Features

- User registration and token-based login
- Create, list, retrieve, and update support tickets
- Ticket status tracking: OPEN, IN_PROGRESS, RESOLVED
- Ticket priority levels: LOW, MEDIUM, HIGH
- Authentication-protected ticket endpoints
- Health-check endpoint with database connectivity status
- Application logging to a file
- Automated API tests

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Token Authentication
- Git and GitHub

## Installation and Setup

1. Clone the repository:

   git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate into the project folder:

   cd Django-Support-API

3. Create and activate a virtual environment:

   python -m venv .venv

   Windows PowerShell:

   .\.venv\Scripts\Activate.ps1

4. Install dependencies:

   pip install django djangorestframework

5. Apply database migrations:

   python manage.py migrate

6. Start the development server:

   python manage.py runserver

## API Endpoints

| Method | Endpoint | Purpose |

| GET | /health/ | Check application and database health |
| POST | /api/tickets/register/ | Register a user |
| POST | /api/tickets/login/ | Obtain an authentication token |
| GET | /api/tickets/ | List tickets |
| POST | /api/tickets/ | Create a ticket |
| GET | /api/tickets/<id>/ | Retrieve a ticket |
| PATCH | /api/tickets/<id>/ | Update a ticket |

Ticket endpoints require token authentication unless configured otherwise.

For authenticated requests, include this header:

Authorization: Token YOUR_AUTH_TOKEN

## Run Automated Tests

Run the test suite with:

python manage.py test tickets

The project currently includes tests for health checks, ticket creation, authentication, listing, and updating.

## Logging

Application logs are stored in:

logs/django.log

## Future Improvements

- Ticket deletion tests and additional validation tests
- API documentation with Swagger or OpenAPI
- Continuous integration using GitHub Actions
- Deployment configuration and production security hardening

## Disclaimer

This project is intended for learning and portfolio demonstration. Configure production security settings before deploying it publicly.
