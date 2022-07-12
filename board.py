class Board:
      def __init__(self):
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            self.winner = ""
      def get_size(self):
            return self.size
      def get_winner(self):
            return self.sign     
      def set(self, cell, sign):
            row = int(cell[1])
            col = cell[0].upper()
            if (col == "A"):
                   if (row == 1):
                          self.board[0] = sign
                   elif (row == 2):
                          self.board[3] = sign
                   else:
                          self.board[6] = sign
            elif (col == "B"):
                   if (row == 1):
                          self.board[1] = sign
                   elif (row == 2):
                          self.board[4] = sign
                   else:
                          self.board[7] = sign
            else:
                   if (row == 1):
                          self.board[2] = sign
                   elif (row == 2):
                          self.board[5] = sign
                   else:
                          self.board[8] = sign
      def isempty(self, cell):
             row = int(cell[1])
             col = cell[0].upper()
             if (col == "A"):
                   if (row == 1 and self.board[0] == " "):
                          return True
                   elif (row == 2 and self.board[3] == " "):
                          return True
                   elif (row == 3 and self.board[6] == " "):
                          return True
             elif (col == "B"):
                   if (row == 1 and self.board[1] == " "):
                          return True
                   elif (row == 2 and self.board[4] == " "):
                          return True
                   elif (row == 3 and self.board[7] == " "):
                          return True
             elif (col == "C"):
                   if (row == 1 and self.board[2] == " "):
                          return True
                   elif (row == 2 and self.board[5] == " "):
                          return True
                   elif (row == 3 and self.board[8] == " "):
                          return True
             else:
                    return False
      def isdone(self):
            done = False
            if (self.board[0] == "X" and self.board[1] == "X" and self.board[2] == "X"):
                done = True
                self.sign = "X"
            elif (self.board[3] == "X" and self.board[4] == "X" and self.board[5] == "X"):
                done = True
                self.sign = "X"
            elif (self.board[6] == "X" and self.board[7] == "X" and self.board[8] == "X"):
                done = True
                self.sign = "X"
            elif (self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X"):
                done = True
                self.sign = "X"
            elif (self.board[2] == "X" and self.board [4] == "X" and self.board[6] == "X"):
                done = True
                self.sign = "X"
            elif (self.board[0] == "X" and self.board [3] == "X" and self.board[6] == "X"):
                done = True
                self.sign = "X"
            elif (self.board[1] == "X" and self.board [4] == "X" and self.board[7] == "X"):
                done = True
                self.sign = "X"
            elif (self.board[2] == "X" and self.board [5] == "X" and self.board[8] == "X"):
                done = True
                self.sign = "X"
            elif (self.board[0] == "O" and self.board[1] == "O" and self.board[2] == "O"):
                done = True
                self.sign = "O"
            elif (self.board[3] == "O" and self.board[4] == "O" and self.board[5] == "O"):
                done = True
                self.sign = "O"
            elif (self.board[6] == "O" and self.board[7] == "O" and self.board[8] == "O"):
                done = True
                self.sign = "O"
            elif (self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O"):
                done = True
                self.sign = "O"
            elif (self.board[2] == "O" and self.board [4] == "O" and self.board[6] == "O"):
                done = True
                self.sign = "O"
            elif (self.board[0] == "O" and self.board [3] == "O" and self.board[6] == "O"):
                done = True
                self.sign = "O"
            elif (self.board[1] == "O" and self.board [4] == "O" and self.board[7] == "O"):
                done = True
                self.sign = "O"
            elif (self.board[2] == "O" and self.board [5] == "O" and self.board[8] == "O"):
                done = True
                self.sign = "O"
            else:
                count = 0
                for i in self.board:
                      if (i != " "):
                            count+=1
                if (count == 9):
                      done = True
            return done
      def show(self):
            print("   A   B   C ")
            print(" +---+---+---+")
            print("1| " + self.board[0] +" | "+ self.board[1] +" | "+ self.board[2] +" | ")
            print(" +---+---+---+")
            print("2| " + self.board[3] +" | "+ self.board[4] +" | "+ self.board[5] +" | ")
            print(" +---+---+---+")
            print("3| " + self.board[6] +" | "+ self.board[7] +" | "+ self.board[8] +" | ")
            print(" +---+---+---+")
