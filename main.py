from dungeons import *
import random
import time

def Create2DArray(value,x,y):
    arr = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(value)
        arr.append(row)
    return arr

def GetNeighbours(x,y,board):
    #an e is for empty neighbours and j is for joined neighbours
    #the the first of the two pairs of numbers(x,y) at the end indicate where an empty character should be to be a joining neighbour
    #the second pair is where a tile should have an empty character to meet the join to be valid
    positions = [[x-1,y,"e",2,1,0,1,"l"],[x+1,y,"e",0,1,2,1,"r"],[x,y-1,"e",1,2,1,0,"u"],[x,y+1,"e",1,0,1,2,"d"]]
    #neighbours: left, right, up, down

    n = []

    for position in positions:
        if position[0] < 0 or position[1] < 0:continue
        try:
            tile = board[position[1]][position[0]]
            if not tile:
                n.append(position)
            elif Tiles[tile].arrangement[position[4]][position[3]] == " ":
                position[2] = "j"
                n.append(position)
            elif Tiles[tile].arrangement[position[4]][position[3]] == "#":
                position[2] = "w"
                n.append(position)

        except IndexError as e:
            pass
    return n

def CheckSquareCollision(x,y,length,board):
    for Y in range(y,y+length):
        for X in range(x,x+length):
            if Y >= len(board) or X >= len(board[Y]):
                return True
            if board[Y][X]: return True
    return False

def GenerateBoard(xSize,ySize):
    board = Create2DArray(False,xSize,ySize)

    board[1][0] = "Vertical"
    board[0][1] = "Horizontal"
    board[1][2] = "Vertical"
    board[2][1] = "Horizontal"

    possiblePositions = [[x,y] for x in range(xSize) for y in range(ySize)]

    t = Create2DArray(0,xSize,ySize)

    def ChooseDungeonType(xx,yy):
        #calulcate largest dungeon that can fit
        l = 1
        while not CheckSquareCollision(xx,yy,l,board):
            l += 1
        l -= 1

        options = [Dungeons[key] for key in Dungeons.keys()]

        #filter dungeons that are too big to fit in the available space
        options = list(filter(lambda opt: opt.squareLength <= l,options))

        temp = []

        for option in options:
            valid = True
            for tx in range(option.size[0]):
                for ty in range(option.size[1]):
                    neighbours = GetNeighbours(xx+tx,yy+ty,board)
                    for n in neighbours:
                        #joins must be met with a valid dungeon
                        if (n[2] == "j" or n[2] == "w") and Tiles[option.arrangement[ty][tx]].arrangement[n[6]][n[5]] != Tiles[board[n[1]][n[0]]].arrangement[n[4]][n[3]]:
                            valid = False
            if valid:
                temp.append(option)

        options = temp

        #filter dungeons that

        #choose a dungeon based on their weights
        totalWeight = sum([opt.weight for opt in options])
        choice = random.randint(0,totalWeight)
        cW = 0
        for opt in options:
            if choice >= cW and choice <= cW + opt.weight:
                return opt
            cW += opt.weight

    while possiblePositions != []:
        x,y = random.choice(possiblePositions)
        if board[y][x]:
            possiblePositions.remove([x,y])
            continue

        #Get a dungeon

        d = ChooseDungeonType(x,y)
        if not d:
            board[y][x] = "Error"
            DrawBoard(board)
            raise Exception(f"No tile could fit at location {x} , {y}")
        for yy in range(d.size[1]):
            for xx in range(d.size[0]):
                board[yy+y][xx+x] = d.arrangement[yy][xx]
                possiblePositions.remove([xx+x,yy+y])

    return board

def DrawBoard(board):
    buffer = ""
    xAxis = []
    for i in range(len(board[0])):
        if i < 10:
            xAxis.append(" "+str(i)+" ")
        elif i < 100:
            xAxis.append(" "+str(i))
        else:
            xAxis.append(str(i))


    buffer += "\n"+" "+"   ".join(xAxis)+"\n"
    for y in range(len(board) * 3):
        row = ""
        for x in range(len(board[y // 3]) * 3):
            try:
                Tile = Tiles[board[y // 3][x // 3]]
                row += Tile.arrangement[y % 3][x % 3]+" "
            except:
                row += "0 "
        if y % 3 == 1:
            row += " "+str(y//3)
        buffer += row+"\n"
    print(buffer)


board = GenerateBoard(30,20)
DrawBoard(board)
