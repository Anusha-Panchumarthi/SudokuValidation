import pygame

run = True
dif = 400/9
line_black = (0, 0, 0)
x, y = 0, 0
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("SUDOKU VALIDATOR")
font = pygame.font.SysFont('comicsans', 15)
font1 = pygame.font.SysFont('comicsans', 25)

def draw_grid(board):
      screen.fill((255, 255, 255))
      for i in range(10):
          thick = 1
          if i % 3 == 0 :
              thick = 4
          else:
              thick = 1
          pygame.draw.line(screen, line_black, (100, i * dif + 100), (500, i * dif + 100), thick)
          pygame.draw.line(screen, line_black, (i * dif + 100, 100), (i * dif + 100, 500), thick)

      for i in range(9):
            for j in range(9):
                  num = font.render(str(board[i][j]), 1, line_black)
                  screen.blit(num, (i*dif + 118, j*dif + 115))
      

def inRange(board):
  for i in range(9):
   for j in range(9):
      if board[i][j] > 9 or board[i][j] < 1:
          return False
  
  return True

def checkRow(board, row):
     check = [ 0 for k in range(10)]
     for i in range(9):
            num = board[row][i]
            if(i==0):
                  check[num] = 1
            else :
                  if(check[num] == 1):
                        return False
                  else:
                        check[num]=1

def checkCol(board, col):
     check = [ 0 for k in range(10)]
     for i in range(9):
            num = board[i][col]
            if(i==0):
                  check[num] = 1
            else :
                  if(check[num] == 1):
                        return False
                  else:
                        check[num]=1
     return True               
if __name__ == "__main__":
      
      board = [ [ 7, 9, 2, 1, 5, 4, 3, 8, 6 ],
            [ 6, 4, 3, 8, 2, 7, 1, 5, 9 ],
            [ 8, 5, 1, 3, 9, 6, 7, 2, 4 ],
            [ 2, 6, 5, 9, 7, 3, 8, 4, 1 ],
            [ 4, 8, 9, 5, 6, 1, 2, 7, 3 ],
            [ 3, 1, 7, 4, 8, 2, 9, 6, 5 ],
            [ 1, 3, 6, 7, 4, 8, 5, 9, 2 ],
            [ 9, 7, 4, 2, 1, 5, 6, 3, 8 ],
            [ 5, 2, 8, 6, 3, 9, 4, 1, 7 ] ]

      while run:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False
          draw_grid(board)
          flag = 0;
          if not inRange(board):
                txt = font1.render("INVALID NUMBER", 1, (255, 0, 0))
                screen.blit(txt, (200, 550))
          else:
                  for i in range(9):
                        flag = 0
                        if not checkRow(board,i):
                              txt = font1.render("Incorrect input for row at :", 1, (255, 0, 0))
                              a = font1.render(str(i), 1, (255, 0, 0))
                              screen.blit(txt, (200, 550))
                              screen.blit(a, (410, 550))
                              flag = 1
                              break
                        if not checkCol(board,i):
                              txt = font1.render("Incorrect input for col at :", 1, (255, 0, 0))
                              a = font1.render(str(i), 1, (255, 0, 0))
                              screen.blit(txt, (200, 550))
                              screen.blit(a, (410, 550))
                              flag = 1
                              break
                        if not checkGrid
                  if(flag):
                        print("help")
                        #break
                  else :
                        txt = font1.render("VALID", 1, (255, 0, 0))
                        screen.blit(txt, (200, 550))
                        #else: 
                              #txt = font1.render("VALID", 1, (255, 0, 0))
                              #screen.blit(txt, (200, 550))
          
          pygame.display.update()


#def checkGrid()
"""
#def isValidSudoku(board):
if __name__ == '__main__':
   
  
  one thread to check if all cells in range, one to check rows, one to check cols, 9 to check subgrids
  
  if (isValidSudoku(board)):
    print("Valid")
  else:
    print("Not Valid") """
