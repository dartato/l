import Board.Board as Board
import Board.Pieces as Pieces
from Tkinter import Button
from Board.Board import pprint
import Gui.gui as gui

class main:
    def __init__(self):
        #create board instance
        self.mainBoard = Board.init()
        #initiate gui
        self.gui_b = gui.GUIBoard(self.mainBoard.cols,self.mainBoard.rows,name="Latrin Culi")
        self.poss_move = []
        self.gui_b.b_canvas.bind("<Button-1>",self.get_click)
        #generate list of pieces
        self.PIECES = {}
        for row in self.mainBoard:
            for piece in row:
                if piece:
                    self.PIECES[piece] = self.gui_b.add_piece(piece.pos[1],piece.pos[0],piece.color,piece.type)
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
            self.gui_b.del_hl_list()
            self.gui_b.hl_squares(self.mainBoard[y][x].legalMoves(), "green")
            self.gui_b.hl_square(x,y,"blue")
            
        #if a none-square is clicked, and not second, reset everything
        else:
            self.gui_b.del_hl_list()
            self.poss_move = []
        print self.gui_b.hl_list
          
    def movePiece(self, (x1,y1), (x2,y2)):
        #how to move a piece:
        piece = self.mainBoard[y1][x1]
        #move the piece internally (this will throw an error if piece cannot be moved there)
        if self.mainBoard.movePiece((y1,x1), (y2,x2)):
            #move the piece on the gui
            self.gui_b.movePiece(self.PIECES[piece],(x2,y2))
            return True
        
   
if __name__ == "__main__":
    m = main()
