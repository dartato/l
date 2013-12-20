from Tkinter import *

master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()
piecedict = {}
test_img = PhotoImage(file="wpawn.gif")
piecedict[(1,1)] = w.create_image(200,200,image=test_img)
w.delete(piecedict[(1,1)])



mainloop()
