import piece,time,os
from colorama import Fore

class board():
    board = []
    def __init__(self):
        self.board=[] #Creating the null board
        b="B" #Making the atributions easier
        w="W"
        self.board=[[piece.Rook(b),piece.Knight(b),piece.Bishop(b),piece.Queen(b),piece.King(b),piece.Bishop(b),piece.Knight(b),piece.Rook(b)]] #Atributing the first row
        row = []
        row2=[]
        for i in range(8): #Creating the pawn rows
            row.append(piece.pawn(b))
            row2.append(piece.pawn(w))

        self.board.append(row) #Appending the black pawn row
        
        for i in range(4): #Null spaces
            self.board.append([])
            for j in range(8):
                self.board[-1].append('-')
        self.board.append(row2) #Appending the white pawn row

        self.board.append([piece.Rook(w),piece.Knight(w),piece.Bishop(w),piece.Queen(w),piece.King(w),piece.Bishop(w),piece.Knight(w),piece.Rook(w)]) #Creating the last row 

    def print_board(self): #Create a Static method when using
        for i in self.board:
            print("")

            for j in i:
                if (j=='-'): print(Fore.BLUE,"  -    ",end='')
                else:
                    if(j.get_color()=="Black"): print(Fore.BLACK,j.get_name(),(6-len(j.get_name()))*" ",end='')
                    else: print(Fore.WHITE,j.get_name(),(6-len(j.get_name()))*" ",end='')
        print()
    
    
    def move(self,beg,end):
        Beg_row=beg[0]
        Beg_col=beg[1]
        End_row=end[0]
        End_col=end[1]
        try: #Checking for Out of index exceptions and if the user is trying to move a black space
            
            if(self.board[End_row][End_col] != "-"): #If the destination has a piece in it, a take will be avaluated 
                
                valid_take=self.board[Beg_row][Beg_col].take(beg,end,self.board[End_row][End_col],self.board) #Avaluate the take in the "Piece" Class
                
                if(valid_take): #If the take was valid, exclude the foe's piece
                    self.board[End_row][End_col]=self.board[Beg_row][Beg_col]
                    self.board[Beg_row][Beg_col] = '-'
                else: return False #If the take was invalid (the piece at the end has the same color as the piece at the beg) the move doesn't happen
            
            if(self.board[Beg_row][Beg_col] == '-'):return False
        except IndexError:
            return False
        valid = self.board[Beg_row][Beg_col].move(beg,end,self.board) # If all of the validantions above passed, the attempt to move occurs
        if (valid):self.board[Beg_row][Beg_col],self.board[End_row][End_col]=self.board[End_row][End_col],self.board[Beg_row][Beg_col] #Move valid
        else: print("Invalid move") #Move invalid


B = board()
j=0
for i in range(5):
    if (i== 4) : j=1
    B.move([i+1,0],[i+2,j])
    B.print_board()
    time.sleep(0.5)
    os.system("clear")


B.move([0,0],[6,0])
B.print_board()
time.sleep(0.5)
os.system("clear")
B.move([6,0],[6,1])
B.print_board()
time.sleep(0.5)
os.system("clear")
B.move([6,0],[6,3])
B.print_board()
time.sleep(0.5)
os.system("clear")
B.move([6,0],[5,5])
B.print_board()
time.sleep(0.5)
os.system("clear")
B.move([6,0],[5,0])
B.print_board()
time.sleep(0.5)
os.system("clear")
B.move([5,0],[5,6])
B.print_board()
time.sleep(0.5)
os.system("clear")
B.move([6,7],[5,6])
B.print_board()
time.sleep(0.5)
os.system("clear")
B.move([7,0],[6,0])
B.print_board()
time.sleep(0.5)
os.system("clear")
B.move([6,0],[6,1])
B.print_board()
time.sleep(0.5)