from src.src.puzzle_game import PuzzleGame


class PuzzleGameWithPlayer(PuzzleGame):

    def __init__(self, dimension, player_name):
        super().__init__(dimension)
        self.__player_name = player_name

    @property
    def player_name(self):
        return self.__player_name

    # MODIFIED TO BE USED IN THE MOCK TESTING...
    def end_of_the_game(self):
        finished = self.board.__eq__(self.board_with_final_state)
        if finished:
            return self.save_game_to_file()
        else:
            return "Game not finished"

    def save_game_to_file(self):
        game_formatted = ''
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    game_formatted += "- "
                else:
                    game_formatted += str(self.board.grid[line][column]) + " "
            game_formatted += "\n"
        with open(f"{self.player_name}.txt", 'w') as output_file:
            output_file.write(game_formatted)
        return "Saved"

