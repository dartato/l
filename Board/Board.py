from matrices import *
import Pieces
# board - what is used to find out where pieces are and what spaces are taken on the board



class board(matrix):
    def __init__(self, cols=12, rows=8):
        #make a matrix the size of the board
        matrix.__init__(self, cols, rows)
    def movePiece(self, (x1,y1), (x2,y2), newtype=False):
        if self[x2][y2]:
            return "Error: target square occupied"
        if newtype:
            self[x2][y2] = newtype
            self[x1][y1].pos = x2,y2
        else:
            self[x2][y2] = self[x1][y1]
            self[x1][y1].pos = x2,y2
        self[x1][y1] = None
def pprint(board_obj):
    print " |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  "
    for i, row in enumerate(board_obj):
        out = str(i)
        for i1, square in enumerate(row):
            if board_obj[i][i1]:
                out+= "|"+str(board_obj[i][i1])
            else:
                out+= "|     "
        print out
            
def init():
    b = board()
    b[0] = [Pieces.pawn(0,x,"w",b) for x in range(12)]
    b[7] = [Pieces.pawn(7,x,"b",b) for x in range(12)]
    b[1][5] = Pieces.king(1,5,"w",b)
    b[6][6] = Pieces.king(6,6,"b",b)
    return b
