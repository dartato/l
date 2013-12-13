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
        # base legal moves, returns an empty list
        return []

class pawn(piece):
    def __init__(self, x, y, color, board):
        piece.__init__(self, x, y, color, board, name="pawn")
    def legalMoves(self):
        #gets the legal moves for a pawn

        #self.pos[1] is horizontal component and self.pos[0] the vertical
        #row is the horizontal line the pawn is on
        row = self.board[self.pos[0]]

        #col is the vertical line the pawn is on
        col = rowsCols(self.board)[self.pos[1]]
        moves = []
        vmoves = []
        hmoves = []
        #moves for adjacent squares
        if self.pos[1] > 0 and not row[self.pos[1]-1]:
            moves.append((self.pos[1]-1,self.pos[0]))
        if self.pos[1] < 11 and not row[self.pos[1]+1]:
            moves.append((self.pos[1]+1,self.pos[0]))
        if self.pos[0] > 0 and not col[self.pos[0]-1]:
            moves.append((self.pos[1],self.pos[0]-1))
        if self.pos[0] < 7 and not col[self.pos[0]+1]:
            moves.append((self.pos[1],self.pos[0]+1))

        #moves to jump to pawn in same col/row
        for i, square in enumerate(row):
            if square and square.color == self.color:
                if i < self.pos[1]:
                    if not row[i+1]:
                        hmoves.append((i+1,self.pos[0]))
                if i > self.pos[1]:
                    if not row[i-1]:
                        hmoves.append((i-1,self.pos[0]))

        for i, square in enumerate(col):
            if square and square.color == self.color:
                if i < self.pos[0]:
                    if not col[i+1]:
                        vmoves.append((self.pos[1],i+1))
                if i > self.pos[0]:
                    if not col[i-1]:
                        vmoves.append((self.pos[1],i-1))
        #moves to jump next to adjacent pawn
        if self.pos[0] > 0:
            for i, square in enumerate(self.board[self.pos[0]-1]):
                if square and square.color == self.color:
                    if i < self.pos[1] or i > self.pos[1]:
                        try:
                            if not row[i+1]:
                                hmoves.append((i+1,self.pos[0]))
                            if not row[i]:
                                hmoves.append((i,self.pos[0]))
                            if not row[i-1]:
                                hmoves.append((i-1,self.pos[0]))
                        except IndexError:
                            pass
        if self.pos[0] < 7:
            for i, square in enumerate(self.board[self.pos[0]+1]):
                if square and square.color == self.color:
                    if i < self.pos[1] or i > self.pos[1]:
                        try:
                            if not row[i+1]:
                                hmoves.append((i+1,self.pos[0]))
                            if not row[i]:
                                hmoves.append((i,self.pos[0]))
                            if not row[i-1]:
                                hmoves.append((i-1,self.pos[0]))
                        except IndexError:
                            pass
        if self.pos[1] > 0:
            for i, square in enumerate(rowsCols(self.board)[self.pos[1]-1]):
                if square and square.color == self.color:
                    if i < self.pos[0] or i > self.pos[0]:
                        try:
                            if not col[i+1]:
                                vmoves.append((self.pos[1],i+1))
                            if not col[i]:
                                vmoves.append((self.pos[1],i))
                            if not col[i-1]:
                                vmoves.append((self.pos[1],i-1))
                        except IndexError:
                            pass

        if self.pos[1] < 11:
            for i, square in enumerate(rowsCols(self.board)[self.pos[1]+1]):
                if square and square.color == self.color:
                    if i < self.pos[0] or i > self.pos[0]:
                        try:
                            if not col[i+1]:
                                vmoves.append((self.pos[1],i+1))
                            if not col[i]:
                                vmoves.append((self.pos[1],i))
                            if not col[i-1]:
                                vmoves.append((self.pos[1],i-1))
                        except IndexError:
                            pass
        #cleanup moves
        hout = hmoves[:]
        for move in hmoves:
            if move[0] < self.pos[1]:
                btw = row[move[0]:self.pos[1]]
            elif move[0] > self.pos[1]:
                btw = row[self.pos[1]+1:move[0]]
            else:
                continue
            for square in btw:
                if square:
                    hout.remove(move)
                    break
                
        vout = vmoves[:]
        for move in vmoves:
            if move[1] < self.pos[0]:
                btw = col[move[1]:self.pos[0]]
            elif move[1] > self.pos[0]:
                btw = col[self.pos[0]+1:move[1]]
            else:
                continue
            for square in btw:
                if square:
                    vout.remove(move)
                    break
        moves+=hout+vout
        return moves
                
class king(pawn,piece):
    def __init__(self, x, y, color, board):
        piece.__init__(self, x, y, color, board, name="king")
    def legalMoves(self):
        #row is the horizontal line the king is on
        row = self.board[self.pos[0]]

        #col is the vertical line the king is on
        col = rowsCols(self.board)[self.pos[1]]
        moves = []
        hmoves, vmoves = [(x,self.pos[0]) for x in range(len(row))],[(self.pos[1],x) for x in range(len(col))]
        hout = hmoves[:]
        for move in hmoves:
            if move[0] < self.pos[1]:
                btw = row[move[0]:self.pos[1]]
            elif move[0] > self.pos[1]:
                btw = row[self.pos[1]+1:move[0]+1]
            else:
                continue
            for square in btw:
                if square:
                    hout.remove(move)
                    break
                
        vout = vmoves[:]
        for move in vmoves:
            if move[1] < self.pos[0]:
                btw = col[move[1]:self.pos[0]]
            elif move[1] > self.pos[0]:
                btw = col[self.pos[0]+1:move[1]+1]
            else:
                continue
            for square in btw:
                if square:
                    vout.remove(move)
                    break
        moves+=hout+vout
        return moves
