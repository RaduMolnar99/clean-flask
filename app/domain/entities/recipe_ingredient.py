import decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import mapped_column, Mapped

from app.domain.entities.base import Base


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    ingredient_id: Mapped[str] = mapped_column(ForeignKey("ingredients.id"), primary_key=True)
    recipe_id: Mapped[str] = mapped_column(ForeignKey("recipes.id"), primary_key=True)

    quantity: Mapped[decimal.Decimal] = mapped_column(Numeric(asdecimal=True))
