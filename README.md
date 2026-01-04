# Smart ToDo API
## Project Overview

Smart ToDo API is a secure and scalable RESTful backend service designed to manage personal tasks efficiently.
It allows users to register, authenticate, and manage their tasks using JWT-based authentication.

This project demonstrates real-world backend development skills, including authentication, database integration, protected routes, and API documentation using Swagger.

## Objective 

In many productivity applications, users need a secure and reliable backend to:

-Create and manage personal tasks

-Ensure data privacy between users

-Authenticate users securely

-Perform CRUD operations efficiently

Smart ToDo API solves this by providing a JWT-secured task management backend, suitable for real-world applications like productivity apps, team dashboards, or SaaS platforms.

## Key Features

User Registration & Login

JWT Authentication & Authorization

Protected Task CRUD APIs

MongoDB Atlas integration

Swagger (OpenAPI) documentation

Clean, modular project structure

## Tech Stack
| Category           | Technology                 |
| ------------------ | -------------------------- |
| Backend Framework  | FastAPI                    |
| Language           | Python                     |
| Authentication     | JWT (OAuth2PasswordBearer) |
| Database           | MongoDB Atlas              |
| ODM                | PyMongo                    |
| Security           | Passlib (bcrypt)           |
| Environment Config | python-dotenv              |
| API Documentation  | Swagger UI                 |

📂 Project Structure
```bash
smart-todo-api/
│
├── main.py                 # FastAPI app entry point
├── database.py             # MongoDB connection setup
├── auth.py                 # JWT & password utilities
├── models.py               # Pydantic models
│
├── routes/
│   ├── user_routes.py      # Register & Login APIs
│   ├── task_routes.py      # Protected Task APIs
│
├── .env.example            # Sample environment config
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
```



# Installation & Local Setup

1️ Clone the Repository
```bash
git clone https://github.com/your-username/smart-todo-api.git
cd smart-todo-api
```
2️. Create & Activate Virtual Environment

```bash
python -m venv venv
```

3. Install Dependencies

 ```bash
pip install -r requirements.txt
```

4️. Setup Environment Variables

Create a .env file using .env.example:
```bash

MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/smart_todo_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5️. Run the Application

```bash
uvicorn main:app --reload
```

## API Documentation (Swagger)

Once the server is running, open:

http://127.0.0.1:8000/docs

This provides:

-Interactive API testing

-Request/response schemas

-Authorization support

## API Endpoints
 Authentication

### POST /register
Registers a new user.
```bash
{
  "name": "Eshani",
  "email": "eshani@gmail.com",
  "password": "test1234"
}
```


### POST /login
Authenticates user and returns JWT token.
```bash

{
  "email": "eshani@gmail.com",
  "password": "test1234"
}
```

Response:
```bash
{
  "access_token": "eyJhbGciOi...",
  "token_type": "bearer"
}
```
### Tasks (JWT Protected)

All task routes require
Authorization: Bearer <ACCESS_TOKEN>

## POST /tasks – Create a task
```bash
{
  "title": "First Task",
  "description": "My first protected task"
}
```


### GET /tasks – Fetch all user tasks

### PUT /tasks/{id} – Update a task
```bash
{
  "title": "Updated Title",
  "completed": true
}
````


### DELETE /tasks/{id} – Delete a task

## Conclusion

This project demonstrates a production-ready backend architecture with secure authentication, clean API design, and real-world database integration — suitable for Python Backend or API Developer roles.
