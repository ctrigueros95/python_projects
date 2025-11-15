# Make the game tic-tac-toe 

player1 = "X"

player2 = "O"

row1 = [" "," "," "]

row2 = [" "," "," "]

row3 = [" "," "," "]


# Define player turn

# Select a row

# Select a space

# Place X or O on the chosen spot.


row_num = input("Please select a row: ")

row_space = int(input("Please select a space: "))

if row_num == row1 and row_space == 1:
    row1 = row1[1-1]
    
print(row1)
