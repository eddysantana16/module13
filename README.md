# FastAPI User & Calculation API (Module 12)
This project is a secure FastAPI application that includes both user authentication and calculation CRUD functionality. It uses SQLAlchemy for ORM, Pydantic for schema validation, and is fully tested, containerized with Docker, and integrated with a CI/CD pipeline via GitHub Actions and Docker Hub.

## Features

- User registration with password hashing using `passlib`
- Full Calculation CRUD (Browse, Read, Edit, Add, Delete)
- Pydantic v2-compliant schemas using `model_config`
- Integration tests using `pytest` and PostgreSQL in CI
- GitHub Actions workflow with PostgreSQL service
- Docker image built and pushed to Docker Hub on every push to `main`

## Project Structure
- module12/
    - ├── app/
    - │ ├── init.py
    - │ ├── main.py
    - │ ├── models.py
    - │ ├── schemas.py
    - │ ├── security.py
    - │ ├── database.py
    - │ └── routes/
    - │     └── users.py
    - │     └── calculations.py
    - ├── tests/
    - │ ├── init.py
    - │ ├── test_security.py
    - │ └── test_users.py
    - │ └── test_calculations.py
    - ├── requirements.txt
    - ├── README.md
    - ├── Dockerfile
    - ├── pytest.ini
    - └── .github/
    -       └── workflows/
    -           └── ci.yml

## Running the App Locally

- Make sure you have Python 3.11 and PostgreSQL installed locally, or use Docker to simulate the DB.
- Clone the repo
- Install dependencies: pip install -r requirements.txt
- uvicorn app.main:app --reload
- open: http://127.0.0.1:8000/docs


## Run with Docker

- docker pull eddysantana/fastapi-userapp:latest
- docker run -d -p 8000:8000 eddysantana/fastapi-userapp:latest
- Open your web browser: http://localhost:8000/docs 

## CI/CD Workflow
- GitHub Actions is configured to:
- Spin up a PostgreSQL container
- Install dependencies
- Run unit + integration tests
- If all tests pass, build and push the Docker image to Docker Hub
- File: .github/workflows/ci.yml

## Testing
- to run tests locally: pytest
- cludes full coverage for: user registration, Calculation: Create, Read, Update, Delete, Invalid ID

## Docker Hub Repository
- Docker Image URL: https://hub.docker.com/r/eddysantana/fastapi-userapp

## Author
- Eddy Santana