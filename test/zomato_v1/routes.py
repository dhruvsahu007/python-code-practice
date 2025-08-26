from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from database import get_database
from schemas import RestaurantCreate, RestaurantUpdate, RestaurantResponse, RestaurantList
from crud import restaurant_crud
from typing import Optional

router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"]
)

@router.post("/", response_model=RestaurantResponse, status_code=201)
async def create_restaurant(
    restaurant: RestaurantCreate,
    db: AsyncSession = Depends(get_database)
):
    """Create a new restaurant"""
    try:
        # Check if restaurant with same name already exists
        existing_restaurant = await restaurant_crud.get_restaurant_by_name(db, restaurant.name)
        if existing_restaurant:
            raise HTTPException(
                status_code=400, 
                detail="Restaurant with this name already exists"
            )
        
        db_restaurant = await restaurant_crud.create_restaurant(db, restaurant)
        return db_restaurant
    except IntegrityError:
        raise HTTPException(
            status_code=400, 
            detail="Restaurant with this name already exists"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=RestaurantList)
async def list_restaurants(
    skip: int = Query(0, ge=0, description="Number of restaurants to skip"),
    limit: int = Query(100, ge=1, le=100, description="Number of restaurants to return"),
    db: AsyncSession = Depends(get_database)
):
    """List all restaurants with pagination"""
    restaurants, total = await restaurant_crud.get_restaurants(db, skip=skip, limit=limit)
    return RestaurantList(
        restaurants=restaurants,
        total=total,
        skip=skip,
        limit=limit
    )

@router.get("/active", response_model=RestaurantList)
async def list_active_restaurants(
    skip: int = Query(0, ge=0, description="Number of restaurants to skip"),
    limit: int = Query(100, ge=1, le=100, description="Number of restaurants to return"),
    db: AsyncSession = Depends(get_database)
):
    """List only active restaurants"""
    restaurants, total = await restaurant_crud.get_active_restaurants(db, skip=skip, limit=limit)
    return RestaurantList(
        restaurants=restaurants,
        total=total,
        skip=skip,
        limit=limit
    )

@router.get("/search", response_model=RestaurantList)
async def search_restaurants_by_cuisine(
    cuisine: str = Query(..., description="Cuisine type to search for"),
    skip: int = Query(0, ge=0, description="Number of restaurants to skip"),
    limit: int = Query(100, ge=1, le=100, description="Number of restaurants to return"),
    db: AsyncSession = Depends(get_database)
):
    """Search restaurants by cuisine type"""
    restaurants, total = await restaurant_crud.search_restaurants_by_cuisine(
        db, cuisine_type=cuisine, skip=skip, limit=limit
    )
    return RestaurantList(
        restaurants=restaurants,
        total=total,
        skip=skip,
        limit=limit
    )

@router.get("/{restaurant_id}", response_model=RestaurantResponse)
async def get_restaurant(
    restaurant_id: int,
    db: AsyncSession = Depends(get_database)
):
    """Get a specific restaurant by ID"""
    restaurant = await restaurant_crud.get_restaurant(db, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

@router.put("/{restaurant_id}", response_model=RestaurantResponse)
async def update_restaurant(
    restaurant_id: int,
    restaurant_update: RestaurantUpdate,
    db: AsyncSession = Depends(get_database)
):
    """Update a restaurant"""
    try:
        # If name is being updated, check for duplicates
        if restaurant_update.name:
            existing_restaurant = await restaurant_crud.get_restaurant_by_name(db, restaurant_update.name)
            if existing_restaurant and existing_restaurant.id != restaurant_id:
                raise HTTPException(
                    status_code=400, 
                    detail="Restaurant with this name already exists"
                )
        
        updated_restaurant = await restaurant_crud.update_restaurant(db, restaurant_id, restaurant_update)
        if not updated_restaurant:
            raise HTTPException(status_code=404, detail="Restaurant not found")
        return updated_restaurant
    except IntegrityError:
        raise HTTPException(
            status_code=400, 
            detail="Restaurant with this name already exists"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{restaurant_id}", status_code=204)
async def delete_restaurant(
    restaurant_id: int,
    db: AsyncSession = Depends(get_database)
):
    """Delete a restaurant"""
    success = await restaurant_crud.delete_restaurant(db, restaurant_id)
    if not success:
        raise HTTPException(status_code=404, detail="Restaurant not found")
