import unittest
from unittest.mock import patch
from Views.PlayerView import PlayerView


class TestPlayerView(unittest.TestCase):

    @patch('Views.View.View.get_valid_alpha_input')
    @patch('Views.View.View.get_valid_date_input')
    @patch('builtins.input', side_effect=['AB12345', ''])
    def test_get_player_info(self, mock_input, mock_get_valid_date_input, mock_get_valid_alpha_input):
        mock_get_valid_alpha_input.side_effect = ['John', 'Doe']  # Prénom puis Nom
        mock_get_valid_date_input.return_value = '01/01/1980'  # Date de naissance

        view = PlayerView()
        result = view.get_player_info()

        self.assertEqual(result, ('John', 'Doe', '01/01/1980', 'AB12345'))
        mock_get_valid_alpha_input.assert_called()
        mock_get_valid_date_input.assert_called_once_with("Date de naissance (JJ/MM/AAAA): ")
        mock_input.assert_called_with("Identifiant national d'échecs (AB12345, optionnel) : ")


if __name__ == '__main__':
    unittest.main()
