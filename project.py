
def checkRow(board, row):

def checkCol(board, col):

def checkGrid()

def inRange(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] > 9 or board[i][j] < 1:
                return False
    
    return True

def isValidSudoku(board):


if __name__ == '__main__':
   
  board = [ [ 7, 9, 2, 1, 5, 4, 3, 8, 6 ],
            [ 6, 4, 3, 8, 2, 7, 1, 5, 9 ],
            [ 8, 5, 1, 3, 9, 6, 7, 2, 4 ],
            [ 2, 6, 5, 9, 7, 3, 8, 4, 1 ],
            [ 4, 8, 9, 5, 6, 1, 2, 7, 3 ],
            [ 3, 1, 7, 4, 8, 2, 9, 6, 5 ],
            [ 1, 3, 6, 7, 4, 8, 5, 9, 2 ],
            [ 9, 7, 4, 2, 1, 5, 6, 3, 8 ],
            [ 5, 2, 8, 6, 3, 9, 4, 1, 7 ] ]
  """one thread to check if all cells in range, one to check rows, one to check cols, 9 to check subgrids"""
  
  
  if (isValidSudoku(board)):
    print("Valid")
  else:
    print("Not Valid")