import uuid

from sqlalchemy.orm import mapped_column, Mapped

from app.domain.entities.base import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid.uuid4())

    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    is_published: Mapped[bool] = mapped_column(default=False)
