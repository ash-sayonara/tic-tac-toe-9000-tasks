from dataclasses import dataclass
from flask import Flask, request, abort
from dataclasses_json import dataclass_json
from game_app import TicTacToeApp, TicTacToeGameNotFoundException
from game_engine import TicTacToeTurn
from uuid import uuid4
from typing import List

app = Flask(__name__)
t_app = TicTacToeApp()

@dataclass_json
@dataclass
class UserInfo:
    user_id: str
    user_pass: str
    user_secret: str

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

@app.route('/start', methods=["POST"])
def start_game():
    user_id = request.args.get('user_id')
    user_pass = request.args.get('user_pass')
    user_secret = request.args.get('user_secret')
    user_id2 = request.args.get('user_id2')
    if user_id and user_pass and user_secret and user_id2:
        user = UserInfo(user_id,user_pass, user_secret)
        if user in t_app._users:
            try:
                t_app.start_game(user_id1, user_id2)
                return t_app._games[-1]
            except TicTacToeUserNotFoundException:
                abort(404) #?
    abort(400)

@app.route('/turn', methods=["POST"])
def turn_post():
    turn = TicTacToeTurn.from_dict(request.json)
    game_id = request.args.get('game_id')
    user_id = request.args.get('user_id')
    user_pass = request.args.get('user_pass')
    user_secret = request.args.get('user_secret')
    if game_id and user_id and user_pass:
        user = UserInfo(user_id,user_pass, user_secret)
        if turn:
            if user in t_app._users:
                try:
                    t_app.do_turn(turn, game_id, user)
                except TicTacToeGameNotFoundException and TicTacToeUserNotFoundException:
                    abort(404)
                return game_info
    abort(400)

@app.route('/regist', methods=["POST"])
def regist():
    user_id = request.args.get('user_id')
    user_pass = request.args.get('user_pass')
    if [(user_id in t_app._users)== True for i in t_app._users]:
        abort(400)
    user = UserInfo(user_id = user_id,user_pass = user_pass, user_secret = uuid4().hex)
    t_app._users.append(user)
    return user.to_json()

@app.route('/my_games', methods=["GET"])
def watch_games():
    user_id = request.args.get('user_id')
    user_pass = request.args.get('user_pass')
    user_secret = request.args.get('user_secret')
    user = UserInfo(user_id = user_id,user_pass = user_pass,user_secret = uuid4().hex)
    ret = []
    if user in t_app._users:
        for i in t_app._games:
            if i.first_player_id == user_id or i.second_player_id == user_id:
                ret.append(i)
        return ret
    abort(404)