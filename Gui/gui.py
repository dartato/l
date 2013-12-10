from Tkinter import *


def board_init(b_width,b_height):
    master = Tk()
    master.resizable(0,0)
    master.wm_title("Checker Board")
    """(Board width, board height)"""
    gui_width = master.winfo_screenwidth()*1/2
    gui_height = master.winfo_screenheight()*2/3
    h_sidel = gui_width/b_width
    v_sidel = gui_height/b_height
    sidel = min(h_sidel,v_sidel)
    gui_height = sidel*b_height
    gui_width = sidel*b_width
        
    s = Canvas(master, width=gui_width, height=gui_height)
    colorcounter=0
    for column in range(b_width): 
        if b_height %2 == 0:
            colorcounter += 1
        for row in range(b_height):
            if colorcounter%2 == 0:
                s.create_rectangle(column*sidel,row*sidel,(column+1)*sidel,(row+1)*sidel,fill="black")
            colorcounter += 1    
    s.pack()
    
board_init(4,2)
mainloop()
