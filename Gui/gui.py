from Tkinter import *

class GUIBoard(Tk):

    def __init__(self,b_width,b_height,name="Checker Board"):
        Tk.__init__(self)
        self.resizable(0,0)
        self.wm_title(name)
        self.b_width,self.b_height = b_width,b_height
        self.get_dims()
        self.draw_board()
        mainloop()
        
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
        colorcounter=0
        for column in range(self.b_width): 
            if self.b_height %2 == 0:
                colorcounter += 1
            for row in range(self.b_height):
                if colorcounter%2 == 0:
                    self.b_canvas.create_rectangle(column*self.sidel,row*self.sidel,(column+1)*self.sidel,(row+1)*self.sidel,fill="black")
                colorcounter += 1    
        self.b_canvas.pack()


b = GUIBoard(12,8,name="Latrine Something")
