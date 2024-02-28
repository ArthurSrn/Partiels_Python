import unittest
from unittest.mock import patch
from Controllers.PlayerController import PlayerController
from Views.PlayerView import PlayerView


class TestPlayerController(unittest.TestCase):

    @patch.object(PlayerView, 'get_player_info')
    @patch('Models.Player.Player.save_player')
    def test_add_player(self, mock_save_player, mock_get_player_info):
        mock_get_player_info.return_value = ('John', 'Doe', '01/01/1980', '123456')

        controller = PlayerController()
        controller.add_player()

        self.assertIsNotNone(controller.player)
        self.assertEqual(controller.first_name, 'John')
        self.assertEqual(controller.last_name, 'Doe')
        self.assertEqual(controller.birth_date, '01/01/1980')
        self.assertEqual(controller.national_chess_id, '123456')
        mock_save_player.assert_called_once()


if __name__ == '__main__':
    unittest.main()
