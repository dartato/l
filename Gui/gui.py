from Tkinter import *
from PIL import Image, ImageTk
PIECENAMES = ("pawn","bishop","knight","rook","queen","king")
PIECECOLORS = ('w','b')
GAMES = {}
GAMES["Latrinculi"],GAMES["Checkers"],GAMES["Chess"] = (12,8),(8,8),(8,8)

class GUIMenu(Tk):
    def __init__(self,game_options=GAMES,name="Main Menu"):
        Tk.__init__(self)
        self.wm_title(name),self.resizable(0,0)
        self.buttons = {}
        self.is_done = False
        for game in game_options:
            self.buttons[game] = Button(text=game)
            self.buttons[game].grid()
        self.buttons["Latrinculi"]["command"]=self.make_latrinculi
        self.buttons["Checkers"]["command"]=self.make_checkers
        self.buttons["Chess"]["command"]=self.make_chess
        self.buttons["Quit?"] = Button(text="Quit?",command=self.die).grid()
        mainloop()
        
    def make_latrinculi(self):
        lc = GUIBoard(12,8,name="Latrinculi")
        global lc
        self.die()
    def make_chess(self):
        chess = GUIBoard(8,8,name="Chess")
        global chess
        self.die()
    def make_checkers(self):
        checkers = GUIBoard(8,8,name="Checkers")
        global checkers
        self.die()

    def die(self):
        self.is_done = True
        self.destroy()
        
        
class GUIBoard(Tk):
    
    def __init__(self,b_width,b_height,name="Checker Board"):
        Tk.__init__(self)
        self.wm_title(name),self.resizable(0,0)
        self.hl_list = []
        self.b_width,self.b_height = b_width,b_height
        self.get_dims()
        self.draw_board()
        self.LOADED_IMAGES = {}
        
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
        return True

    def add_piece(self,x,y,piece_type):
        if not piece_type in self.LOADED_IMAGES:
            self.LOADED_IMAGES[piece_type] = PhotoImage(file=piece_type + ".gif")
        x_coord = self.sidel/2 + self.sidel*x
        y_coord = self.sidel/2 + self.sidel*y
        return self.b_canvas.create_image(x_coord,y_coord,image=self.LOADED_IMAGES[piece_type])

    def del_piece(self,piece):
        self.b_canvas.delete(piece)
        
    def hl_square(self,x,y,color):
        self.hl_list.append(self.b_canvas.create_rectangle(x*self.sidel,y*self.sidel,(x+1)*self.sidel,(y+1)*self.sidel,fill=color,stipple="gray25"))
        #fer dank in range(dayz)

    def movePiece(self, piece, (x,y)):
        self.b_canvas.coords(piece, (self.sidel/2+self.sidel*x,self.sidel/2+self.sidel*y))
        
    def hl_squares(self,squares_list, color):
        for square in squares_list:
            self.hl_square(square[0],square[1],color)
                   
    def del_hl_list(self):
        for square in range(len(self.hl_list)):
            self.b_canvas.delete(self.hl_list.pop())

if __name__ == "__main__":
    #testing recent additions
    #b = GUIBoard(8,8)
    m = GUIMenu()
    

