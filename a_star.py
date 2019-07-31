import copy
from operator import attrgetter


class State(object):
    map = []
    h = 0


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_valid(index, row_size, column_size):
    return (index[0] >= 0 and index[1] >= 0) and (index[0] < row_size and index[1] < column_size)


def swap(start_map, a, b):
    map = copy.deepcopy(start_map)
    temp = map[a[0]][a[1]]
    map[a[0]][a[1]] = map[b[0]][b[1]]
    map[b[0]][b[1]] = temp
    return map


def find_position(final, row_size, column_size):
    position_dict = {}
    for row in range(row_size):
        for column in range(column_size):
            position_dict[final[row][column]] = [row, column]
    return position_dict


def solve(start_map, final, row_size, column_size):
    closed_list = []
    position_dict = find_position(final, row_size, column_size)
    start = start_map
    while start != final:
        next_states = []
        for row in range(row_size):
            for column in range(column_size):
                if start[row][column] == 0:
                    if is_valid([row-1, column], row_size, column_size) and start[row-1][column] != 0:  # up
                        state = State()
                        state.map = swap(start, [row, column], [row-1, column])
                        state.h = manhattan_distance([row, column], position_dict[start[row-1][column]])
                        next_states.append(state)
                    if is_valid([row, column+1], row_size, column_size) and start[row][column+1] != 0:  # right
                        state = State()
                        state.map = swap(start, [row, column], [row, column+1])
                        state.h = manhattan_distance([row, column], position_dict[start[row][column+1]])
                        next_states.append(state)
                    if is_valid([row+1, column], row_size, column_size) and start[row+1][column] != 0:  # down
                        state = State()
                        state.map = swap(start, [row, column], [row+1, column])
                        state.h = manhattan_distance([row, column], position_dict[start[row+1][column]])
                        next_states.append(state)
                    if is_valid([row, column-1], row_size, column_size) and start[row][column-1] != 0:  # left
                        state = State()
                        state.map = swap(start, [row, column], [row, column-1])
                        state.h = manhattan_distance([row, column], position_dict[start[row][column-1]])
                        next_states.append(state)
        next_states.sort(key=attrgetter('h'))
        start = next_states[0].map
        print(start)



start = [[1, 3, 5], [4, 7, 2], [6, 8, 0]]
final = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
row = 3
column = 3
pieces = 8
solve(start, final, row, column)
