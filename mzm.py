def symbol_2_int(symbol):
    if symbol == ".":
        return 0
    elif symbol in 'LRCI':
        return 1
    elif symbol == 'P':
        return 2
    else:
        return 9

def read(filename):
    f = open(filename, 'rU')
    encoding = [list(line.strip('\n')) for line in f]
    COLUMNS, ROWS = len(encoding[0]), len(encoding)

    # looks for P in the first column and X in the last column
    start_row, finish_row = -1, -1
    for i in range(ROWS):
        # possibly move this inside the symbol_2_int func
        if encoding[i][-3] == '*':
            finish_row = i
        if encoding[i][2] == '+':
            start_row = i
    # update the position of P
    encoding[start_row][3] = 'P'

    # Create an array with smaller dimensions, since the outside hashtags are irrelevant
    level = [[None] * (COLUMNS-6) for j in range(ROWS-2)]

    for i in range(1, ROWS-1):
        for j in range(3, COLUMNS-3):
            level[i-1][j-3] = symbol_2_int(encoding[i][j])

    '''nice-looking print func
    for row in level:
        print row
    '''
    # TODO: RAISE error if state matrix has any 9's
    return level, finish_row-1


def move_left(state):
    row = state[1]
    col = state[2]
    # check whether the P is in the leftmost c0olumn
    if col < 1:
        return False
    else:
        # check if there's a block to the left
        if state[row][col-1] == 1:
            return False
        else:
            state[row][col-1] = 2
            state[row][col] = 0
            return state, row, col-1

def move_down(state):
    row = state[1]
    col = state[2]
    matrix = state[0]
    # check whether the P is in the leftmost c0olumn
    if row == len(matrix):
        return False
    else:
        # check if there's a block to the left
        if matrix[row-1][col] == 1:
            return False
        else:
            matrix[row-1][col] = 2   # reassign current player position
            matrix[row][col] = 0     # clear player's previos position
            return matrix, row, col-1


if __name__ == "__main__":
    # TODO: enquire which level should be read in
    level = read('levels/level0.txt')
    for row in level[0]:
        print row
    print level[1]
    print len(level[0])
    state = (level[0], 0, 0)
    move_down(state)
