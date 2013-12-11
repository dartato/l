import Board.Board as Board
import Board.Pieces as Pieces
from Board.Board import pprint
import Gui.gui as gui



mainBoard = Board.init()
pprint(mainBoard)

gui_b = gui.GUIBoard(mainBoard.cols,mainBoard.rows,name="Latrine Something")
for i in range(6):
    gui_b.add_piece(i,0,"w",gui.PIECENAMES[i])
    gui_b.add_piece(i,4,"b",gui.PIECENAMES[i])

gui_b.mainloop()

