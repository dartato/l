from Tkinter import *

master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()
test_img = PhotoImage(file="pawn.gif")
w.create_image(200,200,image=test_img)



mainloop()
