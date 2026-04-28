# Testes executados na primeira execução do Mutmut. 

test_move_tile_adjacent_to_empty_position
test_move_outside_board_tile
test_move_tile_not_adjacent_to_empty_position
test_get_existing_tile
test_get_empty_position
test_tile_in_line_zero
test_tile_in_negative_line
test_get_tile_in_column_bigger_than_board


# Mutantes que não foram mortos, com destaque para os 5 mutantes selecionados.

Survived 🙁 (63)
---- src/src/puzzle_game.py (63) ----
14, 19, 23, 25, 32-37, 47-97, 101, 107

## Mutantes selecionados: 23, 32, 37, 101 e 107

# Novos testes que matarão os 5 mutantes vivos. Cada teste deve identificar o mutante que será morto.

test_tile_in_column_zero
test_get_tile_in_same_line_of_empty
test_move_tile_from_a_position_to_the_empty_position_that_is_not_adjacent

# Mutantes que permanecem vivos após a nova execução do Mutmut.

Survived 🙁 (57)
---- src/src/puzzle_game.py (57) ----
14, 19, 33-36, 47-97

# PARA EXECUTAR

``` bash
rm .mutmut-cache && mutmut run --paths-to-mutate src/src/puzzle_game.py --tests-dir . --runner "python -m pytest exercicio_5.py -x -q"
mutmut results
mutmut show <ID>
```

