import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from typing import Dict
from app.database import Base
from app.models.user import User

# Initialize Faker
fake = Faker()
Faker.seed(12345)  # For reproducible test data

# Test database URL
TEST_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/fastapi_db")

@pytest.fixture(scope="session")
def test_engine():
    """Create a test database engine."""
    engine = create_engine(TEST_DATABASE_URL, echo=True)
    return engine

@pytest.fixture(scope="session")
def test_sessionmaker(test_engine):
    """Create a sessionmaker for tests."""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    return TestingSessionLocal

@pytest.fixture(scope="function")
def db_session(test_engine, test_sessionmaker):
    """
    Provide a transactional scope for each test function.
    Creates tables, provides a session, then rolls back and cleans up.
    """
    # Create all tables
    Base.metadata.create_all(bind=test_engine)
    
    # Create a new session for the test
    session = test_sessionmaker()
    
    yield session
    
    # Rollback and close session
    session.rollback()
    session.close()
    
    # Drop all tables after test
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def fake_user_data() -> Dict[str, str]:
    """
    Generate a dictionary of fake user data for testing.
    
    Returns:
        A dict containing user fields with fake data.
    """
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "username": fake.unique.user_name(),
        "password": fake.password(length=12)
    }

@pytest.fixture
def create_fake_user():
    """
    Factory function to create multiple fake users.
    """
    def _create_fake_user() -> Dict[str, str]:
        return {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.unique.email(),
            "username": fake.unique.user_name(),
            "password": fake.password(length=12)
        }
    return _create_fake_user