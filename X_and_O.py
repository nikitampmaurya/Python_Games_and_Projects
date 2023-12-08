import numpy
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']]) #for creating 3x3 board
p1s='X' #for storing symbol X for player 1
p2s='O' #for storing symbol O for player 2
print("Welcome here, Let's play X and O")

def check_rows(symbol): #to check if any player has won or not by checking each position
    for r in range(3): #since board has 3 rows
        count=0        #for controlling and tracking the repeatition 
        for c in range(3): #since board has 3 colmuns 
            if board[r][c]==symbol:   
                count=count+1       #if place gets fill, add 1
        if count==3:                #if count becomes 3 then announce the winner
            print(symbol,"Won")
            return True
    return False
def check_cols(symbol): #follow explanation of check_rows
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3: 
            print(symbol,"Won")
            return True
    return False  
def check_diagonals(symbol): #for checking if any player have won the game by any diagonals 
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol: #for diagonal extending from bottom left to top right
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol: #for diagonal extending from top right to bottom left
        print(symbol,'won')
        return True
    return False
def won(symbol): #to check all together if any player has won 
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)
    
def place(symbol): #ask players for input by specificing their chosen row and column
    print(numpy.matrix(board))
    while (1):
        row=int(input('Enter your row position 1 or 2 or 3: '))
        col=int(input('Enter your column position 1 or 2 or 3: '))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=="_": #to break input is invalid/absurd
            break
        else:
            print("Not valid input, Please enter again")
    board[row-1][col-1]=symbol #if input passes all the condition and then symbol is added to the place 
def play():   #for managing the game loop and turns of each player 
    for turn in range(9):
        if (turn%2==0): #for even number it is X's turn to play
            print("It is X turn")
            place(p1s)
            if won(p1s):
                break
        else: #for odd number it is O's turn to play
            print("It is O turn")
            place(p2s)
            if won(p2s):
                break
                
    if not (won(p1s)) and not (won(p2s)):
        print("Draw")
play()