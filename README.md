# Simple FastAPI App
This project is a basic FastAPI application demonstrating CRUD operations with a SQLite database. It includes Docker support for containerized deployment.

## Features
- Basic CRUD operations for managing items.
- SQLite database integration.
- Docker support for easy deployment.
## Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
## Installation
1. Clone the repository:
```bash
git clone https://github.com/Fantasista766/simple-fast-api-app.git
cd simple-fast-api-app
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Running the App
### Locally
1. Start the FastAPI application:
```bash
uvicorn main:app --reload
```
2. Open your browser and navigate to http://127.0.0.1:8000/docs to access the interactive API documentation.
### Using Docker
1. Build the Docker image:
```bash
docker build -t simple-fast-api-app .
```
2. Run the Docker container:
```bash
docker run -d -p 8000:8000 simple-fast-api-app
```
3. Open your browser and navigate to http://127.0.0.1:8000/docs to access the interactive API documentation.
## Project Structure
- main.py: The main application file where the FastAPI app is defined.
- database.py: Database connection and setup.
- repository.py: CRUD operations.
- router.py: API route definitions.
- schemas.py: Pydantic models for request and response validation.
- Dockerfile: Docker configuration for containerizing the application.
- requirements.txt: Python dependencies.