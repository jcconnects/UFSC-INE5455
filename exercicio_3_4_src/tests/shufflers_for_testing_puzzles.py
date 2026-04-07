class TestingShufflerPuzzleGame2x2To1X32:
  # 1  -
  # 3  2
    def shuffle(self, puzzle_game):
        if puzzle_game.dimension == 2:
          puzzle_game.move_tile_from_a_position_to_the_empty_position(1, 2)

class TestingShufflerPuzzleGame2x2To12X3:
  # 1  2
  # -  3
    def shuffle(self, puzzle_game):
        if puzzle_game.dimension == 2:
          puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 1)


class TestingShufflerPuzzleGame3x3To12345X786:
  # 1  2  3
  # 4  5  -
  # 7  8  6
    def shuffle(self, puzzle_game):
        if puzzle_game.dimension == 3:
          puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 3)


class TestingShufflerPuzzleGame3x3To1234X5786:
  # 1  2  3
  # 4  -  5
  # 7  8  6
    def shuffle(self, puzzle_game):
        if puzzle_game.dimension == 3:
          puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 3)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 2)


class TestingShufflerPuzzleGame3x3To1X3425786:
  # 1  -  3
  # 4  2  5
  # 7  8  6
    def shuffle(self, puzzle_game):
        if puzzle_game.dimension == 3:
          puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 3)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 2)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(1, 2)


class TestingShufflerPuzzleGame3x3To123456X78:
  # 1  2  3
  # 4  5  6
  # -  7  8
    def shuffle(self, puzzle_game):
        if puzzle_game.dimension == 3:
          puzzle_game.move_tile_from_a_position_to_the_empty_position(3, 2)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(3, 1)


class TestingShufflerPuzzleGame3x3To123X56478:
  # 1  2  3
  # -  5  6
  # 4  7  8
    def shuffle(self, puzzle_game):
        if puzzle_game.dimension == 3:
          puzzle_game.move_tile_from_a_position_to_the_empty_position(3, 2)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(3, 1)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 1)

class TestingShufflerPuzzleGame3x3ToX23156478:
  # -  2  3
  # 1  5  6
  # 4  7  8
    def shuffle(self, puzzle_game):
        if puzzle_game.dimension == 3:
          puzzle_game.move_tile_from_a_position_to_the_empty_position(3, 2)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(3, 1)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 1)
          puzzle_game.move_tile_from_a_position_to_the_empty_position(1, 1)
