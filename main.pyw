import Board.Board as Board
import Board.Pieces as Pieces
from Tkinter import Button
from Board.Board import pprint
import Gui.gui as gui

class main:
    def __init__(self):
        #create board instance
        self.mainBoard = Board.init()
        self.gameover = False
        self.turn = 0
        #initiate gui
        self.gui_b = gui.GUIBoard(self.mainBoard.cols,self.mainBoard.rows,name="Latrin Culi")
        self.poss_move = []
        self.gui_b.b_canvas.bind("<Button-1>",self.get_click)
        #generate list of pieces
        self.PIECES = {}
        for row in self.mainBoard:
            for piece in row:
                if piece:
                    self.PIECES[piece] = self.gui_b.add_piece(piece.pos[1],piece.pos[0],piece.color+piece.type)
        #start it up!
        self.gui_b.mainloop()
    
    def get_click(self,click):
        x,y = click.x//self.gui_b.sidel,click.y//self.gui_b.sidel
        self.poss_move.append((x,y))
        if len(self.poss_move) == 2:
            #test to see if the move is in the legal moves of the piece (this part is very bracket)
            if self.poss_move[1] in self.mainBoard[self.poss_move[0][1]][self.poss_move[0][0]].legalMoves():
                self.movePiece(self.poss_move[0],self.poss_move[1])
                self.gui_b.del_hl_list()
                self.poss_move = []
            #test if user wants to cancel move
            else:
                self.gui_b.del_hl_list()
                self.poss_move = []
        #highlight possible moves on selected piece and check to make sure that selecting a non-empty square
        elif len(self.poss_move) == 1 and self.mainBoard[y][x]:
            if self.mainBoard[y][x].color == "b" and self.turn%2==0:
                return False
            elif self.mainBoard[y][x].color == "w" and self.turn%2==1:
                return False
            self.gui_b.del_hl_list()
            self.currmovingpiece = self.mainBoard[y][x]
            for move in self.mainBoard[y][x].legalMoves():
                self.gui_b.hl_square(move[0],move[1], "green")
                self.gui_b.hl_squares(self.list_takes(move), "red")
            self.gui_b.hl_square(x,y,"blue")
            self.gui_b.hl_squares(self.list_takes((x,y)),"red")
            
        #if a none-square is clicked, and not second, reset everything
        else:
            self.gui_b.del_hl_list()
            self.poss_move = []
        if self.gameover:
            self.gui_b.destroy()
        
    def list_takes(self,(x,y)):
        imm_deaths = []
        if x > 0:
            if self.mainBoard[y][x-1]:
                if self.check_willdie(x-1,y):
                    imm_deaths.append((x-1,y))
        if x < 11:
             if self.mainBoard[y][x+1]:
                if self.check_willdie(x+1,y):
                    imm_deaths.append((x+1,y))
        if y > 0:
            if self.mainBoard[y-1][x]:
                if self.check_willdie(x,y-1):
                    imm_deaths.append((x,y-1))
        if y < 7:
            if self.mainBoard[y+1][x]:
                if self.check_willdie(x,y+1):
                    imm_deaths.append((x,y+1))
        
        return imm_deaths

    def check_willdie(self,x,y):
        color = self.mainBoard[y][x].color
        attackers = []
        if self.isSafe(x,y,color):
            return False
        if y > 0 and self.mainBoard[y-1][x]:
            if self.mainBoard[y-1][x].color != color:
                attackers.append(self.mainBoard[y-1][x])
        if y < 7 and self.mainBoard[y+1][x]:
            if self.mainBoard[y+1][x].color != color:
                attackers.append(self.mainBoard[y+1][x])
        if x > 0 and self.mainBoard[y][x-1]:
            if self.mainBoard[y][x-1].color != color:
                attackers.append(self.mainBoard[y][x-1])
        if x < 11 and self.mainBoard[y][x+1]:
            if self.mainBoard[y][x+1].color != color:
                attackers.append(self.mainBoard[y][x+1])
        if self.currmovingpiece in attackers:
            del attackers[attackers.index(self.currmovingpiece)]
        if len(attackers) > 0 and self.currmovingpiece.color != color:
            return True
    def isSafe(self,x,y,color):
        safe = 0
        if y > 0 and x > 0:
            if self.mainBoard[y-1][x-1]:
                if self.mainBoard[y-1][x-1].color == color:
                    safe += 1
        
        if y > 0 and x < 11:
            if self.mainBoard[y-1][x+1]:
                if self.mainBoard[y-1][x+1].color == color:
                    safe += 4

        if y < 7 and x > 0:
            if self.mainBoard[y+1][x-1]:
                if self.mainBoard[y+1][x-1].color == color:
                    safe += 4

        if y < 7 and x < 11:
            if self.mainBoard[y+1][x+1]:
                if self.mainBoard[y+1][x+1].color == color:
                    safe += 1
        if safe == 2 or safe > 6:
            return True

            
    def movePiece(self, (x1,y1), (x2,y2)):
        #how to move a piece:
        piece = self.mainBoard[y1][x1]
        #move the piece internally (this will throw an error if piece cannot be moved there)
        if self.mainBoard.movePiece((y1,x1), (y2,x2)):
            #move the piece on the gui
            self.gui_b.movePiece(self.PIECES[piece],(x2,y2))
            #check if taking a piece
            for take in self.list_takes((x2,y2)):
                #remove piece on gui
                self.gui_b.del_piece(self.PIECES.pop(self.mainBoard[take[1]][take[0]]))
                #remove piece on board
                piecetype = self.mainBoard.killPiece(take)
                print "Piece taken: "+piecetype
                if piecetype == "king":
                    print "Game over"
                    self.gameover = True
                    
            return True
        
   
if __name__ == "__main__":
    m = main()
