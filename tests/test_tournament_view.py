import unittest
from unittest.mock import patch
from Views.TournamentView import TournamentView


class TestTournamentView(unittest.TestCase):

    @patch('Views.View.View.get_valid_alpha_input')
    @patch('Views.View.View.get_valid_date_input')
    @patch('Views.View.View.get_valid_int_input')
    @patch('builtins.input', side_effect=['Description du tournoi'])
    def test_tournament_info(self, mock_input, mock_get_int, mock_get_date_input, mock_get_valid):
        mock_get_valid.side_effect = ['Tournoi Test', 'Paris']
        mock_get_date_input.side_effect = ['01/01/2023', '05/01/2023']
        mock_get_int.return_value = 4

        view = TournamentView()
        result = view.get_tournament_info()

        self.assertEqual(result, ('Tournoi', 'Paris', '01/01/2023', '05/01/2023', 4, 'Description'))
        mock_get_valid.assert_any_call("Nom du tournoi: ")
        mock_get_valid.assert_any_call("Lieu: ")
        mock_get_date_input.assert_any_call("Date de début (JJ/MM/AAAA): ")
        mock_get_date_input.assert_any_call("Date de fin (JJ/MM/AAAA): ")
        mock_get_int.assert_called_once_with("Nombre de tours (optionnel, défaut à 4): ", 4)
        mock_input.assert_called_once_with("Description du tournoi (optionnel): ")


if __name__ == '__main__':
    unittest.main()
