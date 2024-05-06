from db import db
from sqlalchemy.sql import text



def del_fight(name):
    sql = """
            TRUNCATE TABLE fightsenemies
            """
    db.session.execute(text(sql))
    db.session.commit()

def load_fight(name):
    sql = """
            SELECT el.*
            FROM fights f
            LEFT JOIN fightsenemies fe ON f.id = fe.fight_id
            LEFT JOIN enemylist el ON fe.enemylist_id = el.id
            WHERE f.name = :fight_name;
            """
    result = db.session.execute(text(sql), {"fight_name":name})
    fight = result.fetchall()
    return fight
    
def add_fight(name, difficulty):
    sql = """
            INSERT INTO 
            fights(name, difficulty) 
            VALUES (:name, :difficulty)
            ON CONFLICT DO NOTHING
            """
    db.session.execute(text(sql), {"name":name, "difficulty":difficulty})
    db.session.commit()

def add_fightenemy(fight_name, enemy_name):
    sql = """
            INSERT INTO fightsenemies (fight_id, enemylist_id)
            SELECT f.id, e.id
            FROM fights f
            INNER JOIN enemylist e ON f.name = :fight_name AND e.name = :enemy_name;
            """
    db.session.execute(text(sql), {"fight_name":fight_name, "enemy_name":enemy_name})
    db.session.commit()

def char_attack(char_name, enemy_name):
    sql = """
            UPDATE enemylist
            SET health = health - (
            SELECT attack
            FROM characterlist
            WHERE name = :char_name
            )
            WHERE name = :enemy_name;
            """
    db.session.execute(text(sql), {"enemy_name":enemy_name, "char_name":char_name})
    db.session.commit()

def enemy_attack(enemy_name, char_name):
    sql = """
            UPDATE characterlist
            SET health = health - (
            SELECT attack
            FROM enemylist
            WHERE name = :enemy_name
            )
            WHERE name = :char_name;
            """
    db.session.execute(text(sql), {"enemy_name":enemy_name, "char_name":char_name})
    db.session.commit()

def parse_attack_command(command):
    words = command.lower().split()  
    if len(words) < 3:
        return None  
    attacker = words[0]
    action = words[1]
    target = words[2]
    return (attacker, action, target)


