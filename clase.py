class BackTracking:
    _visited_points_ls = []
    _actual_position_ls = []
    _initial_position_ls = []
    _end_position_ls = []
    _matrix = []

    def __init__(self, _visited_points_ls: list, _actual_position_ls: list, _initial_position_ls: list, _end_position_ls: list, _matrix: list) -> None:
        self._visited_points_ls = _visited_points_ls
        self._actual_position_ls = _actual_position_ls
        self._initial_position_ls = _initial_position_ls
        self._end_position_ls = _end_position_ls
        self._matrix = _matrix

    def __get_matrix_len(self):
        return len(self._matrix)

    def __get_actual_x(self):
        return self._actual_position_ls[0]

    def __get_actual_y(self):
        return self._actual_position_ls[1]

    def __get_actual_position_ls(self):
        return self._actual_position_ls

    def __get_visited_points(self):
        return self._visited_points_ls

    def __set_actual_x(self, value: int) -> None:
        self._actual_position_ls = [value, self._actual_position_ls[1]]

    def __set_actual_y(self, value: int) -> None:
        self._actual_position_ls = [self._actual_position_ls[0], value]

    def __add_visited_point(self, point: list) -> None:
        self._visited_points_ls.append(point)

    def check_completition(self):
        if [item for item in self._initial_position_ls] == [item - 1 for item in self._end_position_ls]:
            print('Solved!')
            return False

    def go_down(self):
        actual_x, actual_y = self.__get_actual_position_ls()
        if actual_x + 1 < self.__get_matrix_len() and [actual_x + 1, actual_y] not in self.__get_visited_points():
            if self._matrix[actual_x + 1][actual_y] == 0:
                self.__set_actual_x(actual_x + 1)
                self.__add_visited_point([self.__get_actual_x, self.__get_actual_y])
                return True
            else:
                return False

    def go_up(self):
        actual_x, actual_y = self.__get_actual_position_ls()
        if actual_x - 1 < self.__get_matrix_len() and [actual_x - 1, actual_y] not in self.__get_visited_points():
            if self._matrix[actual_x - 1][actual_y] == 0:
                self.__set_actual_x(actual_x - 1)
                self.__add_visited_point([self.__get_actual_x, self.__get_actual_y])
                return True
            else:
                return False

    def go_right(self):
        actual_x, actual_y = self.__get_actual_position_ls()
        if actual_y + 1 < self.__get_matrix_len() and [actual_x, actual_y + 1] not in self.__get_visited_points():
            if self._matrix[actual_x][actual_y + 1] == 0:
                self.__set_actual_y(actual_y + 1)
                self.__add_visited_point([self.__get_actual_x, self.__get_actual_y])
                return True
            else:
                return False

    def go_left(self):
        actual_x, actual_y = self.__get_actual_position_ls()
        if actual_y - 1 < self.__get_matrix_len() and [actual_x, actual_y - 1] not in self.__get_visited_points():
            if self._matrix[actual_x][actual_y - 1] == 0:
                self.__set_actual_y(actual_y - 1)
                self.__add_visited_point([self.__get_actual_x, self.__get_actual_y])
                return True
            else:
                return False

    def solve_matrix(self):
        x_actual, y_actual = self._actual_position_ls
        while True:
            if [x_actual, y_actual] == [self._end_position_ls[0] - 1, self._end_position_ls[1] - 1]:
                break