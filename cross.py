import tkinter as tk
from PIL import ImageTk, Image
import warnings

warnings.filterwarnings('ignore') # setting ignore as a parameter

lastClickX = 0
lastClickY = 0
Moving = int(1000)

path = 'crosshair.png'

root = tk.Tk()
root.overrideredirect(1)
root.wm_attributes('-alpha', 0.7)
root.geometry("125x125")
root.resizable(False, False)
root.attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")
root.configure(bg='white')

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
        if Moving >= 100:
                x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
                root.geometry("+%s+%s" % (x , y))
        else: print('false')

root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)

image = Image.open(path)
width = 125
ratio = (width / float(image.size[0]))
height = int((float(image.size[1]) * float(ratio)))
image = image.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack(side="top", fill="both", expand="yes")

canvas.create_image(0, 0, anchor="nw", image=image)
root.mainloop()
