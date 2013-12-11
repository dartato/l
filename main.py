import Board.Board as Board
import Board.Pieces as Pieces
from Board.Board import pprint
import Gui.gui as gui



mainBoard = Board.init()
pprint(mainBoard)

gui_b = gui.GUIBoard(mainBoard.cols,mainBoard.rows,name="Latrine Something")
