from dataclasses import dataclass
from flask import Flask, request, abort
from dataclasses_json import dataclass_json
from game_app import TicTacToeApp, TicTacToeGameNotFoundException
from game_engine import TicTacToeTurn

app = Flask(__name__)
t_app = TicTacToeApp()
t_app.start_game('1', '2')

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

@app.route('/turn', methods=["POST"])
def turn_post():
    turn = TicTacToeTurn.from_dict(request.json)
    game_id,user_id,user_pass = request.args.get('game_id,user_id,user_pass,user_secret')
    if game_id and user_id and user_pass:
        user = UserInfo(user_id,user_pass,user_secret)
        if turn:
            try:
                t_app.do_turn(turn, game_id, user)
            except TicTacToeGameNotFoundException:
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