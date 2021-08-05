#Create working tic tac toe
gui_board = [['_','_','_'],
             ['_','_','_'],
             ['_','_','_']]
o_turn = True


def game_ends(board):

  for r in board:
    if len(set(r)) == 1:
      if r[0] != '_':
        return True, f'{r[0]} is winner'
      else: 
        return False, ''
  if board[0][0] == board[1][1] == board[2][2]:
    if r[0] != '_':
      return True, f'{board[0][0]} is winner'
    else: 
      return False, ''
  elif board[2][0] == board[1][1] == board[0][2]:
    if r[0] != '_':
      return True, f'{board[0][2]} is winner'
    else:
      return False, ''
  else:
    return False, ''



#get possible moves
#compute utility
#implement minimax