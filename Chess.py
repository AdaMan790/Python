class Move:
    def __init__(self,board, startRow, startCol, endRow, endCol):
        self.startRow = startRow
        self.startCol = startCol
        self.endRow = endRow
        self.endCol = endCol
        self.pieceCaptured = board[endRow][endCol]
        self.pieceMoved = board[startRow][startCol]
    def makeMove(self):
        board[self.endRow][self.endCol] = self.pieceMoved
        board[self.startRow][self.startCol] = "[]"

board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]"],
    ["[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]"],
    ["[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]"],
    ["[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]"],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

#Draws the board
def drawBoard(board):
    print("   A  B  C  D  E  F  G  H")
    print("  ------------------------")
    for row in range(8):
        print(str(8 - row) + "|", end = " ")
        for col in range(8):
            print(board[row][col], end = " ")
        print()
        
#Chess notation -> move
def chessNotationToMove(board, chessNotation):
    Rowposition = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}
    startCol = Rowposition[chessNotation[0].lower()]
    startRow = 8 - int(chessNotation[1])
    endCol = Rowposition[chessNotation[2].lower()]
    endRow = 8 - int(chessNotation[3])
    move = Move(board, startRow, startCol, endRow, endCol)
    
    return move

#Gets valid moves considering checks
def getValidMoves():
    pass
#Gets moves regardless of checks
def getAllMoves():
    moves = []
    moves.append(getPawnMoves(board)))
    moves.append(getKnightMoves(board))
    moves.append(getBishopMoves(board))
    moves.append(getRookMoves(board))
    moves.append(getQueenMoves(board))
    moves.append(getKingMoves(board))
    return moves

#Gets other moves
def getPawnMoves():
    pass

def getKnightMoves():
    pass   

def getBishopMoves():
    pass

def getRookMoves():
    pass

def getQueenMoves():
    pass

def getKingMoves():
    pass

drawBoard(board)

while True:
    playerMove = input("Enter your move: ")
    chessNotationToMove(board, playerMove).makeMove()
    drawBoard(board)