# Tic-Tac-Toe project for Milestone 1

########################
# FUNCTIONS START HERE #
########################

# Function that can be used to create the game board.
def print_board(x):
    print("     |     |     ")
    print("  " + str(x[6]) + "  |  " + str(x[7]) + "  |  " + str(x[8]) + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + str(x[3]) + "  |  " + str(x[4]) + "  |  " + str(x[5]) + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + str(x[0]) + "  |  " + str(x[1]) + "  |  " + str(x[2]) + "  ")
    print("     |     |     ")
    

# Function that checks if player has won.
def win_check(x):
    if (( x[0] == x[1] == x[2] ) or
        ( x[3] == x[4] == x[5] ) or
        ( x[6] == x[7] == x[8] ) or
        ( x[0] == x[3] == x[6] ) or
        ( x[1] == x[4] == x[7] ) or
        ( x[2] == x[5] == x[8] ) or
        ( x[0] == x[4] == x[8] ) or
        ( x[2] == x[4] == x[6] )):
        print(f"Congrats! {current_player} wins!")
        return True


# Asks the user if they want to play another game.
def replay():
    print("Would you like to play another game of Tic-Tac-Toe?\n")
    choice = input("Enter [Y] or [N] >> ").upper()
    
    while True:
        if choice == "Y":
            break
        elif choice == "N":
            break
        else:
            choice = input("Invalid selection. Please choose [Y] or [N]. >> ").upper()
            

    if choice == "N":
        return False
    else:
        return True

######################
# FUNCTIONS END HERE #
######################

##########################
# GAME LOGIC STARTS HERE #
##########################

# Boolean for main while loop.
playing = True
# Boolean for while loop for individual game.
game_on = True

print("Welcome to Tic-Tac-Toe!\n")

# Loop for playing the game.
while playing:

    # List for numbering each square on the board
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_board(board)
    print("\n")

    # Get player names.
    player_one_name = input("Player One, what is your name? >> ")
    player_two_name = input("Player Two, what is your name? >> ")
    
    # Variables to remember which player is X/O.
    player_two_token = ""
    player_one_token = input(f"{player_one_name}, would you like to be X's or O's? >> ").upper()
    if player_one_token == "X":
        player_two_token = "O"
    else:
        player_two_token = "X"

    # Variable that will keep track of the current player.  Starts with Player 1.
    current_player = player_one_name

    # Loop for current game.
    while game_on:

        choice = int(input(f"{current_player}, select a number. >> "))
        while True:
            if board[choice - 1] == "X" or board[choice - 1] == "O":
                print("Square is already taken. Please choose another square.\n")
                choice = int(input(f"{current_player}, select a number. >> "))
            else:
                break

        if current_player == player_one_name:
            board[choice - 1] = player_one_token
        elif current_player == player_two_name:
            board[choice - 1] = player_two_token

        print_board(board)

        if win_check(board):
            break

        if current_player == player_one_name:
            current_player = player_two_name
        elif current_player == player_two_name:
            current_player = player_one_name

    if not replay():
        print("GAME OVER")
        break

########################
# GAME LOGIC ENDS HERE #
########################
