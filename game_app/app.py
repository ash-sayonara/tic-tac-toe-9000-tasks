"""This is a body of the app"""
from typing import Dict
from typing import Optional
from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn

class TicTacToeApp():
    """The class is used for making different games between two players
    Attributes
    ----------
    games: Dict(str, TicTacToeGame) <- a dictionary, where we are saving all games"""
    def __init__(self):
        self.__games: Dict(str, TicTacToeGame) = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        """The function to add new game to the dictionary of games"""    
        game_id = str(len(self.__games)+1)
        game = TicTacToeGame(
            game_id=game_id,
            first_player_id=first_player_id,
            second_player_id=second_player_id
        )
        self.__games[game_id] = game
        return game.get_game_info()

    def get_game_by_id(self, game_id: str) -> Optional[TicTacToeGameInfo]:
        """The function for getting geme bi id"""
        if self.__games.get(game_id):
            return self.__games[game_id].get_game_info()
        return None

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> Optional[TicTacToeGameInfo]:
        """The function for doing turn"""
        if game_id in self.__games:
            self.__games[game_id].do_turn(turn)
            return self.__games[game_id].get_game_info()
        return None
