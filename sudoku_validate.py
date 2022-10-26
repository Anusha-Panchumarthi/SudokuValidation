from concurrent.futures import thread
import threading
import colorama
import pyfiglet
import sys, time, os
from colorama import init, Fore, Back, Style

init(convert=True)
def checkRow(board, row):
    check = [False for _ in range(10)]
    for i in range(9):
            if check[board[row][i]] is False:
                  check[board[row][i]] = True
            else:
                  print(Fore.RED + f"Error in row {row}")
                  return False
    print(Fore.GREEN + f"Row {row} valid")
    return True

def checkCol(board, col):
    check = [False for _ in range(10)]
    for i in range(9):
            if check[board[i][col]] is False:
                  check[board[i][col]] = True
            else:
                  print(Fore.RED + f"Error in column {col}")
                  return False
    print(Fore.GREEN + f"Column {col} valid")
    return True

def printGrid(board, x, y):
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(f"{board[x+i][y+j]}", end = " ")
            else:
                print(f"{board[x+i][y+j]}")

def checkSubgrid(board, x, y):
    print(Fore.WHITE + "Checking subgrid ")
    printGrid(board, x, y)
    
    check = [False for _ in range(10)]
    for i in range(3):
            for j in range(3):
                  if check[board[x+i][y+j]] is False:
                        check[board[x+i][y+j]] = True
                  else:
                        print(Fore.RED + "Error in subgrid")
                        print("\n")
                        return False
    print(Fore.GREEN + "Subgrid valid")      
    print("\n")
    return True
def animee(messsage):
    for char in messsage:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

if __name__ == "__main__":

    result = pyfiglet.figlet_format("Sudoku Validator", font = "slant" )
    print(Fore.LIGHTMAGENTA_EX + result)
    print(Fore.WHITE)
    message = "Welcome to the Sudoku Validator!\nThe purpose of this application is to validate a solved sudoku board and check whether the solution is correct."
    animee(message)
    print("\n")
  #  while op!=3:

    board = []
    """board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 4, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    """

    print("Enter board : ")
    for i in range(9):
        print(f"Enter row {i+1}")   
        a = list(map(int, input().split()))
        board.append(a)

    print("\n")
    res = pyfiglet.figlet_format("Board")#, font = "bubble" )
    print(Fore.CYAN+ res)
    print(Fore.WHITE + "------------------------------------")
    for i in range(len(board)): 
    # print("\t\t")
        for j in range(len(board[i])):
            if j == 0:
                print(f"|  {board[i][j]} ", end=" ")
            elif j == 8:
                print(f"{board[i][j]}  |",)
            elif j%3 == 0:
                print(f"|  {board[i][j]} ", end=" ") 
            else:
                print(f"{board[i][j]} ", end = " ")
            #print("\n")
        if i==2 or i == 5 or i==8:
            print("------------------------------------")
    print("\n")

    flag = False
    res1 = pyfiglet.figlet_format("Validation")#, font = "bubble" )
    print(Fore.CYAN+ res1)
    print(Fore.WHITE + "Checking range....")
    valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(board)):
        for j in board[i]:
            if j not in valid:
                print(Fore.RED + f"Value {j} out of range")
                quit()
     
    print(Fore.GREEN + "All values in range")
    print("\n")
    
    print(Fore.WHITE + "Checking rows....")
    for i in range(9):
        thrd = threading.Thread(target=checkRow, args=(board, i))
        thrd.start()
        thrd.join()
    print("\n")

    print(Fore.WHITE + "Checking columns....")
    for i in range(9):
        thrd = threading.Thread(target=checkCol, args=(board, i))
        thrd.start()
        thrd.join()
    print("\n")

    print(Fore.WHITE + "Checking subgrids....")
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            thrd = threading.Thread(target=checkSubgrid, args=(board, i, j))
            thrd.start()
            thrd.join()
    print("\n")

    res2 = pyfiglet.figlet_format("Exiting")#, font = "3-d" )
    print(Fore.RED + Style.DIM + res2)
    quit()
       


"""  5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9"""

"""  5 3 4 6 7 8 9 1 2
6 7 2 1 7 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
2 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 6 6 1 7 9"""

    

    
        
    