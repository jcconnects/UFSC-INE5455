from .invalid_position_exception import InvalidPositionException

class Board:  # Board comeca com a linha 1 e com a coluna 1

    def __init__(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(0, number_of_lines):
            self.grid.append([None] * number_of_columns)

    @property
    def number_of_lines(self):
        return self.__number_of_lines

    @property
    def number_of_columns(self):
        return self.__number_of_columns

    def put_tile(self, tile, line, column):
        if self.is_inside_the_board(line, column):
            self.grid[line-1][column-1] = tile

    def get_tile(self, line, column):
        if self.is_inside_the_board(line, column):
            return self.grid[line-1][column-1]
        return None

    def is_inside_the_board(self, line, column):
        return line > 0 and line <= self.__number_of_lines and column > 0 and column <= self.number_of_columns

    def change_tiles_in_positions(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def positions_are_adjacent(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def is_in_the_superior_border(self, line, column):
        return self.is_inside_the_board(line, column) and line == 1

    def is_in_the_bottom_border(self, line, column):
        return self.is_inside_the_board(line, column) and line == self.__number_of_lines

    def is_in_the_left_border(self, line, column):
        return self.is_inside_the_board(line, column) and column == 1

    def is_in_the_right_border(self, line, column):
        return self.is_inside_the_board(line, column) and column == self.number_of_columns

    def __eq__(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def __str__(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

