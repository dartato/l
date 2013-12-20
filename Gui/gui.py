from Tkinter import *
from PIL import Image, ImageTk
PIECENAMES = ("pawn","bishop","knight","rook","queen","king")
PIECECOLORS = ('w','b')
#pawn = PhotoImage(file="pawn.gif")
class GUIBoard(Tk):
    
    def __init__(self,b_width,b_height,name="Checker Board"):
        Tk.__init__(self)
        self.wm_title(name),self.resizable(0,0)
        self.hl_list = []
        self.gui_pieces = {}
        self.b_width,self.b_height = b_width,b_height
        self.get_dims()
        self.draw_board()
        self.assign_images()
        
    def get_dims(self):
        temp_gui_width = self.winfo_screenwidth()*1/2
        temp_gui_height = self.winfo_screenheight()*2/3
        #determines limiting dimension, then applies to square side length
        h_sidel = temp_gui_width/self.b_width
        v_sidel = temp_gui_height/self.b_height
        self.sidel = min(h_sidel,v_sidel)
        #final dimensions
        self.gui_height,self.gui_width = self.sidel*self.b_height,self.sidel*self.b_width
        
        
    def draw_board(self): 
        self.b_canvas = Canvas(self, width=self.gui_width, height=self.gui_height)
        self.b_canvas.pack()
        colorcounter=0
        for column in range(self.b_width): 
            if self.b_height %2 == 0:
                colorcounter += 1
            for row in range(self.b_height):
                if colorcounter%2 == 0:
                    self.b_canvas.create_rectangle(column*self.sidel,row*self.sidel,(column+1)*self.sidel,(row+1)*self.sidel,fill="gray")
                colorcounter += 1
        
    def assign_images(self):
        self.wpawn_img = PhotoImage(file="wpawn.gif")
        self.wbishop_img = PhotoImage(file="wbishop.gif")
        self.wknight_img = PhotoImage(file="wknight.gif")
        self.wrook_img = PhotoImage(file="wrook.gif")
        self.wqueen_img = PhotoImage(file="wqueen.gif")
        self.wking_img = PhotoImage(file="wking.gif")
        self.bpawn_img = PhotoImage(file="bpawn.gif")
        self.bbishop_img = PhotoImage(file="bbishop.gif")
        self.bknight_img = PhotoImage(file="bknight.gif")
        self.brook_img = PhotoImage(file="brook.gif")
        self.bqueen_img = PhotoImage(file="bqueen.gif")
        self.bking_img = PhotoImage(file="bking.gif")
        
    def get_piece_img(self,color,name):
        if name == "pawn":
            if color == "w":
                img_file = self.wpawn_img
            elif color == "b":
                img_file = self.bpawn_img
        elif name == "bishop":
            if color == "w":
                img_file = self.wbishop_img
            elif color == "b":
                img_file = self.bbishop_img
        elif name == "knight":
            if color == "w":
                img_file = self.wknight_img
            elif color == "b":
                img_file = self.bknight_img
        elif name == "rook":
            if color == "w":
                img_file = self.wrook_img
            elif color == "b":
                 img_file = self.brook_img
        elif name == "queen":
            if color == "w":
                img_file = self.wqueen_img
            elif color == "b":
                img_file = self.bqueen_img
        elif name == "king":
            if color == "w":
                img_file = self.wking_img
            elif color == "b":
                img_file = self.bking_img
        return img_file
    
    def add_piece(self,x,y,color,name):
        img_file = self.get_piece_img(color,name)        
        x_coord = self.sidel/2 + self.sidel*x
        y_coord = self.sidel/2 + self.sidel*y
        #creates a running dictionary of pieces on the gui, accessible by a tuple of their coords
        self.gui_pieces[(x,y)] = self.b_canvas.create_image(x_coord,y_coord,image=img_file)
        return self.gui_pieces[(x,y)]

    def del_piece(self,x,y):
        self.b_canvas.delete(self.gui_pieces[(x,y)])
        
    def hl_square(self,x,y,color):
        self.hl_list.append(self.b_canvas.create_rectangle(x*self.sidel,y*self.sidel,(x+1)*self.sidel,(y+1)*self.sidel,fill=color,stipple="gray25"))
        #fer dank in range(dayz)

    def movePiece(self, piece, (x,y)):
        self.b_canvas.coords(piece, (self.sidel/2+self.sidel*x,self.sidel/2+self.sidel*y))

    def take(self, piece, (x,y)):
        self.del_piece(x,y)
        self.movePiece(self, piece, (x,y))
        
    def hl_squares(self,squares_list, color):
        for square in squares_list:
            self.hl_square(square[0],square[1],color)
                   
    def del_hl_list(self):
        for square in range(len(self.hl_list)):
            self.b_canvas.delete(self.hl_list.pop())


            
if __name__ == "__main__":
    #testing recent additions
    b = GUIBoard(12,8)
    for i in range(6):
        b.add_piece(i,0,"w",PIECENAMES[i])
        b.add_piece(i,1,"b",PIECENAMES[i])
    b.hl_square(0,4,"red")
    b.del_hl_list()
    print b.hl_list
    b.del_piece(1,0)
    mainloop()

