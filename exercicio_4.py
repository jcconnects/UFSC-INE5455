import unittest
from exercicio_3_4_src.src import PuzzleGame, puzzle_game
from exercicio_3_4_src.src.invalid_position_exception import InvalidPositionException


class TestPuzzleGameGetTile(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(3)
        return super().setUp()

    def test_get_existing_tile(self):
        # Path1: 1(T)-2(F)-5
        tile = self.puzzle_game.get_tile(1,1)
        print("Value of existing tile", tile)

        self.assertEqual(tile, 1)

    def test_get_empty_position(self):
        # Path2: 1(T)-2(T)-3

        tile = self.puzzle_game.get_tile(3,3)
        print("Value of empty tile", tile)

        self.assertEqual(tile, " ")

    def test_get_nonexistent_tile(self):
        # Path3: 1(F)-4
        with self.assertRaises(InvalidPositionException):
            self.puzzle_game.get_tile(0,1)




if __name__ == "__main__":
    unittest.main()


