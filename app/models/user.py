import datetime
import email
from typing import List

from sqlalchemy import DateTime, String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = "User"

    id: Mapped[UUID] = mapped_column(UUID,index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    profile_picture: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.utcnow
    )

    items: Mapped[List["Item"]] = relationship(back_populates="user") # Example Item

