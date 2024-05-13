from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("750x400")
#Define function to update the image
def update_image():
   canvas.itemconfig(image_container,image=my_img2)
#Create a canvas and add the image into it
canvas= Canvas(win, width=650, height= 350)
canvas.pack()
#Create a button to update the canvas image
button= ttk.Button(win, text="Update",
command=lambda:update_image())
button.pack()
#Open an Image in a Variable
image1 = Image.open('data/input.png')
my_img1 = ImageTk.PhotoImage(image1)

image1 = Image.open('data/greyscale.png')
my_img2 = ImageTk.PhotoImage(image1)

img2= PhotoImage(file="data\\greyscale.png")

#Add image to the canvas
image_container =canvas.create_image(0,0, anchor="nw",image=my_img1)
win.mainloop()