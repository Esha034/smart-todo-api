#  Smart ToDo API

A secure RESTful backend API for task management built using **FastAPI**, **MongoDB Atlas**, and **JWT Authentication**.

---

##  Features
- User registration and login
- JWT-based authentication
- Protected CRUD APIs for tasks
- MongoDB Atlas integration
- Swagger API documentation

---

## Tech Stack
- Python
- FastAPI
- MongoDB Atlas
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn

---

##  Project Structure
smart-todo-api/
├── main.py
├── auth.py
├── database.py
├── models.py
├── dependencies.py
├── routes/
│ ├── user_routes.py
│ ├── task_routes.py
├── .env.example
├── requirements.txt
├── README.md

---

##  Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/<your-username>/smart-todo-api.git
cd smart-todo-api
### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
### 3️⃣ Install Dependencies

pip install -r requirements.txt
### 4️⃣ Environment Variables Setup
Create a .env file using the template:

cp .env.example .env
Fill in your values:

MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
5️⃣ Run the Application

uvicorn main:app --reload
Open Swagger UI:

http://127.0.0.1:8000/docs
##  API Endpoints
Authentication
POST /register

POST /login

Tasks (JWT Protected)
POST /tasks

GET /tasks

PUT /tasks/{id}

DELETE /tasks/{id}

## Testing
-Swagger UI

-PowerShell curl

-Postman

👩‍💻 Author
Eshani

