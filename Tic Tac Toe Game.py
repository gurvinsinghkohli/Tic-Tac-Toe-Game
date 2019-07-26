#!/usr/bin/env python
# coding: utf-8

# In[8]:


def display_board(board):
    print(board[0] + "  " + board[1] + "  " + board[2])
    print(board[3] + "  " + board[4] + "  " + board[5])
    print(board[6] + "  " + board[7] + "  " + board[8])


# In[15]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[2]:


def player_input():
    marker = ""
    while not (marker.upper() == "X" or marker.upper() == "O"):
        marker = input("Please pick a marker 'X' or 'O' - player1")
    if(marker.upper() == "X"):
        return("X","O")
    if(marker.upper() == "O"):
        return("O","X")


# In[ ]:


player_input()


# In[6]:


def place_marker(board, marker, position):
    if(position <= 8 or position >= 0):
        board[position] = marker


# In[ ]:


place_marker(test_board,'X',0)
display_board(test_board)


# In[5]:


def win_check(board, mark):
    if(board[0] == board[1] == board[2] == mark):
        return True
    elif(board[3] == board[4] == board[5] == mark):
        return True
    elif(board[6] == board[7] == board[8] == mark):
        return True
    elif(board[0] == board[3] == board[6]== mark):
        return True
    elif(board[1] == board[4] == board[7] == mark):
        return True
    elif(board[2] == board[5] == board[8] == mark):
        return True
    elif(board[0] == board[4] == board[8] == mark):
        return True
    elif(board[2] == board[4] == board[6] == mark):
        return True
    else:
        return False


# In[ ]:


win_check(test_board,'X')


# In[4]:


import random
def choose_first():
    randNumber = random.randint(0,1)
    if(randNumber == 0):
        return "player1"
    elif(randNumber == 1):
        return "player2"


# In[ ]:


choose_first()


# In[15]:


def space_check(board, position):
    
    return board[position] == ' '


# In[16]:


def full_board_check(board):
    for x in range(1,10):
        if space_check(board,x):
            return False
    return True


# In[17]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[ ]:





# In[18]:


def replay():
    ques = input("Do you want to play again, Enter Yes or No?")
    if(ques.upper() == "YES"):
        return True
    elif(ques.upper() == "NO"):
        return False


# In[12]:


replay()


# In[19]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:




