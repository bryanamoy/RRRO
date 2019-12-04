grid = [
    ['o', 0, 0],
    [0, 0, 0],
    [0, 0, 'x']]


# robot = x
# player = 0
nextMove = (0, 0)
def move():
    global grid
    global nextMove
    #find potential winning move for robot
    if grid[0][0] == 'x':           #x in 0, 0
        if grid[0][1] == 'x':       #[x, x, 0]
            if grid[0][2] == 0:     #[
                grid[0][2] = 'x'    #[
                nextMove = (0, 2)
                return nextMove
        if grid[0][2] == 'x':      #[x, 0, x
            if grid[0][1] == 0:
                grid[0][1] = 'x'
                nextMove = (0, 1)
                return nextMove
        if grid[1][0] == 'x':      #[x
            if grid[2][0] == 0:    #[x
                grid[2][0] = 'x'   #[0
                nextMove = (2, 0)
                return nextMove
        if grid[1][1] == 'x':     #[x
            if grid[2][2] == 0:   #[0, x
                grid[2][2] = 'x'  #[0, 0, 0
                nextMove = (2, 2)
                return nextMove
        if grid[2][2] == 'x':     #[x
            if grid[1][1] == 0:   #[0, 0
                grid[1][1] = 'x'  #[0, 0, x
                nextMove = (1, 1)
                return nextMove
        if grid[2][0] == 'x':     #[x
            if grid[1][0] == 0:   #[0
                grid[1][0] = 'x'  #[x
                nextMove = (1, 0)
                return nextMove
    if grid[0][1] == 'x':  #x in 0, 1
        if grid[1][1] == 'x':       #[0, x
            if grid[2][1] == 0:     #[0, x
                grid[2][1] = 'x'    #[0, 0
                nextMove = (2, 1)
                return nextMove
        if grid[2][1] == 'x':       #[0, x
            if grid[1][1] == 0:     #[0, 0
                grid[1][1] == 'x'   #[0, x
                nextMove = (1, 1)
                return nextMove
    if grid[0][2] == 'x':  #x in 0, 2
        if grid[1][1] == 'x':       #[0, 0, x
            if grid[2][0] == 0:     #[0, x,
                grid[2][0] = 'x'    #[0
                nextMove = (2, 0)
                return nextMove
    if grid[1][0] == 'x':         #x in 1, 0
        if grid[1][1] == 'x':       #[0
            if grid[1][2] == 0:     #[x, x, 0
                grid[1][2] = 'x'    #[0
                nextMove = (1, 2)
                return nextMove
        if grid[2][0] == 'x':       #[0
            if grid[0][0] == 0:     #[x
                grid[0][0] = 'x'    #[x
                nextMove = (0, 0)
                return nextMove
    if grid[1][1] == 'x':         #x in 1, 1
        if grid[1][2] == 'x':       #[
            if grid[1][0] == 0:     #[0, x, x
                grid[1][0] = 'x'    #[
                nextMove = (1, 0)
                return nextMove
        if grid[2][1] == 'x':
            if grid[0][1] == 0:
                grid[0][1] = 'x'
                nextMove = (0, 1)
                return nextMove
    if grid[1][2] == 'x':         #x in 1, 2
        if grid[1][0] == 'x':       #[
            if grid[1][1] == 0:     #[x, 0, x
                grid[1][1] = 'x'    #[0
                nextMove = (1, 1)
                return nextMove
        if grid[2][2] == 'x':       #[0, 0, 0
            if grid[0][2] == 0:     #[0, 0, x
                grid[0][2] = 'x'    #[0, 0, x
                nextMove = (0, 2)
                return nextMove
    if grid[2][0] == 'x':         #x in 2, 0
        if grid[2][1] == 'x':       #[
            if grid[2][2] == 0:     #[
                grid[2][2] = 'x'    #[x, x, 0
                nextMove = (2, 2)
                return nextMove
        if grid[2][2] == 'x':       #[
            if grid[2][1] == 0:     #[
                grid[2][1] = 'x'    #[x, 0, x
                nextMove = (2, 1)
                return nextMove
    if grid[2][1] == 'x':         #x in 2, 1
        if grid[2][2] == 'x':       #[
            if grid[2][0] == 0:     #[
                grid[2][0] = 'x'    #[0, x, x
                nextMove = (2, 0)
                return nextMove
    #find potential winning moves for player
    if grid[0][0] == 'o':           #o in 0,0
        if grid[0][1] == 'o':       #[o, o, 0
            if grid[0][2] == 0:     #[
                grid[0][2] = 'x'    #[
                nextMove = (0, 2)
                return nextMove
        if grid[0][2] == 'o':       #[o, 0, o
            if grid[0][1] == 0:     #[
                grid[0][1] = 'x'    #[
                nextMove = (0, 1)
                return nextMove
        if grid[1][0] == 'o':       #[o
            if grid[2][0] == 0:     #[o
                grid[2][0] = 'x'    #[0
                nextMove = (2, 0)
                return nextMove
        if grid[2][0] == 'o':       #[o
            if grid[1][0] == 0:     #[0
                grid[1][0] = 'x'    #[o
                nextMove = (1, 0)
                return nextMove
        if grid[1][1] == 'o':       #[o
            if grid[2][2] == 0:     #[0, o, 0
                grid[2][2] = 'x'    #[0, 0 ,0
                nextMove = (2, 2)
                return nextMove
        if grid[2][2] == 'o':       #[o,
            if grid[1][1] == 0:     #[0, 0,
                grid[1][1] = 'x'    #[0, 0, o
                nextMove = (1, 1)
                return nextMove
    if grid[0][1] == 'o':           #[0, o, o
        if grid[0][2] == 'o':
            grid[0][0] = 'x'
            nextMove = (0, 0)
            return nextMove
        if grid[1][1] == 'o':       #[0, o
            if grid[2][1] == 0:     #[0, o
                grid[2][1] = 'x'    #[0, 0
                nextMove = (2, 1)
                return nextMove
        if grid[2][1] == 'o':       #[0, o
            if grid[1][1] == 0:     #[0, 0
                grid[1][1] = 'x'    #[0, o
                nextMove = (1, 1)
                return nextMove
    if grid[0][2] == 'o':           #[0, 0, o
        if grid[1][1] == 'o':       #[0, o
            if grid[2][0] == 0:     #[0
                grid[2][0] = 'x'
                nextMove = (2, 0)
                return nextMove
        if grid[2][0] == 'o':       #[0, 0, o
            if grid[1][1] == 0:     #[0, 0
                grid[1][1] = 'x'    #[o
                nextMove = (1, 1)
                return nextMove
        if grid[1][2] == 'o':       #[0, 0, o
            if grid[2][2] == 0:     #[0, 0, o
                grid[2][2] = 'x'    #[0, 0, 0
                nextMove = (2, 2)
                return nextMove
        if grid[2][2] == 'o':       #[0, 0, o
            if grid[1][2] == 0:     #[0, 0, 0
                grid[1][2] = 'x'    #[0, 0, o
                nextMove = (1, 2)
                return nextMove
    if grid[1][0] == 'o':
        if grid[2][0] == 'o':       #[0, 0, 0
            if grid[0][0] == 0:     #[o, 0, 0
                grid[0][0] = 'x'    #[o, 0, 0
                nextMove = (0, 0)
                return nextMove
        if grid[1][1] == 'o':       #[0, 0, 0
            if grid[1][2] == 0:     #[o, o, 0
                grid[1][2] = 'x'    #[0, 0, 0
                nextMove = (1, 2)
                return nextMove
        if grid[1][2] == 'o':       #[0, 0, 0
            if grid[1][1] == 0:     #[o, 0, o
                grid[1][1] = 'x'    #[0, 0, 0
                nextMove = (1, 1)
                return nextMove
    if grid[1][1] == 'o':
        if grid[1][2] == 'o':       #[0, 0, 0
            if grid[1][0] == 0:     #[0, o, o
                grid[1][0] = 'x'    #[0, 0, 0
                nextMove = (1, 0)
                return nextMove
        if grid[2][1] == 'o':       #[0, 0, 0
            if grid[0][1] == 0:     #[0, o, 0
                grid[0][1] = 'x'    #[0, o, 0
                nextMove = (0, 1)
                return nextMove
        if grid[2][2] == 'o':       #[0, 0, 0
            if grid[0][0] == 0:     #[0, o, 0
                grid[0][0] = 'x'    #[0, 0, o
                nextMove = (0, 0)
                return nextMove
        if grid[2][0] == 'o':       #[0, 0, 0
            if grid[0][2] == 0:     #[0, o, 0
                grid[0][2] = 'x'    #[o, 0, 0
                nextMove = (0, 2)
                return nextMove
    if grid[1][2] == 'o':
        if grid[2][2] == 'o':       #[0, 0, 0
            if grid[0][2] == 0:     #[0, 0, o
                grid[0][2] = 'x'    #[0, 0, o
                nextMove = (0, 2)
                return nextMove
    if grid[2][0] == 'o':
        if grid[2][1] == 'o':       #[0, 0, 0
            if grid[2][2] == 0:     #[0, 0, 0
                grid[2][2] = 'x'    #[o, o, 0
                nextMove = (2, 2)
                return nextMove
        if grid[2][2] == 'o':       #[0, 0, 0
            if grid[2][1] == 0:     #[0, 0, 0
                grid[2][1] = 'x'    #[o, 0, o
                nextMove = (2, 1)
                return nextMove
    if grid[2][1] == 'o':
        if grid[2][2] == 'o':       #[0, 0, 0
            if grid[2][0] == 0:     #[0, 0, 0
                grid[2][0] = 'x'    #[0, o, o
                nextMove = (2, 0)
                return nextMove
    else:
        rows = 3
        columns = 3
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    grid[i][j] = 'x'
                    nextMove = (i, j)
                    return nextMove


move()
print(nextMove)
