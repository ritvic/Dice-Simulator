import tkinter as Tk
from PIL import Image, ImageTk
import random

# function activated by button
def onedice():
    root.geometry('235x290')
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image2)
    # keep a reference
    label1.image = image2

def twodice():
    root.geometry('235x500')
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
    label1.configure(image=image2)
    label1.image = image2
    image5 = ImageTk.PhotoImage(Image.open(random.choice(dice2)))
    label5.configure(image=image5)
    label5.image = image5

# toplevel widget which represents the main window of an application
root = Tk.Tk()
root.resizable(width=False, height=False)
root.geometry('235x290')
root.title('Dice Simulator')

# Adding label into the frame
l1 = Tk.Label(root, text="Hey, Try Your Luck Now!", fg = "purple3", bg = "lavender", font = "comicsansms 14 bold").grid()
b1 = Tk.Button(root, text='Roll one Dice', fg='blue',bg= 'ghost white',relief = 'raised', command=onedice).grid(row = 2)
b2 = Tk.Button(root, text='Roll two Dice', fg='blue',bg= 'ghost white',relief = 'raised', command=twodice).grid(row = 3)

# images
dice1 = ['D1.jpg','D2.jpg','D2.jpg','D3.jpg','D4.jpg','D3.jpg','D4.jpg','D3.jpg','D4.jpg','D5.jpg','D5.jpg','D6.jpg']
dice2 = ['1.jpg','6.jpg','3.jpg','4.jpg','3.jpg','4.jpg','3.jpg','4.jpg','5.jpg','2.jpg','5.jpg','2.jpg']
dice = dice1+dice2

# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# construct a label widget for image
label1 = Tk.Label(root, image=image1,bg = 'pale goldenrod')
label1.grid()
image3 = ImageTk.PhotoImage(Image.open(random.choice(dice2)))
label5 = Tk.Label(root, image=image3, bg = 'pale goldenrod')
label5.grid()

root.configure(bg= 'lavender')
# call the mainloop of Tk
# keeps window open
root.mainloop()