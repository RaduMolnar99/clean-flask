import uuid

from sqlalchemy.orm import Mapped, mapped_column

from app.domain.entities.base import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid.uuid4())

    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
