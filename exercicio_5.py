import unittest
from exercicio_3_4_src.src import PuzzleGame, puzzle_game
from exercicio_3_4_src.src.invalid_position_exception import InvalidPositionException

#### PARA EXECUTAR

# rm .mutmut-cache && mutmut run --paths-to-mutate exercicio_3_4_src/src/puzzle_game.py --tests-dir . --runner "python -m pytest exercicio_5.py -x -q"
# mutmut results
# mutmut show <ID>

#### RESULTADOS ORIGINAIS

# Survived 🙁 (63)
# ---- exercicio_3_4_src/src/puzzle_game.py (63) ----
# 14, 19, 23, 25, 32-37, 47-97, 101, 107

#### RESULTADOS COM NOVOS TESTES

# Survived 🙁 (57)
# ---- exercicio_3_4_src/src/puzzle_game.py (57) ----
# 14, 19, 33-36, 47-97


class TestPuzzleGameGetTile(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(3)
        return super().setUp()

    # ==========================================================================
    # Testes Exercício 3 (move_tile())
    # ==========================================================================
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

    def test_move_tile_not_adjacent_to_empty_position(self):
        # A peca 1 inicia em (1, 1), nao adjacente a (3, 3).
        moved = self.puzzle_game.move_tile(1)

        self.assertFalse(moved)
        self.assertEqual(self.puzzle_game.line_of_empty_position, 3)
        self.assertEqual(self.puzzle_game.column_of_empty_position, 3)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 1), 1)
        self.assertIsNone(self.puzzle_game.board.get_tile(3, 3))

    # ==========================================================================
    # Testes Exercício 4 (get_tile())
    # ==========================================================================
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

    def test_tile_in_line_zero(self):
        # Path3: 1(F)-4
        with self.assertRaises(InvalidPositionException):
            self.puzzle_game.get_tile(0,1)

    def test_tile_in_negative_line(self):
        with self.assertRaises(InvalidPositionException):
            self.puzzle_game.get_tile(-1,1)

    def test_get_tile_in_column_bigger_than_board(self):
        with self.assertRaises(InvalidPositionException):
            self.puzzle_game.get_tile(1,5)

    # ==========================================================================
    # Testes Exercício 5
    # ==========================================================================
    # Test 101
    def test_tile_in_column_zero(self):
        with self.assertRaises(InvalidPositionException):
            self.puzzle_game.get_tile(1,0)

    # Test 23, 107
    # 23 - Cria um tabuleiro 3x3 e o tile (3,1) é igual a 3. __put_tiles_in_the_board__ mexe em board e não no dicionário de tiles, que é onde os outros métodos fazem as validações.
        # 1 |  |
        # 2 |  |
        # 3 |  |
    def test_get_tile_in_same_line_of_empty(self):
        tile = self.puzzle_game.get_tile(3,1)
        self.puzzle_game.board.grid

        self.assertEqual(tile, 7)

    # Test 32, 37
    # 32 - verifica só se a peça está dentro do tabuleiro OU está adjacente de um espaço livre. Nesse caso a peça só está dentro do tabuleiro, mas não está adjacente a um espaço livre
    # 37 - é a mesma verificação anterior, mas a mutação é mudar o resultado do else para verdadeiro. O assertFalse pega essa mutação.
    def test_move_tile_from_a_position_to_the_empty_position_that_is_not_adjacent(self):
        moved = self.puzzle_game.move_tile_from_a_position_to_the_empty_position(1,1)
        self.assertFalse(moved)

if __name__ == "__main__":
    unittest.main()


