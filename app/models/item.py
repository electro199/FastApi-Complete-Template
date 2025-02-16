import datetime
from typing import List

from sqlalchemy import DateTime, String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Item(Base):
    __tablename__ = "Item"

    id: Mapped[int] = mapped_column(BigInteger,index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.utcnow
    )

    user: Mapped["User"] = relationship(back_populates="user") # Example Item
    owner_id: Mapped[str] = mapped_column(ForeignKey(column="User.id"))

