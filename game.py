# Import date and time module
from datetime import datetime

# Function to save game data to a file
def save_game_data(moves,result):
    with open("game_data_new.txt","a") as file:
        file.write(f"Date & Time:{datetime.now()}\n")
        file.write("Moves:\n")
        for i,move in enumerate(moves,1):
            file.write(f"{i}.{move}\n")
        file.write(f"Result:{result}\n")
        file.write("="*30+"\n")

# Welcome section of the game
def welcome():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O")
    print("Let's start the game :)\n")
    print("Board before the start of the game..")

# Initialize the Tic Tac Toe board
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Write all the winning combinations of the game
wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

# Change the dimension of the board(convert the 2-dimensional array to 1-dimensional array)
def dimension_change(arr):
    arr1=[j for i in arr for j in i]
    # print((arr1))
    return arr1

# Winning function
def winning(wins):
    changed_board=dimension_change(arr)
    for i in wins:
        if changed_board[i[0]]==changed_board[i[1]]==changed_board[i[2]]:
            print(f"Player{1 if changed_board[i[0]]=='X' else 2} wins:)")
            return 1

# Function to display the board
def board(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
            if j<len(arr[i])-1:
                print(" | ",end=" ")
        if i<len(arr)-1:
            print("\n-------------")
    print("\n")

# Function to handle player 1
def player1():
    pos=int(input("Player1-Enter position(1-9):"))
    # check if position is valid or not
    if 1<=pos<=9:
        # map position to first row
        if pos <= 3:
            if arr[0][pos - 1] == "O" or arr[0][pos - 1]== "X":
                print("Invalid Position!Please enter again..")
                player1()
            else:
                # mark the respected position with X
                arr[0][pos - 1] = "X"
                return pos
        elif pos <= 6:
            if arr[1][pos - 4] == "O" or arr[1][pos - 4] == "X":
                print("Invalid Position!Please enter again..")
                player1()
            else:
                arr[1][pos - 4] = "X"
                return pos
        elif pos <= 9:
            if arr[2][pos - 7] == "O" or arr[2][pos - 7] == "X":
                print("Invalid Position!Please enter again..")
                player1()
            else:
                arr[2][pos - 7] = "X"
                return pos
    else:
        print("Please enter between 1-9")
        player1()



# Function to handle player 2
def player2():
    pos=int(input("Player2-Enter position(1-9):"))
    if 1<=pos<=9:
        if pos<=3:
            if arr[0][pos-1]=="X" or arr[0][pos - 1] == "O":
                print("Invalid Position!Please enter again..")
                player2()
            else:
                arr[0][pos-1]="O"
                return pos
        elif pos<=6:
            if arr[1][pos - 4] == "X" or arr[1][pos - 4] == "O":
                print("Invalid Position!Please enter again..")
                player2()
            else:
                arr[1][pos-4]="O"
                return pos
        elif pos<=9:
            if arr[2][pos - 7] == "X" or arr[2][pos - 7] == "O":
                print("Invalid Position!Please enter again..")
                player2()
            else:
                arr[2][pos-7]="O"
                return pos
    else:
        print("Please enter between 1-9")
        player2()


# Call functions to run the program
def play():
    welcome()
    board(arr)
    moves=[]  # List to store the sequence of moves
    j=0
    result="Draw"  # Default result is draw

    for i in range(5):
        move=player1()
        moves.append(f"Player 1: {move}")
        j+=1
        board(arr)
        win=winning(wins)
        if win:
            result="Player 1 Wins"
            break
        if j>=9:
            break

        move=player2()
        moves.append(f"Player 2: {move}")
        j+=1
        board(arr)
        win=winning(wins)
        if win:
            result="Player 2 Wins"
            break

    # Save game data
    save_game_data(moves,result)

    if result=="Draw":
        print("Match is drawn..")
    else:
        print(result)

# Start the game
play()