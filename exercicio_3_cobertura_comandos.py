import unittest
from src.src import PuzzleGame


class TestPuzzleGameMoveTile(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(3)
        return super().setUp()

    # Critério de COBERTURA DE COMANDOS
    def test_move_tile_adjacent_to_empty_position(self):
        # Path1: 1-2-3(T)-4(T)-5
        # No estado inicial, a posicao vazia fica em (3, 3).
        # A peca 8 esta em (3, 2), portanto o movimento deve ser valido.
        moved = self.puzzle_game.move_tile(8)

        self.assertTrue(moved)
        self.assertEqual(self.puzzle_game.line_of_empty_position, 3)
        self.assertEqual(self.puzzle_game.column_of_empty_position, 2)
        self.assertEqual(self.puzzle_game.board.get_tile(3, 3), 8)
        self.assertIsNone(self.puzzle_game.board.get_tile(3, 2))

    def test_move_outside_board_tile(self):
        # Path2: 1-2-3(F)-6
        self.puzzle_game.dic_positions_of_tiles[9] = (10,10)
        # A peca 9 esta em (10,10), fora do tabuleiro, portanto o movimento deve ser inválido.
        moved = self.puzzle_game.move_tile(9)

        self.assertFalse(moved)


if __name__ == "__main__":
    unittest.main()


