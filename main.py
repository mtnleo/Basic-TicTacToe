import os, random, time

board = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"]]

def print_board(board):
  for i in board:
    print(i)
    print("\n")

def detect_win(board): #returns "X", "O" or "N" depending on who won or not
  winner = 'N'
  
  # horizontal
  if("X" == board[0][0] and "X" == board[0][1] and "X" == board[0][2]):
    winner = 'X'
  elif("X" == board[1][0] and "X" == board[1][1] and "X" == board[1][2]):
    winner = 'X'
  elif("X" == board[2][0] and "X" == board[2][1] and "X" == board[2][2]):
    winner = 'X'
  else:
    if("O" == board[0][0] and "O" == board[0][1] and "O" == board[0][2]):
      winner = 'O'
    elif("O" == board[1][0] and "O" == board[1][1] and "O" == board[1][2]):
      winner = 'O'
    elif("O" == board[2][0] and "O" == board[2][1] and "O" == board[2][2]):
      winner = 'O'

  # vertical
  if("X" == board[0][0] and "X" == board[1][0] and "X" == board[2][0]):
    winner = 'X'
  elif("X" == board[0][1] and "X" == board[1][1] and "X" == board[2][1]):
    winner = 'X'
  elif("X" == board[0][2] and "X" == board[1][2] and "X" == board[2][2]):
    winner = 'X'
  else:
    if("O" == board[0][0] and "O" == board[1][0] and "O" == board[2][0]):
      winner = 'O'
    elif("O" == board[0][1] and "O" == board[1][1] and "O" == board[2][1]):
      winner = 'O'
    elif("O" == board[0][2] and "O" == board[1][2] and "O" == board[2][2]):
      winner = 'O'

  # diagon-alley ;)
  if("X" == board[0][0] and "X" == board[1][1] and "X" == board[2][2]):
    winner = 'X'
  elif("X" == board[0][2] and "X" == board[1][1] and "X" == board[2][0]):
    winner = 'X'
  else:
    if("O" == board[0][0] and "O" == board[1][1] and "O" == board[2][2]):
      winner = 'O'
    elif("O" == board[0][2] and "O" == board[1][1] and "O" == board[2][0]):
      winner = 'O'

  return winner

def get_num(board):
  os.system("clear")
  print_board(board)
  num = input("--- SELECT A NUMBER TO PLACE YOUR CHOICE ---\n")
  return num

def validate_pos(board, num):
  valid = False
  if(int(num) > 0 and int(num) < 10):
    for i in board:
      if num in i:
        valid = True

  return valid

def update_board(board, num, player):
  for i in board:
    if(num in i):
      pos = i.index(num)
      i[pos] = player

  return board

def cpu_choice(board):
  valid = False
  while valid == False:
    num = str(random.randint(1, 9))
    valid = validate_pos(board, num)

  return num

  
# MAIN CODE -------------

winner = 'N'
valid = False

player = 'O'
cpu = 'X'

while(winner == 'N'):
  while(valid == False):
    num = get_num(board)
    valid = validate_pos(board, num)
    if(valid == False):
      print("\n| X | Incorrect value, try again! | X |\n")
      time.sleep(1.4)
      
  valid = False
  board = update_board(board, num, player)

  num_cpu = cpu_choice(board)
  board = update_board(board, num_cpu, cpu)

  winner = detect_win(board)

os.system("clear")
print_board(board)

if(winner == player):
  print("\n--- CONGRATS! YOU WIN! ---\n")
else:
  print("\n--- YOU LOSE! ---")

  