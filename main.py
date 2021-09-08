from tkinter import *

img_display_root = Tk()

img_display_root.geometry("1920x1080")

# img = PhotoImage("image.png")
# this method is for jpg files! 

img = PhotoImage(file="image.png")
# This Method Is For PNG Files!

img_label = Label(image=img)
img_label.pack()

img_display_root.mainloop() #Keeping The Window Open