class piece():
    def __init__(self,color):
        if(color == 'B' or color =="W"):
            self.color=color
        else:
            print("Invalid Color piece")
            
    def get_color(self):
        if(self.color == "W"): return "White"
        else: return "Black"

    def get_name(self):
        return self.name
    
    def move(self,beg,end,board):
        pass


class pawn(piece):
    def __init__(self,color):
        super().__init__(color)
        self.name = "Pawn"
          
    def move(self,beg,end,board):

        if (self.color == 'B'): #Validanting in case a black pawn is moving
            if(beg[0]-end[0] == -1 and beg[1]==end[1]):  return True
            elif(beg[0]==1):
                if(beg[0]-end[0] == -2 and beg[1]==end[1] and board[beg[0]+1][beg[1]]=="-"):  return True
            else: return False
        else: #Validating in case a white pawn is moving
            if(beg[0]-end[0] == 1 and beg[1]==end[1]):  return True
            elif(beg[0]==6):
                if(beg[0]-end[0] == 2 and beg[1]==end[1] and board[beg[0]-1][beg[1]]=="-"):  return True
            else: return False


    def take(self,beg,end,piece,board): #If a take is happening, validate it 
        if(piece.get_color() == self.color or piece =="-"):return False
        else:
            if (self.color == 'B'):
                if(beg[0]-end[0] == -1 and abs(beg[1]-end[1])==1):  return True
                else: return False
            else:
                if(beg[0]-end[0] == 1 and abs(beg[1]-end[1])==1):  return True
                else: return False

class Rook(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Rook"

    def move(self,beg,end,board): 
        if (beg[0]==end[0] and beg[1]!= end[1]): #Moving in column
            for i in range(1,abs(beg[1]-end[1])):
                if(board[beg[0]][beg[1]+i] != '-'): return False
            return True
        
        elif (beg[0]!=end[0] and beg[1] == end[1]): #Moving in row
            for i in range(1,abs(beg[0]-end[0])):
                if(board[beg[0]+i][beg[1]] != '-'): return False
            return True
        else: return False

    def take(self,beg,end,piece,board):

        if(self.move(beg,end,board)): # Check if the piece can move throught the board 
            if(piece.get_color() == self.get_color()): return False
            else: return True
        else: return False
        

class Knight(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Knight"

    def move(self,beg,end,board):
        if(abs(beg[0]-end[0])==1 and abs(beg[1]-end[1])==2): return True
        elif(abs(beg[0]-end[0])==2 and abs(beg[1]-end[1])==1): return True
        else:return False

    def take(self,beg,end,piece,board):
        if(self.move(beg,end,board)): #Check if the piece can move throught the board
            if(piece.get_color() == self.get_color()): return False
            else: return True
        else:return False        
class Bishop(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Bishop"

class Queen(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Queen"

class King(piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "King"
