# Zomato V1 - Restaurant Management System

A basic restaurant listing system built with FastAPI, SQLAlchemy, and SQLite. This is Version 1 of a progressive food delivery application.

## Features

- Complete CRUD operations for restaurants
- Restaurant data validation and error handling
- Async SQLAlchemy with SQLite database
- RESTful API with proper HTTP status codes
- Input validation (phone number format, rating range, time validation)
- Search functionality by cuisine type
- Filter active restaurants
- Pagination support
- Comprehensive API documentation with FastAPI

## Restaurant Model

The restaurant model includes the following fields:
- `id` - Primary Key
- `name` - Required, 3-100 characters, unique
- `description` - Optional text
- `cuisine_type` - Required (e.g., "Italian", "Chinese", "Indian")
- `address` - Required
- `phone_number` - Required with validation
- `rating` - Float, 0.0-5.0, default 0.0
- `is_active` - Boolean, default True
- `opening_time` - Time
- `closing_time` - Time
- `created_at` - Timestamp
- `updated_at` - Timestamp

## API Endpoints

### Restaurants
- `POST /restaurants/` - Create new restaurant
- `GET /restaurants/` - List all restaurants (with pagination)
- `GET /restaurants/{restaurant_id}` - Get specific restaurant
- `PUT /restaurants/{restaurant_id}` - Update restaurant
- `DELETE /restaurants/{restaurant_id}` - Delete restaurant
- `GET /restaurants/search?cuisine={cuisine_type}` - Search by cuisine
- `GET /restaurants/active` - List only active restaurants

### System
- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the server:
```bash
uvicorn main:app --reload
```

2. The API will be available at:
   - API: http://localhost:8000
   - Interactive Documentation: http://localhost:8000/docs
   - ReDoc Documentation: http://localhost:8000/redoc

## Example Usage

### Create a Restaurant
```bash
curl -X POST "http://localhost:8000/restaurants/" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Mario's Pizza",
       "description": "Authentic Italian pizza",
       "cuisine_type": "Italian",
       "address": "123 Main St, City, State",
       "phone_number": "+1-555-123-4567",
       "rating": 4.5,
       "opening_time": "11:00:00",
       "closing_time": "22:00:00"
     }'
```

### Get All Restaurants
```bash
curl -X GET "http://localhost:8000/restaurants/?skip=0&limit=10"
```

### Search by Cuisine
```bash
curl -X GET "http://localhost:8000/restaurants/search?cuisine=Italian&skip=0&limit=10"
```

### Get Active Restaurants Only
```bash
curl -X GET "http://localhost:8000/restaurants/active?skip=0&limit=10"
```

## Database

The application uses SQLite database (`restaurant.db`) with async SQLAlchemy. The database is automatically created when the application starts.

## Validation Rules

- Restaurant name: 3-100 characters, must be unique
- Phone number: 10-15 digits with optional formatting characters
- Rating: Must be between 0.0 and 5.0
- Opening/Closing time: Closing time must be after opening time
- Cuisine type: Required, 1-50 characters
- Address: Required, 5-255 characters

## Technical Stack

- **Framework**: FastAPI
- **Database**: SQLite with async SQLAlchemy
- **Validation**: Pydantic
- **ASGI Server**: Uvicorn
- **Python Version**: 3.7+

## Project Structure

```
zomato_v1/
├── main.py          # FastAPI application and configuration
├── database.py      # Database configuration and session management
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas for request/response validation
├── crud.py          # Database operations
├── routes.py        # API route definitions
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Future Enhancements (V2 & V3)

This is the foundation version. Future versions will include:
- User authentication and authorization
- Menu management for restaurants
- Order management system
- Delivery tracking
- Payment integration
- Reviews and ratings system
