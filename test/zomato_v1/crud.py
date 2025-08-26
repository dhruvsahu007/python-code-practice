from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_, or_, func
from models import Restaurant
from schemas import RestaurantCreate, RestaurantUpdate
from typing import Optional, List

class RestaurantCRUD:
    
    async def create_restaurant(self, db: AsyncSession, restaurant: RestaurantCreate) -> Restaurant:
        """Create a new restaurant"""
        db_restaurant = Restaurant(**restaurant.dict())
        db.add(db_restaurant)
        await db.commit()
        await db.refresh(db_restaurant)
        return db_restaurant
    
    async def get_restaurant(self, db: AsyncSession, restaurant_id: int) -> Optional[Restaurant]:
        """Get a restaurant by ID"""
        result = await db.execute(select(Restaurant).filter(Restaurant.id == restaurant_id))
        return result.scalar_one_or_none()
    
    async def get_restaurant_by_name(self, db: AsyncSession, name: str) -> Optional[Restaurant]:
        """Get a restaurant by name"""
        result = await db.execute(select(Restaurant).filter(Restaurant.name == name))
        return result.scalar_one_or_none()
    
    async def get_restaurants(
        self, 
        db: AsyncSession, 
        skip: int = 0, 
        limit: int = 100,
        cuisine_type: Optional[str] = None,
        active_only: bool = False
    ) -> tuple[List[Restaurant], int]:
        """Get restaurants with optional filtering"""
        query = select(Restaurant)
        count_query = select(func.count(Restaurant.id))
        
        # Apply filters
        filters = []
        if cuisine_type:
            filters.append(Restaurant.cuisine_type.ilike(f"%{cuisine_type}%"))
        if active_only:
            filters.append(Restaurant.is_active == True)
        
        if filters:
            query = query.filter(and_(*filters))
            count_query = count_query.filter(and_(*filters))
        
        # Get total count
        count_result = await db.execute(count_query)
        total = count_result.scalar()
        
        # Get restaurants with pagination
        query = query.offset(skip).limit(limit).order_by(Restaurant.id)
        result = await db.execute(query)
        restaurants = result.scalars().all()
        
        return restaurants, total
    
    async def search_restaurants_by_cuisine(
        self, 
        db: AsyncSession, 
        cuisine_type: str,
        skip: int = 0,
        limit: int = 100
    ) -> tuple[List[Restaurant], int]:
        """Search restaurants by cuisine type"""
        return await self.get_restaurants(
            db, 
            skip=skip, 
            limit=limit, 
            cuisine_type=cuisine_type
        )
    
    async def get_active_restaurants(
        self, 
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100
    ) -> tuple[List[Restaurant], int]:
        """Get only active restaurants"""
        return await self.get_restaurants(
            db,
            skip=skip,
            limit=limit,
            active_only=True
        )
    
    async def update_restaurant(
        self, 
        db: AsyncSession, 
        restaurant_id: int, 
        restaurant_update: RestaurantUpdate
    ) -> Optional[Restaurant]:
        """Update a restaurant"""
        db_restaurant = await self.get_restaurant(db, restaurant_id)
        if not db_restaurant:
            return None
        
        update_data = restaurant_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_restaurant, field, value)
        
        await db.commit()
        await db.refresh(db_restaurant)
        return db_restaurant
    
    async def delete_restaurant(self, db: AsyncSession, restaurant_id: int) -> bool:
        """Delete a restaurant"""
        db_restaurant = await self.get_restaurant(db, restaurant_id)
        if not db_restaurant:
            return False
        
        await db.delete(db_restaurant)
        await db.commit()
        return True

# Create instance
restaurant_crud = RestaurantCRUD()
