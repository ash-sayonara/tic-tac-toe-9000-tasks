"logic of the game"
from copy import deepcopy
from typing import Callable, List
from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):
    """The class is used for making a game between two players
    Attributes
    ----------
    game_id: str
    first_player_id: srt
    second_player_id: str
    winner_id: str
    strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn]
        function with strategy of tic-tac-toe game
    turns = list
        the list of sequence of turns
        """
    def __init__(
        self,
        game_id: str,
        first_player_id: str,
        second_player_id: str,
        strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None
    ) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__strategy = strategy
        self.__turns = [] # type: List[TicTacToeTurn]
    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        """The function for cheaking the turn's correctness"""
        if self.__winner_id != "":
            return False
        if not (0<=turn.x_coordinate<=2 and 0<=turn.y_coordinate<=2):
            return False
        if self.carrent_player_id() != turn.player_id:
            return False
        field = self.get_game_info().field
        if field[turn.x_coordinate][turn.y_coordinate] != " ":
            return False
        return True
    def carrent_player_id(self) -> str:
        """The function for knowing player's id"""
        if len(self.__turns)%2==0:
            return self.__first_player_id
        return self.__second_player_id
    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        """The function for doing a turn"""
        if not self.is_turn_correct(turn):
            return self.get_game_info()
        self.__turns.append(deepcopy(turn))
        self.set_winner()
        return self.get_game_info()
    def set_winner(self) -> None:
        """The function for cheacking the winner"""
        field = self.get_game_info().field
        draw = True
        for i in range(3):
            row1 = ""
            row2 = ""
            for j in range(3):
                row1 += field[i][j]
                row2 += field[j][i]
            if row1 == "X"*3 or row2 == "X"*3:
                self.__winner_id = self.__first_player_id
                return
            if row1 == "O"*3 or row2 == "O"*3:
                self.__winner_id = self.__second_player_id
                return
            if "X" not in row1 or "X" not in row2 or "O" not in row1 or "O" not in row2:
                draw = False
        row1 = ""
        row2 = ""
        for i in range(3):
            row1 += field[i][i]
            row2 += field[i][2-i]
            if row1 == "X"*3 or row2 == "X"*3:
                self.__winner_id = self.__first_player_id
                return
            if row1 == "O"*3 or row2 == "O"*3:
                self.__winner_id = self.__second_player_id
                return
        if "X" not in row1 or "X" not in row2 or "O" not in row1 or "O" not in row2:
            draw = False
        if draw:
            self.__winner_id = "draw"
    def get_game_info(self) -> TicTacToeGameInfo:
        """The function for taking information about the game"""
        result = TicTacToeGameInfo(
            game_id=self.__game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self.__turns),
            first_player_id=self.__first_player_id,
            second_player_id=self.__second_player_id,
            winner_id=self.__winner_id
        )
        for turn in self.__turns:
            if turn.player_id == self.__first_player_id:
                result.field[turn.x_coordinate][turn.y_coordinate] = "X"
            else:
                result.field[turn.x_coordinate][turn.y_coordinate] = "O"
        return result

        