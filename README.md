# Very Simple Role Playing Game

## Introduction

### Game Summary

The game is a turn based Role Playing Game (RPG) with a simple story. The player is in control of a party of heroes tasked with defeating a great evil. The game focuses on strategy and stats-based fighting mechanics. This is so the completed project makes sufficent use of SQL tables and the material the course teaches.

### Player Experience

The game is a strategy game where different actions (and in the future items) can be used by characters on every turn to fight and exploit the weaknesses of different enemy types. Stat sheets and calculating the benefits of different actions would be the decider of winning tough battles.

## State of Development

Stuff that works:

 - player characters
 - rudimentary fighting mechanics
 - registering and logging in

Stuff that doesn't work:

 - fighting doesn't have a win condition
 - "new game" and "continue" do the same thing currently

Next steps:

 - turn system
 - additional character actions
 - more robust fighting mechanics
 - improved site navigability

## Trying it Out

 - create virtual environment (venv)
 - install dependencies:
    ```
    pip install -r requirements.txt
    ```
 - install postgresql as instructed in the course material
 - create .env file with postgresql address:
   ```
   DATABASE_URL=postgresql:///<my db name>
   SECRET_KEY=<my secret key>
   ```
 - run the server:
    ```
    flask run [--debug]
    ```
 - enter the following URL in a browser: http://127.0.0.1:5000
 - follow the instructions to register an account and log in
 - start a new game by clicking on the "new game" link
 - try fighting the enemy goblins

## Appendix

The following are some earlier thoughts on the design of the game.

### Gameplay overview

The understanding of the underlying mechanics of the game and strategizing in fights is the main draw of the game. The game won't have much exploration and its design is to be mostly linear to keep the design simple. The player progresses through the game by fighting stronger and stronger enemies while gaining power before fighting the final boss.

### Primary mechanics

There is a main party of four characters with each having their own strengths, weaknesses and abilities. These will be represented in their stat sheets which can change depending on the equipment and items the characters are equipped with.

### Art

Though not implemented yet, the art style of the game will be simple pixel art, to emulate the games it is inspired by, and also because of the limited time available.

### UI

The UI is mostly text based. A command in the command box like "attack" opens options for attacks, and then selecting one of those executes it.
