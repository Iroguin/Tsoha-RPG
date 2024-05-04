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



def enemies():
    sql = """SELECT * FROM enemylist"""
    result = db.session.execute(text(sql))
    enemies = result.fetchall()
    return enemies

def characters():
    sql = """SELECT * FROM characterlist"""
    result = db.session.execute(text(sql))
    characters = result.fetchall()
    return characters