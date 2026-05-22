class Move:
    def __init__(self,board, startRow, startCol, endRow, endCol):
        self.board = board
        self.startRow = startRow
        self.startCol = startCol
        self.endRow = endRow
        self.endCol = endCol
        self.pieceCaptured = board[endRow][endCol]
        self.pieceMoved = board[startRow][startCol]
    def makeMove(self):
        self.board[self.endRow][self.endCol] = self.pieceMoved
        self.board[self.startRow][self.startCol] = "[]"

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
    moves = getAllMoves()

    
#Gets moves regardless of checks
def getAllMoves():
    moves = []
    getPawnMoves(moves)
    getKnightMoves(moves)
    getBishopMoves(moves)
    getRookMoves(moves)
    getQueenMoves(moves)
    getKingMoves(moves)
    return moves

#Gets other moves
def getPawnMoves(moves):
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "wP":
                if row > 0:
                    if board[row] == 7:
                        moves.append(Move(board, row, col, row - 2, col))
                    
                    if board[row - 1][col] == "[]":     
                        moves.append(Move(board, row, col, row - 1, col))
                        
                    if 0 < col < 8:
                        if board[row - 1][col - 1] != "[]":
                            moves.append(Move(board, row, col, row - 1, col - 1))   
                        if board[row - 1][col + 1] != "[]":
                            moves.append(Move(board, row, col, row - 1, col + 1))
            
            elif board[row][col] == "bP":
                if row < 8:
                    if board[row] == 1:
                        moves.append(Move(board, row, col, row + 2, col))
                        
                    if board[row + 1][col] == "[]":     
                        moves.append(Move(board, row, col, row + 1, col))
                        
                    if 0 < col < 8:
                        if board[row + 1][col + 1] != "[]":
                            moves.append(Move(board, row, col, row + 1, col + 1))   
                        if board[row + 1][col - 1] != "[]":
                            moves.append(Move(board, row, col, row + 1, col - 1))

def getKnightMoves(moves):
    pass   

def getBishopMoves(moves):
    pass

def getRookMoves(moves):
    pass

def getQueenMoves(moves):
    pass

def getKingMoves(moves):
    pass

drawBoard(board)

while True:
    playerMove = input("Enter your move: ")
    chessNotationToMove(board, playerMove).makeMove()
    drawBoard(board)