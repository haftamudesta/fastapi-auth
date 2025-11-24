from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Text, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase,relationship
from datetime import datetime, timezone
from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTableUUID
DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
from fastapi import Depends

class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTableUUID, Base):
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = "posts"
    id=Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    caption = Column(Text)
    url = Column(String,nullable=False)
    file_type = Column(String,nullable=False)
    file_name = Column(String,nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    user = relationship("User", back_populates="posts")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker=async_sessionmaker(engine,expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def get_async_session()->AsyncGenerator[AsyncSession,None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)