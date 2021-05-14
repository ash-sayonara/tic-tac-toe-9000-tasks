from dataclasses import dataclass
from flask import Flask, request, abort
from dataclasses_json import dataclass_json
from game_app import TicTacToeApp, TicTacToeGameNotFoundException, TicTacToeUserNotFoundException
from game_engine import TicTacToeTurn, TicTacToeGameInfo, UserInfo
from uuid import uuid4
from typing import List

app = Flask(__name__)
t_app = TicTacToeApp()

@app.route('/')
def hello_world():
    return str(t_app._games.keys())

@app.route('/game_info', methods=['GET'])
def get_game_info():
    game_id = request.args.get('game_id')
    if game_id:
        try:
            game_info = t_app.get_game_by_id(game_id).to_json()
        except TicTacToeGameNotFoundException:
            abort(404)
        return game_info
    abort(400)

@app.route('/start_game', methods=["POST"])
def start_game():
    user_id = request.args.get('user_id')
    user_pass = request.args.get('user_pass')
    user_secret = request.args.get('user_secret')
    user_id2 = request.args.get('user_id2')
    if user_id and user_pass and user_secret and user_id2:
        user = UserInfo(user_id = user_id, user_pass = user_pass, user_secret = user_secret)
        try: 
            x =  t_app.start_game(user, user_id2)
            return x.to_json()
        except TicTacToeUserNotFoundException:
            abort(404)
    abort(400)

@app.route('/turn', methods=["POST"])
def turn_post():
    turn = TicTacToeTurn.from_dict(request.json)
    game_id = request.args.get('game_id')
    user_id = request.args.get('user_id')
    user_pass = request.args.get('user_pass')
    user_secret = request.args.get('user_secret')
    if game_id and user_id and user_pass and user_secret and turn:
        user = UserInfo(user_id = user_id, user_pass = user_pass, user_secret = user_secret)
        if turn:
            try:
                game_info = t_app.do_turn(turn, game_id, user)
            except TicTacToeUserNotFoundException and TicTacToeGameNotFoundException:
                abort(404)
            return game_info.to_json()
    abort(400)

@app.route('/sign_up', methods=["POST"])
def registration():
    user_id = request.args.get('user_id')
    user_pass = request.args.get('user_pass')
    for i in t_app._users:
        if user_id == i.user_id:
            abort(400)
    user = UserInfo(user_id = user_id,user_pass = user_pass, user_secret = uuid4().hex)
    t_app._users.append(user)
    return user.to_json()

@app.route('/my_games', methods=["GET"])
def watch_games():
    user_id = request.args.get('user_id')
    user_pass = request.args.get('user_pass')
    user_secret = request.args.get('user_secret')
    if user_id and user_pass and user_secret:
        user = UserInfo(user_id = user_id,user_pass = user_pass,user_secret = user_secret)
        games = []
        if user in t_app._users:
            for i in t_app._games:
                if t_app.get_game_by_id(i).first_player_id == user_id or t_app.get_game_by_id(i).second_player_id == user_id:
                    games.append(i)
            return str(games)
    abort(404)
