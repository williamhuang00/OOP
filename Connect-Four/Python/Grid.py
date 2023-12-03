class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        #initialize grid with rows and cols provided
        self.board = [['*' for i in range(cols)] for j in range(rows)]
    
    def placeDisk(self, column, color):
        #iterate row by row from final row and upwards
        currentRow = self.rows - 1

        while currentRow >= 0 and self.board[currentRow][column] != '*':
            currentRow -= 1
        
        if currentRow >= 0 and self.board[currentRow][column] == '*':
            self.board[currentRow][column] = color
            return True
        
        return False
    
    def printBoard(self):
        for r in self.board:
            print(r)
    
    def checkWinner(self, r, c):
        #vertical
        above = r - 1
        below = r + 1
        numDisks = 1
        while above >= 0:
            if self.board[above][c] == self.board[r][c]:
                numDisks += 1
            above -= 1
        
        while below < self.rows:
            if self.board[below][c] == self.board[r][c]:
                numDisks += 1
            below += 1
        
        if numDisks == 4:
            return True

        #horizontal

        left = c - 1
        right = c + 1
        numDisks = 1
        while left >= 0:
            if self.board[r][left] == self.board[r][c]:
                numDisks += 1
            left -= 1

        while right < self.cols:
            if self.board[r][right] == self.board[r][c]:
                numDisks += 1
            right += 1
        #diagonal bottomleft to topright

        #diagonal bottomright to topleft

        return False


testGrid = Grid(4, 4)

testGrid.placeDisk(3, 'r')
testGrid.placeDisk(3, 'r')
testGrid.placeDisk(3, 'r')
testGrid.placeDisk(3, 'r')

# testGrid.placeDisk(2, 'b')




testGrid.placeDisk(0, 'r')
testGrid.placeDisk(1, 'r')
testGrid.placeDisk(2, 'r')
testGrid.placeDisk(3, 'r')

testGrid.printBoard()

print(testGrid.checkWinner(0,3))
print(testGrid.checkWinner(1,3))



    
