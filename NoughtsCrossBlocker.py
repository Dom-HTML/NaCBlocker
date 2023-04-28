class NCGrid:
    def __init__(self):
        self.board = ["E"]*9

    def getIndex(self, pos):
        pos = str(pos).strip()
        x = None
        y = None
        for char in pos:
            if char.isnumeric():
                y = int(char)
            elif not char.isnumeric():
                x = char.lower()

        index = None
        L = ord(x)-96
        if y == 1:
            index = (L+y)-1
        elif y == 2:
            index = (L+y)+1
        elif y == 3:
            index = (L+y)+3
            
        return index-1

    def outGrid(self):
        print(f"""••A••B••C•
•┏•┳•┳•┓
1┃{self.board[0]}┃{self.board[1]}┃{self.board[2]}┃
•┣•╋•╋•┫
2┃{self.board[3]}┃{self.board[4]}┃{self.board[5]}┃
•┣•╋•╋•┫
3┃{self.board[6]}┃{self.board[7]}┃{self.board[8]}┃
•┗•┻•┻•┛""")

class NCGame:
    def __init__(self):
        self.board = NCGrid()
        self.gameLoop()

    def gameLoop(self):
        grid = self.board
        print("Make a 2 moves to make a line and the AI will block you")
        moveInput1 = "Enter Your First Move (eg. a2)"
        moveInput2 = "Enter Your Second Move (eg. a2)"
        bot = Bot(self.board)

        self.board.outGrid()
        move1 = self.getInput(moveInput1)
        move2 = self.getInput(moveInput2)
        pMoves = [move1, move2]
        grid.board[grid.getIndex(move1)] = "X"
        grid.board[grid.getIndex(move2)] = "X"
        botMove = bot.calculateMove(pMoves)
        grid.board[grid.getIndex(botMove)] = "O"
        self.board.outGrid()
        print("You Lose")

    def getInput(self, prompt):
        inp = str(input(prompt+": "))
        return inp

class Bot:
    def __init__(self, board):
        self.board = board

    def calculateMove(self, pMoves):
        if pMoves[0][0] == pMoves[1][0] or pMoves[0][1] == pMoves[1][1]:
            return self.calcStraight(pMoves)
        else:
            return self.calcDiagonal(pMoves)

    def calcDiagonal(self, pMoves):
        finalMove = ""
        letterTotal = 0
        for move in pMoves:
            letterTotal += ord(move[0])

        if letterTotal == 197:
            finalMove += ("a")
        elif letterTotal == 196:
            finalMove += ("b")
        elif letterTotal == 195:
            finalMove += ("c")

        numTotal = 0
        for move in pMoves:
            numTotal += int(move[1])

        if numTotal == 5:
            finalMove += ("1")
        elif numTotal == 4:
            finalMove += ("2")
        elif numTotal == 3:
            finalMove += ("3")

        return finalMove

    def calcStraight(self, pMoves):
        isVert = False
        finalMove = ""
        
        letterTotal = 0    
        for move in pMoves:
            letterTotal += ord(move[0])

        if letterTotal == 194:
            finalMove += ("a")
            isVert = True
        elif letterTotal == 196:
            finalMove += ("b")
            isVert = True
        elif letterTotal == 198:
            finalMove += ("c")
            isVert = True
        elif letterTotal == 197:
            finalMove += ("a")
        elif letterTotal == 196:
            finalMove += ("b")
        elif letterTotal == 195:
            finalMove += ("c")

        numTotal = 0
        for move in pMoves:
            numTotal += int(move[1])

        if isVert:
            if numTotal == 5:
                finalMove += ("1")
            elif numTotal == 4:
                finalMove += ("2")
            elif numTotal == 3:
                finalMove += ("3")
        else:
            finalMove += (pMoves[0][1])

        return finalMove     

game = NCGame()
        
