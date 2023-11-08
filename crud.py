from sqlalchemy.orm import Session
from models import Hero, Ability, AbilityType, Relationship,RelationshipType
from schemas import HeroModel


# def get_hero(db: Session, id: int):
#     heroes_querry = (
#         db.query(Hero)
#         .filter(Hero.id == id)
#         .first()
#     )
#     hero_models = list[heroes_querry.values()]
#     return hero_models

def get_heros_v1(db: Session):
    heroes_querry = (
        db.query(Hero)
        .all()
    )
    # hero_models = list[heroes_querry.values()]
    return heroes_querry


def get_heros(db: Session):
    heroes_querry = (
        db.query(Hero)
        .join(Hero.abilities)
        .all()
    )
    # hero_models = list[heroes_querry.values()]
    return heroes_querry