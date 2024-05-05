from db import db
from sqlalchemy.sql import text

def add_enemy(name, health, attack):
    sql = """
            INSERT INTO 
            enemylist(name, health, attack) 
            VALUES (:name, :health, :attack)
            """
    db.session.execute(text(sql), {"name":name, "health":health, "attack":attack})
    db.session.commit()

def add_character(name, health, attack):
    sql = """
            INSERT INTO 
            characterlist(name, health, attack) 
            VALUES (:name, :health, :attack)
            """
    db.session.execute(text(sql), {"name":name, "health":health, "attack":attack})
    db.session.commit()

def new_characters():
    sql = """
            TRUNCATE TABLE characters
            """
    db.session.execute(text(sql))
    db.session.commit()
    add_character("hero", 20, 5)
    add_character("healer", 15, 2)
    add_character("mage", 15, 6)
    add_character("defender", 30, 3)


def load_enemies():
    sql = """SELECT name, health, attack FROM enemylist"""
    result = db.session.execute(text(sql))
    enemies = result.fetchall()
    return enemies

def load_characters():
    sql = """SELECT name, health, attack FROM characterlist"""
    result = db.session.execute(text(sql))
    characters = result.fetchall()
    return characters