from fastapi import APIRouter, Depends, HTTPException, status, Query
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import crud
from schemas import RestaurantCreate, RestaurantOut, RestaurantUpdate

from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@router.post("/", response_model=RestaurantOut, status_code=status.HTTP_201_CREATED)
async def create_restaurant_endpoint(restaurant_in: RestaurantCreate, db: AsyncSession = Depends(get_db)):
    try:
        new = await crud.create_restaurant(db, restaurant_in)
        return new
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Restaurant with same name or phone already exists.")


@router.get("/", response_model=List[RestaurantOut])
async def list_restaurants_endpoint(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: AsyncSession = Depends(get_db)):
    rows = await crud.list_restaurants(db, skip=skip, limit=limit)
    return rows


@router.get("/active", response_model=List[RestaurantOut])
async def list_active_endpoint(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: AsyncSession = Depends(get_db)):
    rows = await crud.list_active_restaurants(db, skip=skip, limit=limit)
    return rows


@router.get("/search", response_model=List[RestaurantOut])
async def search_cuisine_endpoint(cuisine: str = Query(..., min_length=1), skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: AsyncSession = Depends(get_db)):
    rows = await crud.search_by_cuisine(db, cuisine=cuisine, skip=skip, limit=limit)
    return rows


@router.get("/{restaurant_id}", response_model=RestaurantOut)
async def get_restaurant_endpoint(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    r = await crud.get_restaurant(db, restaurant_id)
    if not r:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    return r


@router.put("/{restaurant_id}", response_model=RestaurantOut)
async def update_restaurant_endpoint(restaurant_id: int, updates: RestaurantUpdate, db: AsyncSession = Depends(get_db)):
    try:
        r = await crud.update_restaurant(db, restaurant_id, updates)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Update would violate unique constraint (name/phone).")
    if not r:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    return r


@router.delete("/{restaurant_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_restaurant_endpoint(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    ok = await crud.delete_restaurant(db, restaurant_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    return None

