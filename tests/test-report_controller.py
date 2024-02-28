import unittest
from unittest.mock import patch
from Controllers.ReportController import ReportController
from Models.Report import Report


class TestReportController(unittest.TestCase):

    @patch.object(Report, 'load_players')
    def test_players_alphabetical(self, mock_load_players):
        mock_load_players.return_value = [
            {'first_name': 'John', 'last_name': 'Doe'},
            {'first_name': 'Jane', 'last_name': 'Doe'}
        ]
        controller = ReportController()
        sorted_players = controller.players_alphabetical()
        self.assertEqual(sorted_players[0]['first_name'], 'Jane')
        self.assertEqual(sorted_players[1]['first_name'], 'John')

    @patch.object(Report, 'load_tournaments')
    def test_list_tournaments(self, mock_load_tournaments):
        mock_load_tournaments.return_value = [
            {'name': 'Tournament 1'},
            {'name': 'Tournament 2'}
        ]
        controller = ReportController()
        tournaments = controller.list_tournaments()
        self.assertEqual(len(tournaments), 2)
        self.assertEqual(tournaments[0]['name'], 'Tournament 1')

    @patch.object(Report, 'load_tournaments')
    @patch('builtins.input', return_value='1')
    def test_select_tournament_from_list(self, mock_input, mock_load_tournaments):
        mock_load_tournaments.return_value = [
            {'name': 'Tournament 1', 'id': 1},
            {'name': 'Tournament 2', 'id': 2}
        ]
        controller = ReportController()
        selected_tournament = controller.select_tournament_from_list()
        self.assertEqual(selected_tournament['name'], 'Tournament 1')


if __name__ == '__main__':
    unittest.main()
