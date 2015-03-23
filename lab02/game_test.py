__author__ = 'michal'

import unittest
import Playground
import GameUtil

class GameTest(unittest.TestCase):
    expected_values_field_empty = (([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 0, True),
                                   ([[' ', 'X', 'O'], [' ', 'X', ' '], [' ', ' ', ' ']], 0, 2, False),
                                   ([[' ', 'X', 'O'], [' ', 'X', ' '], [' ', ' ', ' ']], 0, 1, False),
                                   ([[' ', 'X', 'O'], [' ', 'X', ' '], [' ', ' ', ' ']], 1, 0, True),
                                   ([[' ', 'X', 'O'], [' ', 'X', ' '], [' ', ' ', ' ']], 1, 1, False))

    expected_values_any_field_empty = (([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], True),
                                       ([[' ', 'X', 'O'], [' ', 'X', ' '], [' ', ' ', ' ']], True),
                                       ([['O', 'X', 'O'], ['X', 'O', 'X'], ['X', 'O', 'O']], False))

    expected_values_is_winner = (([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], (False, '')),
                                       ([['O', 'O', 'O'], ['X', 'O', ' '], ['X', 'X', ' ']], (True, 'O')),
                                       ([['X', 'O', 'O'], ['O', 'O', 'X'], ['X', 'X', 'O']], (False, '')))

    def test_playground_field_empty(self):
        """Playground.is_field_empty() should give expected results for mentioned input"""
        for tup in self.expected_values_field_empty:
            test_playground = Playground.Playground()
            test_playground.fields = tup[0]
            result = test_playground.is_field_empty(tup[1], tup[2])
            self.assertEqual(tup[3], result)

    def test_playground_any_gield_empty(self):
        """Playground.is_any_field_empty() should give expected results for mentioned input"""
        for given_fields, expected in self.expected_values_any_field_empty:
            test_playground = Playground.Playground()
            test_playground.fields = given_fields
            result = test_playground.is_any_field_empty()
            self.assertEqual(expected, result)

    def test_game_util_is_winner(self):
        """GameUtil.is_winner() should give expected results for mentioned cases"""
        for given_playground, expected_result in self.expected_values_is_winner:
            test_game = GameUtil.GameUtil()
            test_game.get_playground().fields = given_playground
            result = test_game.is_winner()
            self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()