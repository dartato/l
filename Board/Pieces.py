from matrices import *
class piece(object):
    # basic functions
    def __init__(self, x, y, color, board, name=None):
        self.board = board
        self.type = name
        self.color = color
        self.pos = x, y

    def __repr__(self):
        return str(self.color+self.type)
    def __str__(self):
        return str(self.color+self.type)
    # what a piece does
    def __legalMoves__(self):
        # I think, therefore I am. Currently this always returns true.
        if self.board[self.pos[0]][self.pos[1]] == None:
            return None
        else:
            return True

class pawn(piece):
    def __init__(self, x, y, color, board):
        piece.__init__(self, x, y, color, board, name="pawn")
    def legalmoves(self):
        if piece.__legalMoves__(self):
            row = self.board[self.pos[0]]
            col = rowsCols(self.board)[self.pos[1]]
            moves = []
            if self.pos[1]>0 and row[self.pos[1]-1] == None:
                moves.append((self.pos[1]-1,self.pos[0]))
            if self.pos[0]>0 and col[self.pos[0]-1] == None:
                moves.append((self.pos[1],self.pos[0]-1))
            if self.pos[1]<7 and row[self.pos[1]+1] == None:
                moves.append((self.pos[1]+1,self.pos[0]))
            if self.pos[0]<11 and col[self.pos[0]+1] == None:
                moves.append((self.pos[1],self.pos[0]+1))
            
            return moves
                
class king(piece):
    def __init__(self, x, y, color, board):
        piece.__init__(self, x, y, color, board, name="king")
