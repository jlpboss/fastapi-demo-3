from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

from database import Base

class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    about_me = Column(String)
    biography = Column(String)
    image_url = Column(String)
    
    abilities: Mapped[List["Ability"]] = relationship(back_populates="heroes", cascade="all, delete-orphan")
    
    # abilities: Mapped[List["Relationships"]] = relationship(
    #     back_populates="heroes", cascade="all, delete-orphan")

class Ability(Base):
    __tablename__ = "abilities"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ability_type_id: Mapped[int] = mapped_column(ForeignKey("ability_types.id"))
    hero_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"))

    heroes: Mapped["Hero"] = relationship(back_populates="abilities")

    def __repr__(self) -> str:
        return f"Ability(id={self.id!r}, ability_type_id={self.ability_type_id!r}, hero_id={self.hero_id!r})"

class Relationship(Base):
    __tablename__ = "relationships"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    hero1_id: Mapped[int] = mapped_column(ForeignKey("heros.id"))
    hero2_id: Mapped[int] = mapped_column(ForeignKey("heros.id"))
    relationship_type_id: Mapped[int] = mapped_column(ForeignKey("relationship_type.id"))

    # hero1: Mapped["Hero"] = relationship(back_populates="relationships")
    # hero2: Mapped["Hero"] = relationship(back_populates="relationships")

    def __repr__(self) -> str:
        return f"Relationship(id={self.id!r}, hero1_id={self.hero1_id!r}, hero2_id={self.hero2_id!r}, relationship_type_id={self.relationship_type_id!r})"

class AbilityType(Base):
    __tablename__ = "ability_type"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Relationship(id={self.id!r}, name={self.name!r})"

class RelationshipType(Base):
    __tablename__ = "relationship_type"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"relationship_type(id={self.id!r}, name={self.name!r})"

