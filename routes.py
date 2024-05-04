from app import app
from flask import Flask
from flask import render_template, request, redirect, session
import users
import entities as ent


print('routes run')

@app.route("/")
def index():
    return render_template("index.html")
    #return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        try:
            username = request.form["username"]  # Access form data using "username" key
            password = request.form["password"]
            if users.login(username, password):
                return redirect("/")
            else:
                return render_template("error.html", message="Väärä tunnus tai salasana")
        except KeyError:
            return render_template("error.html", message="Käyttäjätunnus tai salasana puuttuu")



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

@app.route("/fight")
def fight():
    ent.add_character("hero", 20, 5)
    ent.add_enemy("goblin", 10, 3)
    characters = ent.characters()
    enemies = ent.enemies()
    print(fight)
    return render_template('fight.html', enemies=enemies, characters=characters)

@app.route("/game")
def game():
    return render_template('game.html')
