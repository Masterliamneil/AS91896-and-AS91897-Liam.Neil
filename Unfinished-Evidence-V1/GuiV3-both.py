import tkinter as gui
import os
from pathlib import Path
import math

pi = math.pi

label = None ##this fixes all my problems
Volumebutton = None
Surfacebutton = None

Cubebutton = None
Cylinderbutton = None
Spherebutton = None
Conebutton = None
SquarePyramidbutton = None
TrianglePyramidbutton = None
BackButton = None
ButtonInput = None

entry = None
label2 = None

num1 = "X"
num2 = "Y"
num3 = "Z"
placeholder = None
question = None
pi = math.pi
##cubevolumeawnser = int(num1*num2*num3)

##home_dir = os.path.expanduser("~") ##used for images, graphics and data storage.
##newpath = Path(home_dir) / "Desktop"
##os.chdir(newpath)
root = gui.Tk()
root.title("Cal-cue-la-tor")
root.geometry("500x800") 
root.resizable(False, False)

def button_clicked_Surface():
    global label, Volumebutton, Surfacebutton ##this fixes all my problems when used with the other.
    global BackButton
    if label is not None:
        label.destroy()
    if Volumebutton is not None:
        Volumebutton.destroy()
    if Surfacebutton is not None:
        Surfacebutton.destroy()
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")

def resetfunction():
    global label, Volumebutton, Surfacebutton,Cubebutton,Cylinderbutton,Spherebutton,Conebutton,SquarePyramidbutton,TrianglePyramidbutton,BackButton,ButtonInput,entry,label2,num1,num2,num3,question
    label = None ##this fixes all my problems
    if BackButton != None:
        BackButton.destroy()
    Volumebutton = None
    Surfacebutton = None
    Cubebutton = None
    Cylinderbutton = None
    Spherebutton = None
    Conebutton = None
    SquarePyramidbutton = None
    TrianglePyramidbutton = None
    BackButton = None
    ButtonInput = None
    entry = None
    label2 = None
    num1 = "X"
    num2 = "Y"
    num3 = "Z"
    question = None
    for widget in root.winfo_children():
        widget.destroy()
    Volumebutton = gui.Button(root, font=("Helvetica", 19), text="Volume", width=15, height=21, command=button_clicked_Volume)
    Volumebutton.place(x=10, y=180)
    Volumebutton.config(activebackground="#424242")
    Surfacebutton = gui.Button(root, font=("Helvetica", 19), text="Surface Area", width=15, height=21, command=button_clicked_Surface)
    Surfacebutton.place(x=260, y=180)
    Surfacebutton.config(activebackground="#424242")
    label = gui.Label(root, text="What would you like to calculate?", font=("Helvetica", 25))
    label.pack(pady=20)

def submit(): #we may need a seccond submit function for 2 number equations.
    global num1, num2, num3, entry, placeholder, label2, label, ButtonInput
    placeholder = entry.get()
    if num1 == "X":
        try:
            placeholder = entry.get()
            placeholder = float(placeholder)
            if placeholder > 0:
              if isinstance(placeholder, (int, float)):
                    num1 = float(placeholder)
                    if label2 != None:
                        label2.destroy()
                        label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
                        label2.place(y=200)
                        if label != None:
                            label.destroy()
                            label = gui.Label(root, text=f"Cube Volume =\n{num1}*{num2}*{num3}", font=("Helvetica", 45))
                            label.place(y=20)
                            entry.delete(0, gui.END)
                            return
            else:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for X", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
        except ValueError:
            if label2 != None:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for X", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
    elif num2 == "Y":
        try:
            placeholder = entry.get()
            placeholder = float(placeholder)
            if placeholder > 0:
                if isinstance(placeholder, (int, float)):
                    num2 = float(placeholder)
                    if label2 != None:
                        label2.destroy()
                        label2 = gui.Label(root, text="Please type value for Z", font=("Helvetica", 14))
                        label2.place(y=200)
                        if label != None:
                            label.destroy()
                            label = gui.Label(root, text=f"Cube Volume =\n{num1}*{num2}*{num3}", font=("Helvetica", 45))
                            label.place(y=20)
                        entry.delete(0, gui.END)
                        return
            else:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for Y", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
        except ValueError:
            if label2 != None:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for Y", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
    elif num3 == "Z":
        try:
            placeholder = entry.get()
            placeholder = float(placeholder)
            if placeholder > 0:
                if isinstance(placeholder, (int, float)):
                    num3 = float(placeholder)
                    entry.delete(0, gui.END)
                    label2.destroy()
                    entry.destroy()
                    if ButtonInput != None:
                        ButtonInput.destroy()
                    num1 = float(num1)
                    num2 = float(num2)
                    num3 = float(num3)
                    if label != None:
                        label.destroy()
                        label = gui.Label(root, text=f"Cube Volume =\n{num1}*{num2}*{num3}", font=("Helvetica", 45))
                        label.place(y=20)
                    
                        cubevolumeawnser = float(num1*num2*num3)
                        label2 = gui.Label(root, text=f"{cubevolumeawnser}Units^3", font=("Helvetica", 18))
                        label2.place(y=200)
                    return
            else:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for Z", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
                #if label2 != None:
                    #label2.destroy()
                    #label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
                    #label2.place(y=200)
        except ValueError:
            if label2 != None:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for Z", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return

def button_clicked_Volume():
    global label, Volumebutton, Surfacebutton
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton
    if label is not None:
        label.destroy()
    if Volumebutton is not None:
        Volumebutton.destroy()
    if Surfacebutton is not None:
        Surfacebutton.destroy()
    Cubebutton = gui.Button(root, text="Cuboid\n❒", width=21, height=10, command=Cube_button_clicked, font=("Helvetica", 14))
    Cubebutton.place(x=8, y=10)
    Cubebutton.config(activebackground="#424242")
    Cylinderbutton = gui.Button(root, text="Cylinder\n🛢", width=21, height=10, command=button_clicked_Surface, font=("Helvetica", 14))
    Cylinderbutton.place(x=252,y=10)
    Cylinderbutton.config(activebackground="#424242")
    Spherebutton = gui.Button(root, text="Sphere\n🔵", width=21, height=10, command=button_clicked_Surface, font=("Helvetica", 14))
    Spherebutton.place(x=8, y=250)
    Spherebutton.config(activebackground="#424242")
    Conebutton = gui.Button(root, text="Cone\n𓉴", width=21, height=10, command=button_clicked_Surface, font=("Helvetica", 14))
    Conebutton.place(x=252,y=250)
    Conebutton.config(activebackground="#424242")
    SquarePyramidbutton = gui.Button(root, text="Square Based Pyramid\n☒", width=21, height=10, command=button_clicked_Surface, font=("Helvetica", 14))
    SquarePyramidbutton.place(x=8, y=490)
    SquarePyramidbutton.config(activebackground="#424242")
    TrianglePyramidbutton = gui.Button(root, text="Triangle Based Pyramid\n⛛", width=21, height=10, command=button_clicked_Surface, font=("Helvetica", 14))
    TrianglePyramidbutton.place(x=252,y=490)
    TrianglePyramidbutton.config(activebackground="#424242")
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")

def Cube_button_clicked():
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton
    global entry, label2, label, ButtonInput
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cube Volume =\nX*Y*Z", font=("Helvetica", 50))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")




Volumebutton = gui.Button(root, font=("Helvetica", 19), text="Volume", width=15, height=21, command=button_clicked_Volume)
Volumebutton.place(x=10, y=180)
Volumebutton.config(activebackground="#424242")

Surfacebutton = gui.Button(root, font=("Helvetica", 19), text="Surface Area", width=15, height=21, command=button_clicked_Surface)
Surfacebutton.place(x=260, y=180)
Surfacebutton.config(activebackground="#424242")

label = gui.Label(root, text="What would you like to calculate?", font=("Helvetica", 25))
label.pack(pady=20)

root.mainloop()