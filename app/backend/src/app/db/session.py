from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


data_engine = create_async_engine(settings.database_url, future=True, echo=False)
async_session = sessionmaker(
    bind=data_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
