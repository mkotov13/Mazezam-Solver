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
        if encoding[i][-1] == 'X':
            finish_row = i
        if encoding[i][0] == 'P':
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
    return level, finish_row-1

if __name__ == "__main__":
    level = read('levels/level2.txt')
    for row in level[0]:
        print row
    print level[1]
