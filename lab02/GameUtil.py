__author__ = 'michal'

import re
import Player
import Playground

# Actually, this class has a functionality of Facade.
class GameUtil:

    pplayground = Playground.Playground()
    current_row = 0
    current_col = 1
    turn = Player.Player('', '')


    def print_on_start(self):
        print('Welcome to Tic-Tac-Toe game!')

    def print_game_result(self, player_a, player_b):
        """Prints final result: who is a winner or if it is a draw."""
        outp = ''
        result, winner = self.is_winner()
        if result:
            outp += 'The winner is: '
            if winner == player_a.get_pl_id():
                outp += player_a.get_name() + ' with: ' + player_a.get_pl_id()
            else:
                outp += player_b.get_name() + ' with: ' + player_b.get_pl_id()
        else:
            outp += 'There is a draw. Nobody has won.'
        return outp


    def create_player(self, player_id):
        """Creates player for game."""
        player_name = raw_input('Enter player\'s name for ' + str(player_id) +' : ')
        player = Player.Player(player_name, player_id)
        return player

    def is_winner(self):
        """
        Checks whether there is a winner
        :return: tuple(True if it is winner or False if it isn't, sign 'O' or 'X' of winner)
        """
        if (self.pplayground.get_field(0, 0) != ' ' and
                        (self.pplayground.get_field(0, 0) == self.pplayground.get_field(0, 1) == self.pplayground.get_field(0, 2) or
                        self.pplayground.get_field(0, 0) == self.pplayground.get_field(1, 0) == self.pplayground.get_field(2, 0) or
                        self.pplayground.get_field(0, 0) == self.pplayground.get_field(1, 1) == self.pplayground.get_field(2, 2))):
            return True, self.pplayground.get_field(0, 0)
        elif (self.pplayground.get_field(0, 1) != ' ' and
                          self.pplayground.get_field(0, 1) == self.pplayground.get_field(1, 1) == self.pplayground.get_field(2, 1)):
            return True, self.pplayground.get_field(0, 1)
        elif (self.pplayground.get_field(0, 2) != ' ' and
                        (self.pplayground.get_field(0, 2) == self.pplayground.get_field(1, 2) == self.pplayground.get_field(2, 2) or
                          self.pplayground.get_field(0, 2) == self.pplayground.get_field(1, 1) == self.pplayground.get_field(2, 0))):
            return True, self.pplayground.get_field(0, 2)
        elif (self.pplayground.get_field(1, 0) != ' ' and
                        self.pplayground.get_field(1, 0) == self.pplayground.get_field(1, 1) == self.pplayground.get_field(1, 2)):
            return True, self.pplayground.get_field(1, 0)
        elif (self.pplayground.get_field(2, 0) != ' ' and
                          self.pplayground.get_field(2, 0) == self.pplayground.get_field(2, 1) == self.pplayground.get_field(2, 2)):
            return True, self.pplayground.get_field(2, 0)
        else:
            return False, ''

    def get_playground(self):
        return self.pplayground

    def get_cur_row(self):
        return self.current_row

    def get_cur_col(self):
        return self.current_col

    def set_turn(self, pturn):
        self.turn = pturn
        print('It\'s ' + str(self.turn.get_name()) + '\'s turn.')

    def get_turn(self):
        return self.turn

    def get_player_turn(self):
        inp = raw_input('Enter field name (e.g. 1A):')
        return inp

    def parse_input(self, inp):
        """Parser for user input about which field he puts sign"""
        inp.upper()
        if re.search(r'^[1-3][ABC]$', inp):
            if inp[1] == 'A':
                self.current_col = 0
            elif inp[1] == 'B':
                self.current_col = 1
            elif inp[1] == 'C':
                self.current_col = 2
            self.current_row = int(inp[0]) - 1
            return True
        else:
            print('Invalid input.')
            return False
            
