# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple RESTful API using the FastAPI framework. Students will implement CRUD endpoints, define request/response models with Pydantic, and run the service locally using Uvicorn.

## 📝 Tasks

### 🛠️ Create the API Endpoints

#### Description
Implement a small REST API that manages a collection of "items" (or resources). Provide endpoints to create, read, update, and delete items.

#### Requirements
Completed program should:

- Expose REST endpoints for `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, and `DELETE /items/{id}`
- Use Pydantic models for request validation and response serialization
- Store data in an in-memory store (dictionary) for simplicity
- Return appropriate HTTP status codes for success and error cases

Example usage (from the assignment folder):

```bash
cd assignments/fastapi-rest-apis
uvicorn starter-code:app --reload
# Create an item
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name":"Apple","price":1.5}'
# List items
curl "http://127.0.0.1:8000/items/"
```

### 🛠️ Add Validation and Error Handling

#### Description
Ensure the API validates incoming data and handles common error scenarios such as missing resources.

#### Requirements
Completed program should:

- Validate request bodies using Pydantic models (required fields, types, basic constraints)
- Return `404 Not Found` when a requested item does not exist
- Return `400 Bad Request` for invalid input where appropriate

### 🛠️ Optional: Testing and Enhancements

#### Description
Add tests or enhancements to make the API more production-like.

#### Requirements
Completed program may optionally:

- Include simple endpoint tests using `requests` or `httpx`
- Add filtering or search to `GET /items`
- Persist data to a lightweight SQLite DB using `databases` or SQLAlchemy


## Getting Started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app (from the assignment folder):

```bash
cd assignments/fastapi-rest-apis
uvicorn starter-code:app --reload
```

3. Open `http://127.0.0.1:8000/docs` to explore the interactive OpenAPI docs.
