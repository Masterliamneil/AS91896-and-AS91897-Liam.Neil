import tkinter as gui
import os
from pathlib import Path
from datetime import datetime
import math

pi = math.pi

CubeVolumeFormula = "num1*num2*num3" ##With use of eval(Cubeformula) can be used as an equation directory.
CylinderVolumeFormula = "pi*num2*num3**2"
SphereVolumeFormula = "(4/3)*pi*num3**3"
ConeVolumeFormula = "pi*(num2**2)*(num3/3)"
SquarePyramidVolumeFormula = "(num1*num2*num3)/3"
TrianglePyramidVolumeFormula = "(0.5*num1*num2*num3)/3"

awnser = None
title = None
label = None ##this fixes all my problems
extra = None
extra2 = None
extra3 = None
extra4 = None
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

def savefunction():
    global title, num1, num2, num3, awnser
    default = f"calc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    content = f"{title}{num1}*{num2}*{num3}\n={awnser}Units^3"
    #in write mode ('w')
    with open(default, "w") as text_file:
        open(default,"w").close()
        # Write the content to the file
        text_file.write(content)

def resetfunction():
    global label, extra, title, Volumebutton, extra2, extra3, extra4, Surfacebutton,Cubebutton,Cylinderbutton,Spherebutton,Conebutton,SquarePyramidbutton,TrianglePyramidbutton,BackButton,ButtonInput,entry,label2,num1,num2,num3,question,awnser
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
    awnser = None
    title = None
    extra = None
    entry = None
    label2 = None
    num1 = "X"
    num2 = "Y"
    num3 = "Z"
    extra2 = None
    extra3 = None
    extra4 = None
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
    global num1, num2, num3, entry, placeholder, label2, label, ButtonInput, question, title, awnser, extra, extra2, extra3, extra4
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
                            if extra != None:
                                label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                label.place(y=20)
                                entry.delete(0, gui.END)
                                if extra2 != None:
                                    if label != None:
                                        label.destroy()
                                    label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                    label.place(y=20)
                                    entry.delete(0, gui.END)
                                    if extra3 != None:
                                        if label != None:
                                            label.destroy()
                                        label = gui.Label(root, text=f"{title}\n{num1}*{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                        label.place(y=20)
                                        entry.delete(0, gui.END)
                                        if extra4 != None:
                                            if label != None:
                                                label.destroy()
                                            label = gui.Label(root, text=f"{title}\n{num1}*{extra4}{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                            label.place(y=20)
                                            entry.delete(0, gui.END)
                                        else:
                                            if label != None:
                                                label.destroy()
                                            label = gui.Label(root, text=f"{title}\n{num1}*{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                            label.place(y=20)
                                            entry.delete(0, gui.END)
                                    else:
                                        if label != None:
                                            label.destroy()
                                        label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                        label.place(y=20)
                                        entry.delete(0, gui.END)
                                else:
                                    if label != None:
                                        label.destroy()
                                    label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                    label.place(y=20)
                                    entry.delete(0, gui.END)
                                return
                            else:
                                if label != None:
                                    label.destroy()
                                label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}", font=("Helvetica", 30), wraplength=450)
                                label.place(y=20)
                                entry.delete(0, gui.END)
                            return
            else:
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
                        if extra != None:
                                label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                label.place(y=20)
                                entry.delete(0, gui.END)
                                if extra2 != None:
                                    if label != None:
                                        label.destroy()
                                    label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                    label.place(y=20)
                                    entry.delete(0, gui.END)
                                    if extra3 != None:
                                        if label != None:
                                            label.destroy()
                                        label = gui.Label(root, text=f"{title}\n{num1}*{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                        label.place(y=20)
                                        entry.delete(0, gui.END)
                                        if extra4 != None:
                                            if label != None:
                                                label.destroy()
                                            label = gui.Label(root, text=f"{title}\n{num1}*{extra4}{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                            label.place(y=20)
                                            entry.delete(0, gui.END)
                                        else:
                                            if label != None:
                                                label.destroy()
                                            label = gui.Label(root, text=f"{title}\n{num1}*{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                            label.place(y=20)
                                            entry.delete(0, gui.END)
                                    else:
                                        if label != None:
                                            label.destroy()
                                        label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                        label.place(y=20)
                                        entry.delete(0, gui.END)
                                else:
                                    label.destroy
                                    label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                    label.place(y=20)
                                    entry.delete(0, gui.END)
                                return
                        else:
                            label.destroy
                            label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}", font=("Helvetica", 30), wraplength=450)
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
                        if extra != None:
                                label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                label.place(y=20)
                                if extra2 != None:
                                    label.destroy()
                                    label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                    label.place(y=20)
                                    if extra3 != None:
                                        label.destroy()
                                        label = gui.Label(root, text=f"{title}\n{num1}*{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                        label.place(y=20)
                                        if extra4 != None:
                                            label.destroy()
                                            label = gui.Label(root, text=f"{title}\n{num1}*{extra4}{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                            label.place(y=20)
                                        else:
                                            if label != None:
                                                label.destroy()
                                            label = gui.Label(root, text=f"{title}\n{num1}*{num2}{extra3}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                            label.place(y=20)
                                    else:
                                        if label != None:
                                            label.destroy()
                                        label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{extra2}{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                        label.place(y=20)
                                else:
                                    if label != None:
                                            label.destroy()
                                    label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}{extra}", font=("Helvetica", 30), wraplength=450)
                                    label.place(y=20)
                        else:
                            if label != None:
                                    label.destroy()
                            label = gui.Label(root, text=f"{title}\n{num1}*{num2}*{num3}", font=("Helvetica", 30), wraplength=450)
                            label.place(y=20)

                    
                        awnser = eval(question)
                        label2 = gui.Label(root, text=f"={awnser}Units^3", font=("Helvetica", 18))
                        label2.place(y=250)
                        SaveButton = gui.Button(root, text="Save results?", width=21, height=2, command=savefunction, font=("Helvetica", 14))
                        SaveButton.place(x=130,y=600)
                        SaveButton.config(activebackground="#424242")
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
    Cylinderbutton = gui.Button(root, text="Cylinder\n🛢", width=21, height=10, command=Cylinder_button_clicked, font=("Helvetica", 14))
    Cylinderbutton.place(x=252,y=10)
    Cylinderbutton.config(activebackground="#424242")
    Spherebutton = gui.Button(root, text="Sphere\n🔵", width=21, height=10, command=Sphere_button_clicked, font=("Helvetica", 14))
    Spherebutton.place(x=8, y=250)
    Spherebutton.config(activebackground="#424242")
    Conebutton = gui.Button(root, text="Cone\n𓉴", width=21, height=10, command=Cone_button_clicked, font=("Helvetica", 14))
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
    global entry, label2, label, ButtonInput, question, CubeVolumeFormula, title
    question = CubeVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cube Volume ="
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

def Cylinder_button_clicked():
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton
    global entry, label2, label, ButtonInput, question, CylinderVolumeFormula, title, num1, extra
    question = CylinderVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    extra = "^2"
    title = "Cylinder Volume ="
    num1 = math.pi
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cylinder Volume =\nPi*X*Y**2", font=("Helvetica", 50))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")

def Sphere_button_clicked():
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton
    global entry, label2, label, ButtonInput, question, SphereVolumeFormula, title, num1, extra, num2, num3
    question = SphereVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    extra = "^3"
    title = "Sphere Volume ="
    num2 = round(math.pi, 4)
    num1 = round(4/3, 5)
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for Z", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Sphere Volume =\n4/3*pi*Z**3", font=("Helvetica", 45))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")

def Cone_button_clicked(): ##broken
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton
    global entry, label2, label, ButtonInput, question, ConeVolumeFormula, title, num1, extra, extra2, extra3, extra4, num2, num3, π
    question = ConeVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    extra = "/3)"
    extra2 = "("
    extra3 = "^3)"
    extra4 = "("
    title = "Cone Volume ="
    num1 = round(math.pi, 4)
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cone Volume =\nπ*(Y**2)*(Z/3)", font=("Helvetica", 40))
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