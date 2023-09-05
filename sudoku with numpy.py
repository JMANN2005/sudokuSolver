import numpy as np
from time import sleep

class Board:
    def __init__(self):
        # get board from text file
        file = open("sudoku.txt").read()
        lines = file.split("\n")
        #create empty board
        self.board = np.empty((9,9))
        #fill board with values from text file
        for i in range(0,9):
            for j in range(0,9):
                self.board[i,j] = lines[i][j]
    def fillNotepad(self,out):
        file = open("sudoku.txt","w")
        text = ""
        for i in range(0,9):
            for j in range(0,9):
                text += str(int(out[i][j]))
            text += "\n"
        file.writelines(text)
        file.close()
    def showboard(self):
        #loop through each row of the board
        for i in range(0,9):
            row = ""
            for j in range(0,9): # add each item in the row so can be outputted on 1 row
                row += str(int(self.board[i,j]))
            print(row)
    def updateBoard(self,n,x,y):
        self.board[x][y] = n
    def getboard(self):
        return self.board.copy()
    def checkUnique(self, arr):
        arr.sort()
        for j in range(0,8):
            if arr[j] == arr[j+1]:
                return False
        return True
    def createSquare(self,startx,starty):
        flatSquare = []
        for i in range(0,3):
            for j in range(0,3):
                flatSquare.append(self.board[i+starty][j+startx])
        return flatSquare
    def checkBoard(self):
        error = False # flag for if there is an error detected
        
        if 0 in self.board: #check every value has been filled
            return True
        #check rows and columns are all unique if they are then it should be solved
        for i in range(0,9):
            error = not self.checkUnique(self.board[i].copy())
            if (error):
                return error
            error = not self.checkUnique(self.board[:][i].copy())
            if (error):
                return error
        #see if the boxes are all unique
        for i in range(0,3):
            for j in range(0,3):
                error = not self.checkUnique(self.createSquare((i*3),(j*3))) 
                if (error):
                    return error
        return error
    

class Solver:
    def __init__(self):
        self.board = board.getboard()
    def findPossible(self,y,x):
        self.board = board.getboard()
        possible = [1,2,3,4,5,6,7,8,9]
        flatSquare = board.createSquare((x//3)*3,(y//3)*3)
        for i in range(0,9):
            try:
                possible.remove(self.board[i][x])
            except:
                pass
                
            try:
                possible.remove(self.board[y][i])
            except:
                pass
            try:
                possible.remove(flatSquare[i])
            except:
                pass
        return possible
    def solve(self):
        self.board = board.getboard()
        for i in range(0,9):
            for j in range(0,9):
                self.board = board.getboard()
                if self.board[i][j] == 0:
                    possible = self.findPossible(i,j)
                    for n in possible:
                        board.updateBoard(n,i,j)
                        self.solve()
                        board.updateBoard(0,i,j)
                    return
        board.showboard()
        print(not(board.checkBoard()))
        input("found")
        board.fillNotepad(self.board)
        
        return 

board = Board()
solver = Solver()
    
board.showboard()
print(not(board.checkBoard()))

#down, accross
#print(solver.findPossible(8,0))

print("solving")
solver.solve()