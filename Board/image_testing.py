from Tkinter import *
#from PIL import Image, ImageTk
#tstimage = Image.open("Chess_Sprites.png")

test = Tk()
tstimage = PhotoImage(file="pawn.gif")
label = Label(test,image = tstimage)

label.pack()
mainloop()
