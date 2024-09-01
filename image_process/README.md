# Image Processing System

This project processes image data from CSV files, compresses the images, and stores the results in a database.

## Features
- Asynchronous image processing.
- CSV file upload and validation.
- Webhook integration for processing completion.
- Status check for processing requests.

## Tech Stack
- FastAPI
- PostgreSQL
- Docker

## Setup
1. Clone the repository.
2. Run `docker-compose up --build` to start the application.
3. Access the API at `http://localhost:8000`.

## API Endpoints
- `POST /upload`: Upload a CSV file.
- `GET /status/{request_id}`: Check the status of the image processing.
- `POST /webhook`: Webhook endpoint to handle processing completion.
