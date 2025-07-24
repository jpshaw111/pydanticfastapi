# 🚀 FastAPI User CRUD API with MySQL

This is a mini-project using **FastAPI**, **Pydantic**, **SQLAlchemy**, and **MySQL** that allows you to:

- ✅ Create a new user
- ✅ View all users
- ✅ Update a user
- ✅ Delete a user

---

## 🧰 Tech Stack

- ⚙️ FastAPI — web framework
- 🧱 SQLAlchemy — ORM for database interaction
- 🛡️ Pydantic — data validation (like Laravel FormRequest)
- 🐬 MySQL — database
- 🔌 Uvicorn — server

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/jpshaw111/pydanticfastapi.git
cd pydanticfastapi


python -m venv venv
# On Linux/macOS
source venv/bin/activate
# On Windows
venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy pymysql pydantic email-validator


uvicorn main:app --reload


