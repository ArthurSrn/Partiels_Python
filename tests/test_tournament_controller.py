import unittest
from unittest.mock import patch
from Controllers.TournamentController import TournamentController


class TestTournamentController(unittest.TestCase):

    @patch('Models.Tournament.Tournament.save_tournament')
    @patch('Views.TournamentView.TournamentView.get_tournament_info')
    def test_create_tournament(self, mock_get_info, mock_save_tournament):
        mock_get_info.return_value = ('Open Paris', 'Paris', '2023-01-01', '2023-01-05', 5, 'Description')

        controller = TournamentController()
        controller.create_tournament()

        self.assertEqual(controller.tournament.name, 'Open Paris')
        self.assertEqual(controller.tournament.location, 'Paris')
        self.assertEqual(controller.tournament.start_date, '2023-01-01')
        self.assertEqual(controller.tournament.end_date, '2023-01-05')
        mock_save_tournament.assert_called_once()


if __name__ == '__main__':
    unittest.main()
