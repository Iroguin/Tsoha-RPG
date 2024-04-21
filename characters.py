from db import db
from sqlalchemy.sql import text

def enemies():
    sql = text("SELECT * FROM enemylist")
    enemies = db.execute(sql)
    return enemies

def characters():
    sql = text("SELECT * FROM characterlist")
    characters = db.execute(sql)
    return characters