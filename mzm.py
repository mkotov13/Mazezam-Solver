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

    # TODO: RAISE error if state matrix has any 9's
    return level, finish_row-1


# =========================== Mechanics ===============================

def find_player(matrix):
    # returns player's position for a given state matrix
    if matrix:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 2:
                    return row, col

def move_left(matrix):
    row, col = find_player(matrix)
    leftmost = matrix[row].index(1)
    # check whether the P is in the leftmost column
    if col < 1:
        return False
    # check if there's a block to the left
    if matrix[row][col-1] == 1:
        # if so, check if there's room to move to the left
        if leftmost < 1:
            return False        # cannot move
        else:
            # shift the row one space to the left
            matrix[row].append(matrix[row].pop(0))
            return matrix
    # if no block to the left, move the person there
    else:
        matrix[row][col-1] = 2
        matrix[row][col] = 0
        return matrix

def move_right(matrix):
    row, col = find_player(matrix)
    rightmost = matrix[row][::-1].index(1)
    # check whether the P is in the rightmost column
    if col == (len(matrix[0])-1):
        return False
    # check if there's a block to the right
    if matrix[row][col+1] == 1:
        if rightmost < 1:
            return False        # no room to move to the right
        else:
            # shift the row one space to the right
            matrix[row].insert(matrix[row].pop(), 0)
            return matrix
    else:
        matrix[row][col+1] = 2
        matrix[row][col] = 0
        return matrix

def move_down(matrix):
    row, col = find_player(matrix)
    # check whether the P is in the bottom row
    if row == (len(matrix)-1):
        return False
    # check if there's a block below
    if matrix[row+1][col] == 1:
        return False
    else:
        matrix[row+1][col] = 2   # reassign current player position
        matrix[row][col] = 0     # clear player's previos position
        return matrix


def move_up(matrix):
    row, col = find_player(matrix)
    # check whether the P is in the top row
    if row == 0:
        return False
    # check if there's a block below
    if matrix[row-1][col] == 1:
        return False
    else:
        matrix[row-1][col] = 2   # reassign current player position
        matrix[row][col] = 0     # clear player's previos position
        return matrix


def print_state(matrix):
    if matrix:
        print '\n'
        for row in matrix:
            print row
    else:
        print False

if __name__ == "__main__":
    # TODO: enquire which level should be read in
    level, finish_row = read('levels/level0.txt')
    # make a copy of the initial matrix, store it in the variable level
    state = level
    print finish_row
    print_state(state)
    print_state(move_down(state))
    print 'neighbors'
    print neighbors(state)
    '''
    print_state(move_down(state))
    print_state(move_down(state))
    print_state(move_up(state))
    #print_state(move_up(state))
    print_state(move_down(state))
    print_state(move_right(state))
    print_state(move_right(state))
    print_state(move_up(state))
    print_state(move_right(state))
    print_state(move_down(state))
    #print_state(move_left(state))
    print_state(move_up(state))
    print_state(move_left(state))
    print_state(move_left(state))
    '''
