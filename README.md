# FastAPI Backend for K2 Authentication

This project provides a backend API for authentication using FastAPI, with SQLite as the database. It supports user registration and login functionalities.

## Features

- User registration (`/auth/signup`)
- User login (`/auth/login`)
- Token-based authentication
- SQLite database integration

## Installation
### Prerequisites

- Python 3.10 or higher
- Git

### Clone the Repository

```bash
git clone https://github.com/aoc78/k2-back-auth.git
cd k2-back-auth
```
## Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### Running the Application Locally
```bash
uvicorn main:app --reload
```


