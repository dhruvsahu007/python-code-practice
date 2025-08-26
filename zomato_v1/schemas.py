from pydantic import BaseModel, Field, constr, field_validator
from typing import Optional
from datetime import time, datetime

PHONE_REGEX = r"^\+?\d{7,15}$"

class RestaurantBase(BaseModel):
    name: constr(min_length=3, max_length=100)
    description: Optional[str] = None
    cuisine_type: constr(min_length=2, max_length=50)
    address: constr(min_length=3)
    phone_number: constr(pattern=PHONE_REGEX)
    rating: Optional[float] = Field(default=0.0, ge=0.0, le=5.0)
    is_active: Optional[bool] = True
    opening_time: Optional[time] = None
    closing_time: Optional[time] = None

    @field_validator("closing_time")
    def validate_times(cls, v, info):
        ot = info.data.get("opening_time")
        if ot and v:
            if v == ot:
                raise ValueError("closing_time must be different from opening_time")
        return v


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantUpdate(BaseModel):
    name: Optional[constr(min_length=3, max_length=100)] = None
    description: Optional[str] = None
    cuisine_type: Optional[constr(min_length=2, max_length=50)] = None
    address: Optional[constr(min_length=3)] = None
    phone_number: Optional[constr(pattern=PHONE_REGEX)] = None
    rating: Optional[float] = Field(None, ge=0.0, le=5.0)
    is_active: Optional[bool] = None
    opening_time: Optional[time] = None
    closing_time: Optional[time] = None

    @field_validator("closing_time")
    def validate_times(cls, v, info):
        ot = info.data.get("opening_time")
        if ot and v:
            if v == ot:
                raise ValueError("closing_time must be different from opening_time")
        return v


class RestaurantOut(RestaurantBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

