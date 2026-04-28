import random


class ShufflePuzzleLevelCustomized:

    def __init__(self, number_of_shuffles):
        self.number_of_shuffles = number_of_shuffles;

    def shuffle (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")


class ShufflePuzzleLevelEasy:

    def __init__(self):
        self.number_of_shuffles = 4;

    def shuffle (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")


class ShufflePuzzleLevelMedium:

    def __init__(self):
        self.number_of_shuffles = 10;

    def shuffle (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")


class ShufflePuzzleLevelHard:

    def __init__(self):
        self.number_of_shuffles = 30;

    def shuffle (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")