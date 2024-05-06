from app import app
from flask import Flask
from flask import render_template, request, redirect, session
import users
import entities as ent
import fightlogic as fl



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]  # Access form data using "username" key
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


@app.route("/fight", methods=["GET", "POST"])
def fight():
    if request.method == "GET":
        print("fight")
        characters = ent.load_characters()
        enemies = fl.load_fight("first_fight")
        return render_template('fight.html', enemies=enemies, characters=characters)
    if request.method == "POST":
        characters = ent.load_characters()
        enemies = fl.load_fight("first_fight")
        action = request.form["action"]
        command = fl.parse_attack_command(action)
        fl.char_attack(command[0], command[2])
        return render_template('fight.html', enemies=enemies, characters=characters)

@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        fl.del_fight("first_fight")
        ent.new_characters()
        ent.add_enemy("goblin1", 10, 3)
        ent.add_enemy("goblin2", 10, 3)
        ent.add_enemy("goblin3", 10, 3)
        fl.add_fight("first_fight", 1)
        fl.add_fightenemy("first_fight", "goblin1")
        fl.add_fightenemy("first_fight", "goblin2")
        fl.add_fightenemy("first_fight", "goblin3")
        return render_template('game.html')
    if request.method == "POST":
        pass