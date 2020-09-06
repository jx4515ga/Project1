# Boris Paul Pizha
#Tic Tac Toe Game

# Table set up, the way it will look before game starts 
table = ["?","?","?",
         "?","?","?",
         "?","?","?"]

game_still_going = True

# No winners at the begginig of the game 
Winner = None

# This is 1/2 players 
current_player = "X"

# Dispalying the table set up above

def display_table():
    print (table[0] + " | " + table[1] + " | " + table[2])
    print (table[3] + " | " + table[4] + " | " + table[5])
    print (table[6] + " | " + table[7] + " | " + table[8])

# Game starts with one of the player's, in this case the first player is "x"
def play_game():

    display_table()

    while game_still_going:
        
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

# Either Win X or O, otherwise there will be a tie
    if Winner == "X" or Winner == "O":
        print ("Congrats! " + Winner + "  You won. ")
    elif Winner == None:
        print("Game Tie.")

# Handling player turns and select a range dorm 1 to 9 to choose a spot in the table
def handle_turn(player):

    print(player + "'s turn.'")
    position = input("Select a position bertween 1 - 9: ")
#
# Validating the entities to avoid selecting the same spot     
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalis input. Please try again. ")
    
        position = int(position) -1

        if table[position] == "?":
            valid = True
        else:
            print("Unfortunately this place is alreasy taken. . ")

    table[position] = player

    display_table()

# Checking if there is a winner or tie 
def check_if_game_over():
    check_for_winner()
    check_if_tie()

# There will be a winner (X or O)
# To win player need to get a row, column, or diagonal
# If neither get anything there won't be winners

def check_for_winner():
    global Winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonals_winner = check_diagonals()
    
    if row_winner:
        Winner = row_winner
    elif column_winner:
        Winner = column_winner
    elif diagonals_winner:
        Winner = diagonals_winner
    else:  
        Winner = None

    return

# Checking if any of the three rows were checked by the same player
def check_rows():
    global game_still_going

    row_1 = table[0] == table[1] == table[2] != "?"
    row_2 = table[3] == table[4] == table[5] != "?"
    row_3 = table[6] == table[7] == table[8] != "?"

    if row_1 or row_2 or row_3:

        game_still_going = False 

    if row_1:
        return table[0]
    elif row_2:
        return table[3]
    elif row_3:
        return table[6] 

    
    return

# Checking if any of the three Columns were checked by the same player
def check_columns():

    global game_still_going

    column_1 = table[0] == table[3] == table[6] != "?"
    column_2 = table[1] == table[4] == table[7] != "?"
    column_3 = table[2] == table[5] == table[8] != "?"

    if column_1 or column_2 or column_3:
        game_still_going = False 

    if column_1:
        return table[0]
    elif column_2:
        return table[1]
    elif column_3:
        return table[2]
    return

# checking if any of the two diagonals were checked by the same player 

def check_diagonals():
    global game_still_going

    diagonals_1 = table[0] == table[4] == table[8] != "?"
    diagonals_2 = table[6] == table[4] == table[2] != "?"
    

    if diagonals_1 or diagonals_2:
        game_still_going = False 

    if diagonals_1:
        return table[0]
    elif diagonals_2:
        return table[6]
    
    return

# There will be a game_over if the table is full and no winners exist 
def check_if_tie():
    global game_still_going

    if "?" not in table:
        game_still_going = False

    return

# Players getting turns to select a spot in the table. 
def flip_player():

    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return

play_game()

