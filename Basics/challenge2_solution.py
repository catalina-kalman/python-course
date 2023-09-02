# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.
board_rows = 0
board_columns = 0
groups_to_check = []
def play_game():
  board = []
  global board_rows
  global board_columns
  while board == []:
    board_rows = int(input("Enter number of rows: "))
    board_columns = int(input("Enter number of column: "))
    if board_rows < 3 or board_columns < 3:
        print("Board needs to be at least 3x3")
        continue
    for x in range(board_rows):
      board.append([])
      for y in range(board_columns):
        board[x].append(".")
    get_groups_to_check()

#  board = [
#    [".", ".", "."],
#    [".", ".", "."],
#    [".", ".", "."]
#  ]

  player = "X"
  while not is_game_over(board):
    print(print_board(board))
    print("It's " + player + "'s turn.")
    # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    board, player = make_move(board, row, column, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")

def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

def make_move(board, row, column, player):
  if board[row][column] == ".":
    board[row][column] = player
  else:
    print("Position not available.")
    if player == "X":
      player = "O"
    else:
      player = "X"
  return board, player


# This function will extract three cells from the board
def get_cells(board, coord_1, coord_2, coord_3):
  return [
    board[coord_1[0]][coord_1[1]],
    board[coord_2[0]][coord_2[1]],
    board[coord_3[0]][coord_3[1]]
  ]

# This function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return "." not in cells

# This function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return cells[0] == cells[1] and cells[1] == cells[2]

# We'll make a list of groups to check:
def get_groups_to_check():
    for x in range(board_rows):
        for y in range(board_columns):
            if y+2 < board_columns:
                option1 = [(x,y), (x,y+1), (x,y+2)]
                groups_to_check.append(option1)
            if x+2 < board_rows:   
                option2 = [(x,y), (x+1,y), (x+2,y)]
                groups_to_check.append(option2)
            if y+2 < board_columns and x+2 < board_rows:
                option3 = [(x,y), (x+1,y+1), (x+2,y+2)]
                groups_to_check.append(option3)
            if y-2 >= 0 and x+2 < board_rows:
                option4 = [(x,y), (x+1,y-1), (x+2,y-2)]
                groups_to_check.append(option4)
            
'''
groups_to_check = [
  # Rows
  [(0, 0), (0, 1), (0, 2)],x
  [(1, 0), (1, 1), (1, 2)],x
  [(2, 0), (2, 1), (2, 2)],x
  # Columns
  [(0, 0), (1, 0), (2, 0)],x
  [(0, 1), (1, 1), (2, 1)],x
  [(0, 2), (1, 2), (2, 2)],x
  # Diagonals
  [(0, 0), (1, 1), (2, 2)],x
  [(0, 2), (1, 1), (2, 0)]
]
'''

def is_game_over(board):
  # We go through our groups
  for group in groups_to_check:
    # If any of them are empty, they're clearly not a
    # winning row, so we skip them.
    if is_group_complete(board, group[0], group[1], group[2]):
      if are_all_cells_the_same(board, group[0], group[1], group[2]):
        return True # We found a winning row!
        # Note that return also stops the function
  for board_row in board:
    if "." in board_row:
      return False # If we get here, we didn't find a winning row
  return True # If we get here, it is a draw

# And test it out:

print("Game time!")
play_game()