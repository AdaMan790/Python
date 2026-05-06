import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random

page = tk.Tk()
player = "X"

page.geometry("500x500")
page.resizable(False,False)
page.title("Naughts and Crosses")

start = True

buttons = []
board = []
Ai = True
AiMode = "hard"
if messagebox.askyesno("AI?", "Are you playing 2 player?"):
    Ai = False
else:
    if messagebox.askyesno("Difficulty", "Easy Ai?"):
        AiMode = "easy"
    if messagebox.askyesno("Start?", "Would you like to be first?"):
        start = True
    else:
        start = False

if not start:
    player = "O"

for i in range(3):
    page.columnconfigure(i, weight=1)
    page.rowconfigure(i,weight=1)

def saveFile(winner):
    page.withdraw()

    file_path = filedialog.asksaveasfilename(
    title="Select a File",
    initialdir="//hazelwick.internal/users/23users/23LOSKOTAd/XO",
    )

    if file_path:
        print(f"File selected: {file_path}")
    else:
        messagebox.showwarning("Warning", "No file selected. Program is shutting down...")
        return

    with open(file_path, "r") as file:
        content = file.readlines()

    with open(file_path, "w") as file:
        if not content:
            Xscore =  0
            Yscore =  0
            Draws =  0
            if winner == "X":
                Xscore += 1
            elif winner == "O":
                Yscore += 1
            else:
                Draws += 1

            file.write(f"Total X wins: {Xscore} \nTotal O wins: {Yscore} \nTotal draws: {Draws}")
            return
        
        Xscore =  int(content[0].split(":")[1])
        Yscore =  int(content[1].split(":")[1])
        Draws =  int(content[2].split(":")[1])
        if winner == "X":
            Xscore += 1
        elif winner == "O":
            Yscore += 1
        else:
            Draws += 1

        file.write(f"Total X wins: {Xscore} \nTotal O wins: {Yscore} \nTotal draws: {Draws}")

    messagebox.showinfo("Scoreboard", f"Total X wins: {Xscore} \nTotal O wins: {Yscore} \nTotal draws: {Draws}")
    
def checkwin(board):
    global player
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return True
        elif board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        elif board[0][2] == board[1][1] == board[2][0] != " ":
            return True

def checkdraw(board):
    counter = 0
    for i in range(3):
        if board[i][0] != " " and board[i][1] != " " and board[i][2] != " ":
            counter += 1
    if counter == 3:
        return True

def runAi(buttons):
    global Ai
    tempboard = []
    if Ai:
        global AiMode
        global player
        if AiMode == "easy":
            
            x = random.randint(0,2)
            y = random.randint(0,2)
            button = buttons[x][y]
            while button['text'] != " ":
                x = random.randint(0,2)
                y = random.randint(0,2)
                button = buttons[x][y]
                
            button.configure(text = player, state = "disabled")
            board[x][y] = player
            checkall(board)
            return


                
        elif AiMode == "hard":
            #check if can win
            for row in range(3):
                for col in range (3):
                    if board[row][col] == " ":
                        tempboard = [r[:] for r in board]
                        tempboard[row][col] = player
                        if checkwin(tempboard):
                            scoreMove(board)
                            button = buttons[row][col]
                            button.configure(text = player, state = "disabled")
                            board[row][col] = player
                            checkall(board)
                            return
                        
            #check if player can win
            for row in range(3):
                for col in range (3):
                    if board[row][col] == " ":
                        tempboard = [r[:] for r in board]
                        tempboard[row][col] = "X"
                        if checkwin(tempboard):
                            scoreMove(board)
                            print("Scoring overriden, must block player.")
                            button = buttons[row][col]
                            button.configure(text = player, state = "disabled")
                            board[row][col] = player
                            checkall(board)
                            return


            scoreBoard = scoreMove(board)
            topScores = []
            for i in range(3):
                topScores.append(max(scoreBoard[i]))
            topScore = max(topScores)
            bestMoves = []
            for row in range(3):
                for col in range(3):
                    if topScore == scoreBoard[row][col]:
                        bestMoves.append((row, col))

            choice = random.choice(bestMoves)

            row = choice[0]
            col = choice[1]
            
            button = buttons[row][col]
            button.configure(text = player, state = "disabled")
            board[row][col] = player
            checkall(board)
            return

def checkall(board):
    global player
    
    if checkwin(board):
        messagebox.showinfo("You won!", f"Player {player} won!")
        saveFile(player)
        quit()

    if checkdraw(board):
        messagebox.showinfo("You drew!", f"It's a draw!")
        saveFile("Draw")
        quit()
            
    if player == "X":
        player = "O"
    else:
        player = "X"       
                           

        
def buttonclick(row, col):
    global player
    
    button = buttons[row][col]
    button.configure(text = player, state = "disabled")

    board[row][col] = player

    checkall(board)

    runAi(buttons)

def scoreMove(board):
    scoreboard = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]

    #Horizontal
    
    for row in range(3):
        rowCount = 0
        OCount = 0
        IncreaseScore = False
        for item in range(3):
            if board[row][item] == " " or board[row][item] == "O":
                rowCount += 1
            if board[row][item] == "O":
                OCount += 1
        if rowCount == 3:
            IncreaseScore = True

        if IncreaseScore == True:
            for item in range(3):
                scoreboard[row][item] += 1 + OCount*2
        else:
            for item in range(3):
                scoreboard[row][item] -= 1

    #Vertical
    for col in range(3):
        colCount = 0
        OCount = 0
        IncreaseScore = False
        for row in range(3):
            if board[row][col] == " " or board[row][col] == "O":
                colCount += 1
            if board[row][col] == "O":
                OCount += 1
        if colCount == 3:
            IncreaseScore = True

        if IncreaseScore == True:
            for row in range(3):
                scoreboard[row][col] += 1 + OCount*2
        else:
            for row in range(3):
                scoreboard[row][col] -= 1

    #Diagonal
    Dcount = 0
    OCount = 0
    IncreaseScore = False
    for i in range(3):
        if board[i][i] == " " or board[i][i] == "O":
            Dcount += 1
        if board[i][i] == "O":
            OCount += 1

    if Dcount == 3:
        IncreaseScore = True
        
    if IncreaseScore == True:
        for i in range(3):
            scoreboard[i][i] += 1 + OCount*2
    else:
        for i in range(3):
            scoreboard[i][i]-= 1

    Dcount = 0
    OCount = 0
    IncreaseScore = False
    for i in range(3):
        if board[i][2 - i] == " " or board[i][2 - i] == "O":
            Dcount += 1
        if board[i][2 - i] == "O":
            OCount += 1
            
    if Dcount == 3:
        IncreaseScore = True
        
    if IncreaseScore == True:
        for i in range(3):
            scoreboard[i][2 - i] += 1 + OCount*2
    else:
        for i in range(3):
            scoreboard[i][2 - i]-= 1

    scoreboard[1][1] += 2
    
    for row in range(3):
        for col in range(3):
            if board[row][col] != " ":
                scoreboard[row][col] = -99

    for row in range(3):
        print(scoreboard[row])

    print()
    
    return scoreboard
    
for _ in range(3):
    board.append([" ", " ", " "])

for row in range(3):
    buttonrow = []
    for col in range(3):
        button = tk.Button(page, text = " ", command = lambda r = row, c = col: buttonclick(r,c), font = ("System", 60), bg = 'black', fg = 'white')
        button.grid(column = col, row = row, sticky="nesw", padx = 3, pady =3)
        buttonrow.append(button)

    buttons.append(buttonrow)

if not start:
    runAi(buttons)

page.mainloop()
