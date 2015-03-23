__author__ = 'michal'

import GameUtil

# 'main' executable file

game = GameUtil.GameUtil()
game.print_on_start()
player1 = game.create_player('O')
player2 = game.create_player('X')

game.set_turn(player1)

first_turn = True
one_won = False
game_result = False, ''

while not one_won and game.get_playground().is_any_field_empty():
    if first_turn:
        pass
    else:
        if game.get_turn() == player1:
            game.set_turn(player2)
        else:
            game.set_turn(player1)

    first_turn = False

    game.get_playground().show_playground()
    inp = game.get_player_turn()
    while not game.parse_input(inp):
        inp = game.get_player_turn()

    game.get_playground().put_on_field(game.get_cur_row(), game.get_cur_col(), game.get_turn().get_pl_id())
    game_result = game.is_winner()
    one_won = game_result[0]

print(game.print_game_result(player1, player2))
