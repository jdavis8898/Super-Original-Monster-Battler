#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Battle, Monster, Move, Battle_User, Monster_Move

fake = Faker()

def create_users():
    users = []

    for _ in range(15):
        u = User(
            name=fake.first_name(),
            computer=False
        )
        users.append(u)
    
    for _ in range(5):
        u = User(
            name=fake.first_name(),
            computer=True
        )
        users.append(u)

    return users

# def create_battles():
#     battles = []

#     for _ in range(10):
#         b = Battle(
#             user_turn=false
#             complete=true
#         )

def create_monsters():
    monsters = []

    m1 = Monster(
        name="FireDino",
        type="Fire",
        health=20
    )
    monsters.append(m1)

    m2 = Monster(
        name="WaterDevil",
        type="Water",
        health=20
    )
    monsters.append(m2)

    m3 = Monster(
        name="EarthyPlant",
        type="Leaf",
        health=20
    )
    monsters.append(m3)

    return monsters

def create_moves():
    moves = []

    m1 = Move(
        name="Fire Throw",
        type="Fire",
        damage = 4
    )
    moves.append(m1)

    m2 = Move(
        name="Water Throw",
        type="Water",
        damage = 4
    )
    moves.append(m2)
    
    m3 = Move(
        name="Leaf Throw",
        type="Leaf",
        damage = 4
    )
    moves.append(m3)

    return moves

def create_monster_moves():
    monster_moves = []

    mm1 = Monster_Move(
        monster_id=1,
        move_id=1
    )
    monster_moves.append(mm1)

    mm2 = Monster_Move(
        monster_id=2,
        move_id=2
    )
    monster_moves.append(mm2)

    mm3 = Monster_Move(
        monster_id=3,
        move_id=3
    )
    monster_moves.append(mm3)

    return monster_moves

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        print("Clearing db...")
        User.query.delete()
        Battle.query.delete()
        Monster.query.delete()
        Move.query.delete()
        # Battle_User.delete()
        Monster_Move.delete()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        # print("Seeding battles...")
        # battles = create_battles()
        # db.session.add_all(battles)
        # db.commit()

        print("Seeding monsters...")
        monsters = create_monsters()
        db.session.add_all(monsters)
        db.session.commit()

        print("Seeding moves...")
        moves = create_moves()
        db.session.add_all(moves)
        db.session.commit()

        print("Seeding monster_moves...")
        monster_moves = create_monster_moves()
        db.session.add_all(monster_moves)
        db.session.commit()