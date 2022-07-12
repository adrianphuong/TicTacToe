class Player:
      def __init__(self, name, sign):
            self.name = name
            self.sign = sign
      def get_sign(self):
            return self.sign
      def get_name(self):
            return self.name
      def choose(self, board):
            cellnum = input(self.name + ", " + self.sign +": Enter a cell [A-C][1-3]: \n")
            letters = ("A", "B", "C")
            nums = ("1","2","3")
            while True:
                  if (cellnum[0].upper() in letters and len(cellnum) == 2 and cellnum[1] in nums):
                        while True:         
                               if (board.isempty(cellnum)):
                                      board.set(cellnum,self.sign)
                                      break
                               else:
                                      print("You did not choose correctly.")
                                      cellnum = input(self.name + ", " + self.sign +": Enter a cell [A-C][1-3]: \n")
                        break
                  else:
                        print("You did not choose correctly.")
                        cellnum = input(self.name + ", " + self.sign +": Enter a cell [A-C][1-3]: \n")
