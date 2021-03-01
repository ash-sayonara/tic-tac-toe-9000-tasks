from game_app import TicTacToeApp
from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn

def test_app():
    app = TicTacToeApp()
    assert app.start_game("Petya","Vasya") == TicTacToeGameInfo(
        game_id="1",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert app.get_game_by_id("1", "Petya") == TicTacToeGameInfo(
        game_id="1",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert app.get_game_by_id("1", "Vasya") == TicTacToeGameInfo(
        game_id="1",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )
    
    assert app.do_turn(TicTacToeTurn("Petya",-1,-1), "1") == TicTacToeGameInfo(
        game_id="1",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )
    
    assert app.do_turn(TicTacToeTurn("Vasya",0,0), "1") == TicTacToeGameInfo(
        game_id="1",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )
    
    assert app.do_turn(TicTacToeTurn("Vasya",0,0), "2") == None

    assert app.do_turn(TicTacToeTurn("Petya",0,0), "1") == TicTacToeGameInfo(
        game_id="1",
        field=[
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn(
                player_id="Petya",
                x_coordinate=0,
                y_coordinate=0
            )
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert app.get_game_by_id("1","Petya") == TicTacToeGameInfo(
        game_id="1",
        field=[
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn(
                player_id="Petya",
                x_coordinate=0,
                y_coordinate=0
            )
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert app.do_turn(TicTacToeTurn("Vasya",0,0), "1") == TicTacToeGameInfo(
        game_id="1",
        field=[
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn(
                player_id="Petya",
                x_coordinate=0,
                y_coordinate=0
            )
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    app.do_turn(TicTacToeTurn("Petya", 1, 0), "1")
    app.do_turn(TicTacToeTurn("Vasya", 1, 0), "1")
    app.do_turn(TicTacToeTurn("Petya", 0, 1), "1")
    app.do_turn(TicTacToeTurn("Vasya", 1, 1), "1")
    app.do_turn(TicTacToeTurn("Petya", 0, 2), "1")

    assert app.get_game_by_id("1","Petya") == TicTacToeGameInfo(
        game_id="1",
        field=[
            ["X", "X", "X"],
            ["O", "O", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn("Petya", 0, 0),
            TicTacToeTurn("Vasya", 1, 0),
            TicTacToeTurn("Petya", 0, 1),
            TicTacToeTurn("Vasya", 1, 1),
            TicTacToeTurn("Petya", 0, 2)
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id="Petya"
    )

    assert app.start_game("Petya","Sasha") == TicTacToeGameInfo(
        game_id="2",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Sasha",
        winner_id=""
    )

    assert app.get_game_by_id("1", "Sasha") == None

    assert app.get_game_by_id("2", "Sasha") == TicTacToeGameInfo(
        game_id="2",
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Sasha",
        winner_id=""
    )