def symbol_2_int(symbol):
    if symbol == ".":
        return 0
    elif symbol in 'LRC':
        return 1
    elif symbol == 'P':
        return 3
    else:
        return 9

def read(filename):
    f = open(filename, 'rU')
    encoding = [line.strip('\n') for line in f]
    # possibly calculate the number of columns and rows
    COLUMNS, ROWS = len(encoding[0]), len(encoding)

    start_row, finish_row = -1, -1
    for i in range(ROWS):
        # possibly move this inside the symbol_2_int func
        if encoding[i][-1] == 'X':
            finish_row += i
        if encoding[i][0] == 'P':
            start_row += i


    print finish_row, start_row


    level = [[None] * COLUMNS for j in range(ROWS)]

    for i in range(1, ROWS-1):
        for j in range(3, COLUMNS-2):
            level[i][j] = symbol_2_int(encoding[i][j])

    # nice-looking print func
    for row in level:
        print row


read('level.txt')

#if __name__ = "__main"":
