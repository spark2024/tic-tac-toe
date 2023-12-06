class TicTacToe:
  def __init__(self):
      self.board = []

  # For creating the Board
  def create_board(self):
      for i in range(3):
          row = []
          for j in range(3):
              row.append("-")
          self.board.append(row)
      # For Printing the Board
      for row in self.board:
          for item in row:
              print(item, end=" ")
          print()

  # To show the view of boards
  def show_board(self):
      for i in self.board:
          for j in i:
              print(j, end=" ")
          print()

  # Fixing the spot
  def fix_spot(self, row, col, player):
      self.board[row - 1][col - 1] = player

  # To check Whether the player is won or not
  def is_player_won(self, player):
      n = len(self.board)
      # For checking rows
      for i in range(n):
          win = all(cell == player for cell in self.board[i])
          if win:
              return True

      # For checking columns
      for i in range(n):
          win = all(self.board[j][i] == player for j in range(n))
          if win:
              return True

      # For checking left-to-right diagonal
      win = all(self.board[i][i] == player for i in range(n))
      if win:
          return True

      # For checking right-to-left diagonal
      win = all(self.board[i][n - i - 1] == player for i in range(n))
      if win:
          return True
      return False

  # Checking whether the match is draw or not
  def is_match_draw(self):
      for row in self.board:
          for item in row:
              if item == '-':
                  return False
      return True

  def is_not_filled(self, row, col):
      if self.board[row - 1][col - 1] == '-':
          return True
      return False

  def is_turn(self, player1, player2, player):
      return player1 if player == 'X' else player2

  def start(self):
      player1 = input("Enter Player1 name: ")
      player2 = input("Enter Player2 name: ")
      self.create_board()
      player = 'X'

      while True:
          name = self.is_turn(player1, player2, player)
          print("Player", name, "turn")
          # self.show_board()
          row, col = [int(x) for x in input("Enter row and column number to fix spot: ").split()]
          if self.is_not_filled(row, col):
              self.fix_spot(row, col, player)
              self.show_board()
              won = self.is_player_won(player)
              if won:
                  if player == 'X':
                      print(player1, "Won.")
                  elif player == 'O':
                      print(player2, "Won.")
                  break
              player = 'X' if player == 'O' else 'O'
              if self.is_match_draw():
                  print("Match Draw..!")
                  break
          else:
              print("Oops... this position already occupied.\nAgain", end=" ")


tic_tac_toe = TicTacToe()
tic_tac_toe.start()
