import tictactoefuncs as ttt

# MAIN CODE -------------


valid = False

score = ttt.read_txt()

player = 'O'
cpu = 'X'

cont = 'y'
while cont == 'y':
  
  board = ttt.get_board()
  winner = 'N'
  free_slot = True
  
  while(winner == 'N' and free_slot == True):
    
    while(valid == False): # player's choice
      ttt.os.system("clear")
      ttt.print_score(score)
      num = ttt.get_num(board)
      valid = ttt.validate_pos(board, num)
      
      if(valid == False):
        print("\n| X | Incorrect value, try again! | X |\n")
        ttt.time.sleep(1.4)
        
    valid = False
    board = ttt.update_board(board, num, player)
  
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
    score["playerScore"] = int(score["playerScore"]) + 1
  elif winner == cpu:
    print("\n--- YOU LOSE! ---")
    score["cpuScore"] = int(score["cpuScore"]) + 1
  else:
    print("\n--- IT'S A DRAW ---")
  
  ttt.update_txt(score)

  cont = input("Do you want to keep playing ('y/n')")