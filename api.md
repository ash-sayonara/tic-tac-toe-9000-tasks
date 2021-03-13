# API

### GET: /api/game_info?game_id=1&user_name=Petya&user_id=af056ec7-4f62-4a38-b860-076d5b5d7ea4&user_pass=greengolddog12346&token=9a5adaf4-9353-4d28-b1e7-f4c8753dea10

**response:**
```json
{
    "game_id": "1",
    "field": [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ],
    "sequence_of_turns": [],
    "first_player_name": "Petya",
    "second_player_name": "Vasya",
    "winner_id": ""
}
```
если не авторизован 401

### POST: /api/sign_up
**request:**
```json
{
  "user_name": "Petya",
  "user_pass": "greengolddog12346"
}
```

**response**
```json
{
  "user_name": "Petya",
  "user_id": "af056ec7-4f62-4a38-b860-076d5b5d7ea4",
  "user_pass": "greengolddog12346",
  "token": "9a5adaf4-9353-4d28-b1e7-f4c8753dea10"
}
```
если такое имя уже есть - ошибка 403 + объяснение(н: "message": "this username is already used")

### POST: /api/do_turn?game_id=1&user_name=Petya&user_id=af056ec7-4f62-4a38-b860-076d5b5d7ea4&user_pass=greengolddog12346&token=9a5adaf4-9353-4d28-b1e7-f4c8753dea10
**request:**
```json
{
  "player_name": "Petya",
  "x_coordinate": 0,
  "y_coordinate": 0
}
```
**response**
```json
{
    "game_id": "1",
    "field": [
        ["X", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ],
    "sequence_of_turns": [{
                "player_name":"Petya",
                "x_coordinate": 0,
                "y_coordinate": 0}],
    "first_player_name": "Petya",
    "second_player_name": "Vasya",
    "winner_id": ""
}
```

если такой игры нет - ошибка 404
если пользователь не авторизирован - ошибка 401
если игроку нельзя делать ход - ошибка 403 + объяснение(н: "message": "now it's not your turn", "message": "game over")