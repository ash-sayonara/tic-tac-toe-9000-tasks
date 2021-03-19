"""This is a body of the app"""
from typing import Dict
from uuid import uuid4
from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn

class TicTacToeGameNotFoundException(Exception):
    """game not found :)"""

class TicTacToeApp:
    """The class is used for making different games between two players
    Attributes
    ----------
    games: Dict(str, TicTacToeGame) <- a dictionary, where we are saving all games"""
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        """The function to add new game to the dictionary of games"""
        game_id = uuid4().hex
        game = TicTacToeGame(game_id, first_player_id, second_player_id)
        self._games[game_id] = game
        return game.get_game_info()

    def get_game_by_id(self, game_id: str) -> TicTacToeGameInfo:
        """The function for getting geme bi id"""
        game = self._games.get(game_id)
        if game:
            return game.get_game_info()
        raise TicTacToeGameNotFoundException(f"no game with id={game_id}")

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        """The function for doing turn"""
        game = self._games.get(game_id)
        if game:
            return game.do_turn(turn)
        raise TicTacToeGameNotFoundException(f"no game with id={game_id}")
