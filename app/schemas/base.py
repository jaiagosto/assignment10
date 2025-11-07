from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional

class UserBase(BaseModel):
    """Base schema for user with common fields"""
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)

class PasswordMixin(BaseModel):
    """Mixin for password validation"""
    password: str = Field(..., min_length=6)
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Validate password strength"""
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v

class UserCreate(UserBase, PasswordMixin):
    """Schema for creating a new user"""
    pass

class UserLogin(BaseModel):
    """Schema for user login"""
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)