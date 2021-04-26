"""Tic-tac-toe game library(for import)"""
from abc import ABC, abstractmethod
from typing import List, Callable
from dataclasses import dataclass

@dataclass
class TicTacToeTurn:
    """Information about player's turn(id, coordinates)"""
    player_id: str
    x_coordinate: int
    y_coordinate: int

@dataclass
class TicTacToeGameInfo:
    """Information about one game(id, fied, sequence of turns, players, winner)"""
    game_id: str
    field: List[List[str]]
    sequence_of_turns: List[TicTacToeTurn]
    first_player_id: str
    second_player_id: str
    winner_id: str # а какие могут быть варианты?

@dataclass
class UserInfo:
    """Information about user(id,password)"""
    user_id: str
    user_pass: str
    user_secret: str

class AbstractTicTacToeGame(ABC):
    """Abstract class of tic-tac-toe game(in the future we'll inherit from it)"""
    @abstractmethod
    def __init__(
            self,
            game_id: str,
            first_player_id: str,
            second_player_id: str,
            strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None
        ) -> None:
        """пока просто раскладываем по полям"""

    @abstractmethod
    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        """подумайте, когда использовать"""

    @abstractmethod
    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        """сначала проверяем корректность, для проверки используйте is_turn_correct,
        а возвращаем TicTacToeGameInfo"""

    @abstractmethod
    def get_game_info(self) -> TicTacToeGameInfo:
        """обычный геттер."""
