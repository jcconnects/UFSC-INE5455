from .board import Board
from .invalid_position_exception import InvalidPositionException


class PuzzleGame:

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    @property
    def dimension(self):
        return self.__dimension

    @property
    def board(self):
        return self.__board

    @property
    def board_with_final_state(self):
        return self.__board_with_final_state

    @property
    def dic_positions_of_tiles(self):
        return self.__dic_positions_of_tiles

    def __generate_list_of_tiles__(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def __put_tiles_in_the_board__(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def __put_tiles_in_dic_positions__(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def shuffle(self, shuffler):
        shuffler.shuffle(self)

    def move_tile_from_a_position_to_the_empty_position(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def move_tile(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def __move_empty_cell_to_down__ (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def __move_empty_cell_to_up__ (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def __move_empty_cell_to_right__ (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def __move_empty_cell_to_left__ (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def move_empty_tile(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def __print_board_of_puzzle_game__(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def end_of_the_game(self):
        return self.board.__eq__(self.board_with_final_state)

    def get_tile(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def __str__(self):
        return self.board.__str__()
