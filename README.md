# FastAPI JWT Auth & Calculation API (Module 13)
This project is a secure FastAPI application for user authentication using JWT and basic calculation features. It includes a front-end for login and registration, full E2E testing with Playwright, and CI/CD integration via GitHub Actions and Docker Hub.


## Features

- JWT-based User Authentication
- `/api/register` hashes passwords and stores users securely
- `/api/login` verifies credentials and returns JWT
- Front-End Pages
- `register.html` and `login.html` with client-side validation
- JWT stored in `localStorage` after login
- Calculation CRUD
- Full Create, Read, Update, Delete (BREAD) endpoints for calculations
- Security
- Passwords hashed with `bcrypt` via `passlib`
- Data validated using Pydantic v2 models
- Testing
- Playwright E2E tests for auth flow
- Pytest integration and unit tests
- CI/CD
- GitHub Actions pipeline spins up PostgreSQL and FastAPI
- Runs all tests and pushes Docker image on success

## Project Structure
- module12/
    - ├── app/
    - │ ├── init.py
    - │ ├── main.py
    - │ ├── models.py
    - │ ├── schemas.py
    - │ ├── security.py
    - │ ├── database.py
    - │ ├── auth.py
    - │ └── routes/
    - │     └── users.py
    - │     └── calculations.py
    - ├── tests/
    - │ ├── init.py
    - │ ├── test_auth_e2e.py
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

- git clone <https://github.com/eddysantana16/module13.git>
- cd <module13>
- pip install -r requirements.txt
- uvicorn app.main:app --reload
- open: Open http://localhost:8000/register or http://localhost:8000/login
- API docs: http://localhost:8000/docs


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
- to run tests locally: pytest tests/
- Includes full coverage for: user registration, Calculation: Create, Read, Update, Delete, Invalid ID

## Docker Hub Repository
- docker pull <eddysantana>/fastapi-userapp:latest
- docker run -d -p 8000:8000 <eddysantana>/fastapi-userapp:latest
- Visit: http://localhost:8000
- Docker Image URL: 

## Author
- Eddy Santana