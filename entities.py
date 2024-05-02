from db import db
from sqlalchemy.sql import text

def load_enemies():
    sql = """
            INSERT INTO 
            enemylist(name, health, attack) 
            VALUES ('goblin', '10', '3')
            """
    db.session.execute(text(sql))
    db.session.commit()

def load_characters():
    sql = """
            INSERT INTO 
            characterlist(name, health, attack) 
            VALUES ('hero', '20', '5')
            """
    db.session.execute(text(sql))
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