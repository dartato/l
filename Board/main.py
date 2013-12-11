import Board
import Pieces
from Board import pprint
import gui



mainBoard = Board.init()
pprint(mainBoard)

gui_b = gui.GUIBoard(mainBoard.cols,mainBoard.rows,name="Latrine Something")
