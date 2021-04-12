from dataclasses import dataclass
from flask import Flask, request, abort
from dataclasses_json import dataclass_json
from game_app import TicTacToeApp, TicTacToeGameNotFoundException
from game_engine import TicTacToeTurn

app = Flask(__name__)
t_app = TicTacToeApp()

@app.route('/')
def hello_world():
    return list(t_app._games.keys())[0]

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
    user_id1,user_pass1,user_secret1,user_id2 = request.args.get('users_info')
    if user_id1 and user_pass1 and user_secret1 and user_id2:
        try:
            t_app.start_game(user_id1, user_id2)
            return t_app._games[-1]
        except TicTacToeUserNotFoundException:
            abort(404) #?
    abort(400)

@app.route('/turn', methods=["POST"])
def turn_post():
    turn = TicTacToeTurn.from_dict(request.json)
    game_id,user_id,user_pass = request.args.get('game_id,user_id,user_pass,user_secret')
    if game_id and user_id and user_pass:
        user = UserInfo(user_id,user_pass,user_secret)
        if turn:
            try:
                t_app.do_turn(turn, game_id, user)
            except TicTacToeGameNotFoundException and TicTacToeUserNotFoundException:
                abort(404)
            return game_info
    abort(400)

@app.route('/regist', methods=["POST"])
def regist():
    user_id,user_pass = request.args.get('user_id,user_pass')
    if [(user_id in t_app._users)== True for i in t_app._users]:
        abort(400)
    user = UserInfo(user_id,user_pass,uuid4().hex)
    t_app._users.append(user)
    return user.to_dict

@app.route('/my_games', methods=["POST"])
def watch_games():
    user_id,user_pass, user_secret = request.args.get('user_info')
    user = UserInfo(user_id,user_pass,uuid4().hex)
    ret = []
    if user in t_app._users:
        for i in t_app._games:
            if i.first_player_id == user_id or i.second_player_id == user_id:
                ret.append(i)
        return ret
    abort(404)