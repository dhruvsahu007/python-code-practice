from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from models import Restaurant
from typing import List, Optional
from schemas import RestaurantCreate, RestaurantUpdate


async def create_restaurant(db: AsyncSession, restaurant_in: RestaurantCreate) -> Restaurant:
    new = Restaurant(**restaurant_in.dict())
    db.add(new)
    try:
        await db.commit()
        await db.refresh(new)
        return new
    except IntegrityError as e:
        await db.rollback()
        raise


async def get_restaurant(db: AsyncSession, restaurant_id: int) -> Optional[Restaurant]:
    q = await db.execute(select(Restaurant).where(Restaurant.id == restaurant_id))
    result = q.scalars().first()
    return result


async def list_restaurants(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[Restaurant]:
    q = await db.execute(select(Restaurant).offset(skip).limit(limit).order_by(Restaurant.id))
    return q.scalars().all()


async def update_restaurant(db: AsyncSession, restaurant_id: int, updates: RestaurantUpdate) -> Optional[Restaurant]:
    existing = await get_restaurant(db, restaurant_id)
    if not existing:
        return None

    for k, v in updates.dict(exclude_unset=True).items():
        setattr(existing, k, v)
    try:
        db.add(existing)
        await db.commit()
        await db.refresh(existing)
        return existing
    except IntegrityError:
        await db.rollback()
        raise


async def delete_restaurant(db: AsyncSession, restaurant_id: int) -> bool:
    existing = await get_restaurant(db, restaurant_id)
    if not existing:
        return False
    await db.delete(existing)
    await db.commit()
    return True


async def search_by_cuisine(db: AsyncSession, cuisine: str, skip: int = 0, limit: int = 10):
    q = await db.execute(
        select(Restaurant)
        .where(Restaurant.cuisine_type.ilike(f"%{cuisine}%"))
        .offset(skip)
        .limit(limit)
    )
    return q.scalars().all()


async def list_active_restaurants(db: AsyncSession, skip: int = 0, limit: int = 10):
    q = await db.execute(
        select(Restaurant).where(Restaurant.is_active == True).offset(skip).limit(limit)
    )
    return q.scalars().all()

