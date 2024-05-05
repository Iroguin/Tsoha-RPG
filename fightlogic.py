from db import db
from sqlalchemy.sql import text

def load_fight(name):
    sql = """
            SELECT name FROM fights
            WHERE name = :name
            """
    result = db.session.execute(text(sql), {"name":name})
    fight = result.fetchone()
    return fight
    
