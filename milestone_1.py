#1 the board
def display_board(board):  
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- - -')
    print(board[7]+'|'+board[8]+'|'+board[9])

#2 decide the marker
def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
    
    player1 = marker
    
    if player1 == 'X':player2 = 'O'
    else:
        player2 ='X'
    
    print('player1 = ' + player1, 'player2 = ' + player2)
    return player1, player2

#3 decide the position    
def place_marker(board, marker, position):
    board[position] = marker
    #draw the mark on the blank

#check if the player wins   
def win_check(board, marker):
    if board[1] == marker and board[2] == marker and board[3] == marker:
        return True
    elif board[4] == marker and board[5] == marker and board[6] == marker:
        return True
    elif board[7] == marker and board[8] == marker and board[9] == marker:
        return True
    elif board[1] == marker and board[5] == marker and board[9] == marker:
        return True
    elif board[1] == marker and board[4] == marker and board[7] == marker:
        return True
    elif board[2] == marker and board[5] == marker and board[8] == marker:
        return True
    elif board[3] == marker and board[6] == marker and board[9] == marker:
        return True
    elif board[3] == marker and board[5] == marker and board[7] == marker:
        return True
    else:
        return False

#decide the turn
import random
def choose_first():
    if random.randint(1,2) == 2:
        print('Player 2 goes first')
        return 'player2'
    else:
        print('Player 1 goes first')
        return 'player1'

#check if the space is blank, applies to the player_choice function
def space_check(board, position):
    return board[position] == ' '

#check if the baord is full, applies to the player_choice function
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#check whether the number is correct and whether the position is blank     
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Please enter number from 1 to 9: '))
        except:
            continue
        
    return position
    

def replay():
    return input('To replay, enter Yes or No: ').lower().startswith('y')






print('Let us play Tic Tac Toe!')

while True:
    player1_marker, player2_marker = player_input()
    theboard = [' '] * 10
    turn = choose_first() 
    play = input('Do you want to start the game? Yes or No: ')

    #chech if the player would like to start
    if play.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on == True:
        if turn == 'player1':
            display_board(theboard) #show the board
            position = player_choice(theboard) #input the position
            place_marker(theboard, player1_marker, position) #mark the position
            
            if win_check(theboard, player1_marker): #check if the player1 wins
                display_board(theboard)
                print('Congratulations player1 !')
                game_on = False
            
            else:
                #check if the board is full
                if full_board_check(theboard):
                    display_board(theboard)
                    print('Deuce')
                    break
                else:
                    turn = 'player2'
        
        if turn == 'player2':
            display_board(theboard) #show the board
            position = player_choice(theboard) #input the position
            place_marker(theboard, player2_marker, position) #place the marker
                
            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('Congratulations player2 !')
                game_on = False
                
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('Deuce')
                    break
                else:
                    turn = 'player1'


    if not replay():
        print('End of the game')
        break



                
               



        



       
    
        
