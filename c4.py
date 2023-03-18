board = [['  ','  ','  ','  ','  ','  ','  '],
         ['  ','  ','  ','  ','  ','  ','  '],
         ['  ','  ','  ','  ','  ','  ','  '],
         ['  ','  ','  ','  ','  ','  ','  '],
         ['  ','  ','  ','  ','  ','  ','  '],
         ['  ','  ','  ','  ','  ','  ','  ']]

def print_board(board):
    for row in board:
        print(row)
    print("")

print_board(board)

def make_move(col, player,board):
    row = 6
    col = int(col)
    while True:
        if row == 0:
            return board, False
        
        # checks if spot is not empty
        if board[row-1][col] != "  ": # its row - 1 to account for list index starting from 0
            #move up to next row
            row = row - 1
        else:
            board[row-1][col] = player
            
            return board, True
        
def check_win(board):
    #vertical
    #this is the number of 4 combinations that can happen in each coloumn
    height = 3 - 1 #minus one to account for list index starting from 0, doesnt need to be variable can use loop instead
    print("checking...")
    # checks starting bottom most
    for j in range(3):
        #checks every column
        for i in range(7):
            if board[3+height][i] != "  " and board[3+height][i] == board[2+height][i] and board[2+height][i] == board[1+height][i] and board[1+height][i] == board[height][i]:
                return True, f"player{board[3+height][i]} has won"
        height -= 1

    # horizontal
    width = 4 - 1 # same concept as vertical check
    #checks starting right most
    for j in range(4):
        for i in range(6):
            if board[i][3+width] != "  " and board[i][3+width] == board[i][2+width] and board[i][2+width] == board[i][1+width] and board[i][1+width] == board[i][width]:
                return True, f"player{board[i][3+width]} has won"
        width -= 1
    # diagonal check
    #   x
    #  x
    # x
    #x
    #
    #3,0 2,1 1,2 0,3 goes along for 4 combinations [][changes]
    #4,0 3,1 2,2 1,3 goes along for 4 combinations [][changes]
    #5,0 4,1 3,2 ,2,3 goes along for 4 combinations [][changes]
    for i in range(3):
        for j in range(4):
            if board[3+i][j] != "  " and board[3+i][j] == board[3+i-1][j+1] and board[3+i-1][j+1] == board[3+i-2][j+2] and board[3+i-2][j+2] == board[3+i-3][j+3]:
                
                return True, f"player{board[3+i][j]} has won"
    #opposite diagonal
    for i in range(3):
        for j in range(6,3,-1):
            if board[5-i][j] != "  " and board[5-i][j] == board[5-i-1][j-1] and board[5-i-1][j-1] == board[5-i-2][j-2] and board[5-i-2][j-2] == board[5-i-3][j-3]:
                
                return True, f"player{board[5-i][j]} has won"
            

    for i in range(3):
        pass
    #no win found, check if full (42 pieces), nevermind only need to check top row
    pieces = 0
    for i in range(7):
        if board[0][i] == "  ":
            print(i,"this")
            break
        else:
            pieces +=1

    if pieces == 7:
        return "", "Draw"

    return False, ""


move_num = 0
while True:
    user = input()
    
    if user == "/":
        break
    if move_num % 2 == 0:
        board, msg = make_move(user,"🟡",board)
        move_num += 1
    else:
        board, msg = make_move(user,"🔴",board)
        move_num += 1
    
    if msg == False:
        move_num -= 1
        print("column is full, move again")
    condition, msg = check_win(board)
    if condition == True:
        print_board(board)
        print(msg)
        break
    elif msg == "Draw":
        print_board(board)
        print(msg)
        break 
    print_board(board)

#Test play
# from random import randint

# ls2 = [num for num in range(7) for j in range(6)]
# print(ls2)
# move_num = 0
# #moves = [0,1,1,3,2,2,2,3,3,4,3,0]

# while loop for random games till draw 
# iterations = 0
# msg = ""
# while msg != "Draw":
#     iterations +=1
#     board = [['  ','  ','  ','  ','  ','  ','  '],
#             ['  ','  ','  ','  ','  ','  ','  '],
#             ['  ','  ','  ','  ','  ','  ','  '],
#             ['  ','  ','  ','  ','  ','  ','  '],
#             ['  ','  ','  ','  ','  ','  ','  '],
#             ['  ','  ','  ','  ','  ','  ','  ']]

# moves = [randint(0,6) for i in range(100)]
# for i in range(len(moves)):
#     user = moves[i]
#     print(i, user)
    
#     if user == "/":
#         break
#     if move_num % 2 == 0:
#         board, msg = make_move(user,"🟡",board)
#         move_num += 1
#     else:
#         board, msg = make_move(user,"🔴",board)
#         move_num += 1
    
#     if msg == False:
#         move_num -= 1
#         print("coloumn is full, move again")
#     condition, msg = check_win(board)
#     if condition == True:
#         print_board(board)
#         print(msg)
#         break
#     elif msg == "Draw":
#         print_board(board)
#         print(msg)
#         break
#     print_board(board)



# print(iterations)