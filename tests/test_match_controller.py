
import unittest
from Models import Match
from Controllers.MatchController import MatchController


class TestMatchController(unittest.TestCase):

    def setUp(self):
        self.controller = MatchController()

    def test_create_match_pairs_even(self):
        players = ['Player1', 'Player2', 'Player3', 'Player4']
        expected = [('Player1', 'Player2'), ('Player3', 'Player4')]
        result = self.controller.create_match_pairs(players)
        self.assertEqual(result, expected)

    def test_create_match_pairs_odd(self):
        players = ['Player1', 'Player2', 'Player3']
        expected = [('Player1', 'Player2')]  # Avec un nombre impair, le dernier joueur ne sera pas apparié
        result = self.controller.create_match_pairs(players)
        self.assertEqual(result, expected)

    def test_create_matches(self):
        pairs = [('Player1', 'Player2'), ('Player3', 'Player4')]
        matches = self.controller.create_matches(pairs)
        self.assertEqual(len(matches), 2)
        self.assertTrue(all(isinstance(match, Match) for match in matches))

    def test_pair_players_no_previous_matches(self):
        players = [{'first_name': 'John', 'last_name': 'Doe'}, {'first_name': 'Jane', 'last_name': 'Doe'}]
        played_matches = []
        expected = [(players[0], players[1])]
        result = self.controller.pair_players(players, played_matches)
        self.assertEqual(result, expected)

    def test_has_played_together_false(self):
        player1 = {'first_name': 'John', 'last_name': 'Doe'}
        player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
        played_matches = []
        self.assertFalse(self.controller.has_played_together(player1, player2, played_matches))


if __name__ == '__main__':
    unittest.main()
