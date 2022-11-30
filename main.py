import tictactoefuncs as ttt

# MAIN CODE -------------

winner = 'N'
valid = False

player = 'O'
cpu = 'X'
free_slot = True

while(winner == 'N' and free_slot == True):
  while(valid == False): # player's choice
    num = ttt.get_num(ttt.board)
    valid = ttt.validate_pos(ttt.board, num)
    if(valid == False):
      print("\n| X | Incorrect value, try again! | X |\n")
      ttt.time.sleep(1.4)
      
  valid = False
  board = ttt.update_board(ttt.board, num, player)

  # Checks if there's an available spot to place the player's choice
  free_slot = ttt.check_available_pos(board)
  
  if(free_slot): #if there's an available spot, CPU's choice
    num_cpu = ttt.cpu_choice(board)
    board = ttt.update_board(board, num_cpu, cpu)

    winner = ttt.detect_win(board)


ttt.os.system("clear")
ttt.print_board(board)

if(winner == player):
  print("\n--- CONGRATS! YOU WIN! ---\n")
elif winner == cpu:
  print("\n--- YOU LOSE! ---")
else:
  print("\n--- IT'S A DRAW ---")
