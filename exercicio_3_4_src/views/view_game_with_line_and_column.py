from exercicio_3_src.src import PuzzleGame
from exercicio_3_src.src import ShufflePuzzleLevelEasy, ShufflePuzzleLevelMedium, \
    ShufflePuzzleLevelHard

def play_game_using_line_and_column():
    puzzle_game = PuzzleGame(3)
    entry = input("Enter the difficulty of the level game (1-easy 2-medium 3-hard): ")
    if (entry == "1"):
        ShufflePuzzleLevelEasy().shuffle(puzzle_game)
    elif (entry == "2"):
        ShufflePuzzleLevelMedium().shuffle(puzzle_game)
    elif (entry == "3"):
        ShufflePuzzleLevelHard().shuffle(puzzle_game)
    else:
        return
    puzzle_game.__print_board_of_puzzle_game__()
    line = ''
    while not puzzle_game.end_of_the_game() and not entry == "end":
        line = input("Enter the line and column to move or \"end\" to terminate the game: ")
        if line != "end":
            column = input()
            puzzle_game.move_tile_from_a_position_to_the_empty_position(int(line), int(column))
            puzzle_game.__print_board_of_puzzle_game__()
    print("The End.")

play_game_using_line_and_column()