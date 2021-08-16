def outOfBounds(row, col, width, height):
    return row < 0 or row > height or col < 0 or col > width

def zigzagTraverse(array):
    res = []

    height = len(array) - 1
    width = len(array[0]) - 1

    r, c = 0, 0 # initialization of multiple variables at the same time; don't use r = c = 0
    down = True

    while not outOfBounds(r, c, width, height):
        res.append(array[r][c])
        if down:
            if c == 0 or r == height:
                down = False
                if r == height:
                    c += 1
                else:
                    r += 1
            else:
                r += 1
                c -= 1
        else:
            if r == 0 or c == width:
                down = True
                if c == width:
                    r += 1
                else:
                    c += 1
            else:
                r -= 1
                c += 1
    return res