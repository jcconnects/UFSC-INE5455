import unittest
from src.src import PuzzleGame
from src.src.invalid_position_exception import InvalidPositionException
from unittest.mock import patch, Mock
from puzzle_game_with_mock import PuzzleGameWithPlayer

# PARTE 1
#
# Para o projeto PuzzleGame:
# 1. Analise os testes sem e com mock do método get_tile da
# classe Board apresentados a seguir.
# 2. Faça dois testes sem mock para o método get_tile da
# classe PuzzleGame.
# 3. Faça os mesmos dois testes com mocks para o método
# get_tile da classe PuzzleGame.


# ==========================================================================
# PARTE 1
# ==========================================================================

class TestPuzzleGameGetTile(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(3)
        return super().setUp()

    def test_get_existing_tile(self):
        tile = self.puzzle_game.get_tile(1,1)

        self.assertEqual(tile, 1)

    def test_get_empty_position(self):
        tile = self.puzzle_game.get_tile(3,3)

        self.assertEqual(tile, " ")

    @patch('src.src.puzzle_game.PuzzleGame.get_tile')
    def test_get_existing_tile_with_mock(self, mock_puzzle_game_get_tile):
        mock_puzzle_game_get_tile.return_value = "foo"
        tile = self.puzzle_game.get_tile(1,1)

        self.assertEqual(tile, "foo")

    @patch('src.src.puzzle_game.PuzzleGame.get_tile')
    def test_get_empty_position_with_mock(self, mock_puzzle_game_get_tile):
        mock_puzzle_game_get_tile.return_value = "bar"
        tile = self.puzzle_game.get_tile(3,3)

        self.assertEqual(tile, "bar")


# PARTE 2
#
# Para o projeto PuzzleGame:
# 1. Inclua o arquivo puzzle_game_with_mock.py no projeto.
# Este arquivo tem a classe PuzzleGameWithPlayer que é
# subclasse de PuzzleGame.
# 2. Faça dois testes sem mock envolvendo o método
# end_of_the_game da classe PuzzleGameWithPlayer.
# 3. Faça os mesmos dois testes envolvendo o método
# end_of_the_game da classe PuzzleGameWithPlayer
# utilizando mock para o método save_game_to_file.
# Obs: o método com ”mockeado” é o save_game_to_file e não o método
# end_of_the_game.

# ==========================================================================
# PARTE 2
# ==========================================================================
class TestPuzzleGameWithPlayerEndOfGame(unittest.TestCase):
    def setUp(self):
        self.game = PuzzleGameWithPlayer(3, "test_player")
        return super().setUp()

    def test_end_of_game_when_finished(self):
        # Board começa no estado final
        result = self.game.end_of_the_game()

        self.assertEqual(result, "Saved")

    # def test_end_of_game_when_not_finished(self):
    #     # Move um tile para retirar o board do estado final
    #     self.game.move_tile_from_a_position_to_the_empty_position(3, 2)
    #     result = self.game.end_of_the_game()
    #
    #     self.assertEqual(result, "Game not finished")

    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_game_when_finished_with_mock(self, mock_save):
        mock_save.return_value = "Saved"
        result = self.game.end_of_the_game()

        # mock_save.assert_called_once()
        self.assertEqual(result, "Saved")

    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_game_when_not_finished_with_mock(self, mock_save):
        self.game.move_tile_from_a_position_to_the_empty_position(2, 3)
        result = self.game.end_of_the_game()

        # mock_save.assert_not_called()
        self.assertEqual(result, "Game not finished")


if __name__ == "__main__":
    unittest.main()
