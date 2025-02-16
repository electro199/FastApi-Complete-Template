# FastAPI Server Template

A minimal and scalable FastAPI server template for building RESTful APIs quickly.

## Features
- FastAPI framework for high-performance APIs
- Automatic interactive API documentation (Swagger)
- Pydantic for data validation
- Async support for high concurrency
- CORS support
- Environment variable configuration
- Logging and error handling
- Ready `Config` class with `.env` example and validation for `int`, `float`, `str`, and missing values
- FastAPI email client
- Middleware example class
- Ready model for `User` and `Item` as examples
- Custom logger with file logging and console logging with auto colors
- alembic support for migrations
## Installation

### Clone the repository
```sh
git clone https://github.com/electro199/FastApi-Complete-Template
cd fastapi-server-template
```

### Install dependencies

```sh
pip install -r requirements.txt
```

## Running the Server

### Using Uvicorn
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
or
```sh
python3 run.py
```


## API Documentation
After running the server, access API docs at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

## Environment Variables
Create a `.env` file by renaming .env.template:

## Deployment
To deploy on production, run Uvicorn:
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000
```


## License
This project is licensed under the MIT License.

