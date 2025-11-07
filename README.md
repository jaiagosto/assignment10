# 🧮 Assignment 10 - Secure User Authentication with FastAPI

**Author:** Jailene Agosto (ja428)  
**GitHub:** [jaiagosto](https://github.com/jaiagosto)  
**Docker Hub:** [jaiagosto](https://hub.docker.com/u/jaiagosto)

---

## 📋 Project Overview

This project extends Assignment 9 by adding secure user authentication with password hashing, JWT tokens, and comprehensive testing. The application demonstrates professional security practices and CI/CD deployment to Docker Hub.

**Key Features:**
- ✅ Secure User Model with bcrypt password hashing
- ✅ JWT token-based authentication
- ✅ Pydantic validation for user data
- ✅ SQLAlchemy ORM with PostgreSQL
- ✅ Comprehensive unit, integration, and E2E tests
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Docker Hub deployment with multi-platform support
- ✅ Security scanning with Trivy

---

## 🎯 Module 10 Learning Outcomes

This assignment demonstrates:
- **CLO3:** Python applications with automated testing
- **CLO4:** GitHub Actions CI/CD with Docker builds
- **CLO7:** Professional web systems development terminology
- **CLO9:** Containerization with Docker
- **CLO11:** Python programs integrated with SQL databases
- **CLO12:** JSON serialization/validation with Pydantic
- **CLO13:** Secure authentication with encryption, hashing, and encoding

---

## 🛠️ Technologies Used

- **FastAPI** - Modern web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **Passlib + Bcrypt** - Password hashing
- **Python-Jose** - JWT token handling
- **Pytest** - Testing framework
- **Playwright** - E2E testing
- **Docker & Docker Compose** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Trivy** - Security scanning

---

## 🚀 Getting Started

### Prerequisites

- Docker Desktop installed and running
- Git installed
- Python 3.10+ (for local development)

### 1. Clone the Repository
```bash
git clone https://github.com/jaiagosto/assignment10.git
cd assignment10
```

### 2. Start Docker Services
```bash
docker-compose up --build
```

Wait for all services to start (~2 minutes). You should see:
- ✅ PostgreSQL database ready
- ✅ FastAPI app running on port 8000
- ✅ pgAdmin ready on port 5050

### 3. Access the Applications

- **FastAPI Calculator:** http://localhost:8000
- **pgAdmin:** http://localhost:5050
- **API Docs:** http://localhost:8000/docs

---

## 🧪 Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test Categories
```bash
# Unit tests only
pytest tests/unit/ -v

# Integration tests only
pytest tests/integration/ -v

# E2E tests only
pytest tests/e2e/ -v

# With coverage report
pytest tests/ --cov=app --cov-report=html
```

### Run Tests in Docker
```bash
docker-compose run web pytest tests/ -v
```

---

## 📦 Project Structure
```
assignment10/
├── app/
│   ├── auth/
│   │   ├── __init__.py
│   │   └── dependencies.py       # JWT authentication
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py               # User model with hashing
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── base.py               # Base Pydantic schemas
│   │   └── user.py               # User response schemas
│   ├── __init__.py
│   ├── config.py                 # Configuration settings
│   ├── database.py               # SQLAlchemy setup
│   ├── database_init.py          # DB initialization
│   └── operations.py             # Calculator operations
├── tests/
│   ├── auth/
│   │   ├── __init__.py
│   │   └── test_dependencies.py  # Auth tests
│   ├── e2e/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   └── test_e2e.py           # End-to-end tests
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_fastapi_calculator.py
│   │   ├── test_user.py          # User DB tests
│   │   └── test_user_auth.py     # Authentication tests
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_calculator.py
│   │   ├── test_database.py
│   │   └── test_schemas.py       # Schema validation tests
│   ├── __init__.py
│   └── conftest.py               # Test fixtures
├── templates/
│   └── index.html                # Calculator UI
├── .github/
│   └── workflows/
│       └── ci-cd.yml             # CI/CD pipeline
├── docker-compose.yml            # Docker services
├── Dockerfile                    # Container definition
├── main.py                       # FastAPI application
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🔐 Security Features

### Password Hashing
- Uses bcrypt algorithm with automatic salt generation
- Passwords never stored in plain text
- Password strength validation (uppercase, lowercase, digits)

### JWT Authentication
- Token-based authentication
- Secure token generation and verification
- 30-minute token expiration

### Data Validation
- Pydantic schemas validate all user input
- Email format validation
- Username and password length requirements
- Type checking for all fields

---

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Test Job:**
   - Sets up PostgreSQL test database
   - Installs dependencies
   - Runs unit, integration, and E2E tests
   - Generates coverage reports

2. **Security Job:**
   - Builds Docker image
   - Scans for vulnerabilities with Trivy
   - Fails on CRITICAL or HIGH severity issues

3. **Deploy Job:**
   - Builds multi-platform Docker images (amd64, arm64)
   - Pushes to Docker Hub with tags:
     - `jaiagosto/assignment10:latest`
     - `jaiagosto/assignment10:<commit-sha>`
   - Uses layer caching for faster builds

---

## 📊 Test Coverage

The project includes comprehensive tests:

- **Unit Tests:** Schema validation, password hashing, database setup
- **Integration Tests:** User registration, authentication, database operations
- **E2E Tests:** Full application workflow with browser automation
- **Auth Tests:** JWT token handling, user dependencies

Target coverage: **>90%**

---

## 🐳 Docker Hub

**Repository:** https://hub.docker.com/r/jaiagosto/assignment10

### Pull and Run
```bash
docker pull jaiagosto/assignment10:latest
docker run -p 8000:8000 jaiagosto/assignment10:latest
```

---

## 📝 Environment Variables

Create a `.env` file for local development:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🔧 Development Commands

### Start Development Server
```bash
uvicorn main:app --reload
```

### Create Database Tables
```bash
python -m app.database_init
```

### Run Linting
```bash
pylint app/
```

### Format Code
```bash
black app/ tests/
```

---

## 🎓 Key Learnings

### Secure Authentication
- Implementing bcrypt password hashing
- JWT token generation and verification
- Secure session management

### Database Integration
- SQLAlchemy ORM patterns
- Database migrations
- Transaction management
- Constraint handling

### Testing Strategies
- Unit testing with mocks
- Integration testing with real database
- E2E testing with Playwright
- Test fixtures and parametrization

### DevOps Practices
- Multi-stage Docker builds
- CI/CD automation
- Security scanning
- Multi-platform deployments

---

## 📎 Links

- **GitHub Repository:** https://github.com/jaiagosto/assignment10
- **Docker Hub:** https://hub.docker.com/r/jaiagosto/assignment10
- **API Documentation:** http://localhost:8000/docs (when running)

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👩‍💻 Author

**Jailene Agosto**  
UCID: ja428  
Assignment: Module 10 - Secure User Authentication