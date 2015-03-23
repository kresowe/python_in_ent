__author__ = 'michal'

import logging
#import logging.config


class Playground:
    """Playground on which crosses and circles are to be put"""
    fields = []
    playgroundSize = 3
    message = ''

    def __init__(self):
        self.fields = [[' ' for j in range(self.playgroundSize)] for i in range(self.playgroundSize)]

    def is_field_empty(self, row, col):
        """ checks, whether field of coords row, col is empty"""
        if self.fields[row][col] == ' ':
            return True
        else:
            return False

    def is_any_field_empty(self):
        """Checks, whether all the fields are empty."""
        for row in range(self.playgroundSize):
            for col in range(self.playgroundSize):
                if self.get_field(row, col) == ' ':
                    return True
        return False

    def put_on_field(self, row, col, player):
        """Put a sign (player arg) into field in row row and col column."""
        if row not in range(self.playgroundSize) or col not in range(self.playgroundSize):
            self.message = 'There is not such a field on playground!'
            print(self.message)
        elif self.is_field_empty(row, col):
            self.fields[row][col] = player
            self.show_playground()
        else:
            self.message = 'This field is not empty'
            print(self.message)
        self.print_log()


    def get_field(self, row, col):
        return self.fields[row][col]

    def show_playground(self):
        """Prints current situation on playground."""
        print('   | A | B | C | ')
        print('--------------')
        j = 1
        for row in range(self.playgroundSize):
            outp = ' ' + str(j) + ' | '
            for col in range(self.playgroundSize):
                outp += self.fields[row][col]
                outp += ' | '
            print(outp)
            print('--------------')
            j += 1
        print ''

    def print_log(self):
        logger = logging.getLogger(__name__)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s -- %(name)s -- %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.warning('Player\'s activity\n')

