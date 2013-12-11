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
        self.gui_b = gui.GUIBoard(self.mainBoard.cols,self.mainBoard.rows,name="Latrine Something")
        #generate list of pieces
        self.PIECES = {}
        for row in self.mainBoard:
            for piece in row:
                if piece:
                    self.PIECES[piece] = self.gui_b.add_piece(piece.pos[1],piece.pos[0],piece.color,piece.type)
        #add the submit move button
        self.submitButton = Button(self.gui_b,text="Move", command=self.updateBoard)
        self.submitButton.pack()
        #start it up!
        self.gui_b.mainloop()
    def movePiece(self, (x1,y1), (x2,y2)):
        #how to move a piece:
        piece = self.mainBoard[y1][x1]
        #move the piece internally (this will throw an error if piece cannot be moved there)
        if self.mainBoard.movePiece((y1,x1), (y2,x2)):
            #move the piece on the gui
            self.gui_b.b_canvas.coords(self.PIECES[piece], (self.gui_b.sidel/2+self.gui_b.sidel*x2,self.gui_b.sidel/2+self.gui_b.sidel*y2))
    def updateBoard(self):
        #get the contents of the move box
        move = self.gui_b.entryBox.get()
        #format is initial x,initial y,final x,final y
        i_x = int(move[0])
        i_y = int(move[2])
        f_x = int(move[4])
        f_y = int(move[6])
        print(i_x,i_y,f_x,f_y)
        
        if move == "dank":
            self.movePiece((0,0),(0,1))
        else:
            self.movePiece((i_x,i_y),(f_x,f_y))
        Board.pprint(self.mainBoard)
        #clear the text box
        self.gui_b.entryBox.delete(0,'end')
        
if __name__ == "__main__":
    m = main()
