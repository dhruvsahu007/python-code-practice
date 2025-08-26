from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime, time
import re

class RestaurantBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Restaurant name")
    description: Optional[str] = Field(None, description="Restaurant description")
    cuisine_type: str = Field(..., min_length=1, max_length=50, description="Type of cuisine")
    address: str = Field(..., min_length=5, max_length=255, description="Restaurant address")
    phone_number: str = Field(..., description="Phone number")
    rating: Optional[float] = Field(0.0, ge=0.0, le=5.0, description="Rating from 0.0 to 5.0")
    is_active: Optional[bool] = Field(True, description="Whether restaurant is active")
    opening_time: time = Field(..., description="Opening time")
    closing_time: time = Field(..., description="Closing time")
    
    @validator('phone_number')
    def validate_phone_number(cls, v):
        # Basic phone number validation (10-15 digits with optional +, -, space, parentheses)
        pattern = r'^[\+]?[\d\s\-\(\)]{10,15}$'
        if not re.match(pattern, v.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')):
            raise ValueError('Invalid phone number format')
        return v
    
    @validator('closing_time')
    def validate_closing_time(cls, v, values):
        if 'opening_time' in values and v <= values['opening_time']:
            raise ValueError('Closing time must be after opening time')
        return v

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = None
    cuisine_type: Optional[str] = Field(None, min_length=1, max_length=50)
    address: Optional[str] = Field(None, min_length=5, max_length=255)
    phone_number: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0.0, le=5.0)
    is_active: Optional[bool] = None
    opening_time: Optional[time] = None
    closing_time: Optional[time] = None
    
    @validator('phone_number')
    def validate_phone_number(cls, v):
        if v is not None:
            pattern = r'^[\+]?[\d\s\-\(\)]{10,15}$'
            if not re.match(pattern, v.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')):
                raise ValueError('Invalid phone number format')
        return v

class RestaurantResponse(RestaurantBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class RestaurantList(BaseModel):
    restaurants: list[RestaurantResponse]
    total: int
    skip: int
    limit: int
