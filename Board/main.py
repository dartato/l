import Board
import Pieces
from Board import pprint
import gui



mainBoard = Board.init()
pprint(mainBoard)

b = gui.GUIBoard(12,8,name="Latrine Something")
