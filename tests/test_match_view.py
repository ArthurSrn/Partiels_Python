import unittest
from unittest.mock import patch, MagicMock
from Views.MatchView import MatchView


class TestMatchView(unittest.TestCase):

    @patch('Views.MatchView.MatchView.get_user_choice', return_value=1)
    def test_display_match_results(self, mock_get_user_choice):
        match = MagicMock()
        match.player1 = {'first_name': 'John', 'last_name': 'Doe'}
        match.player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
        view = MatchView()

        choice = view.display_match_results(match, 1, 1)

        self.assertEqual(choice, 1)
        mock_get_user_choice.assert_called_once()


if __name__ == '__main__':
    unittest.main()
