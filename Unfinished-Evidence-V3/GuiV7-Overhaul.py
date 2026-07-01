import tkinter as gui
import os
from pathlib import Path
from datetime import datetime
import math
import ctypes

root = gui.Tk()
root.title("Cal-cue-la-tor")
root.geometry("500x800") 
root.resizable(False, False)

pi = math.pi

CubeVolumeFormula = 'num1*num2*num3' ##With use of eval(Cubeformula) can be used as an equation directory.
CylinderVolumeFormula = "pi*num2*num3**2"
SphereVolumeFormula = "(4/3)*pi*num3**3"
ConeVolumeFormula = "pi*(num2**2)*(num3/3)"
SquarePyramidVolumeFormula = "(num1*num2*num3)/3"
TrianglePyramidVolumeFormula = "(0.5*num1*num2*num3)/3"

CubeSurfaceFormula = "2*(num1*num2+num1*num3+num2*num3)"
CylinderSurfaceFormula = "2*num1*num2*num3+2*num1*num2**2"
SphereSurfaceFormula = "4*pi*num3**2"
ConeSurfaceFormula = "pi*num2*(num2+(num3**2+num2**2)**0.5)"
SquarePyramidSurfaceFormula = "num2*num1+num2*((num1/2)**2+num3**2)**0.5+num1*((num2/2)**2+num3**2)**0.5"
TrianglePyramidSurfaceFormula = ""

displaynum1 = gui.StringVar()
displaynum1.set("X")
displaynum2 = gui.StringVar()
displaynum2.set("Y")
displaynum3 = gui.StringVar()
displaynum3.set("Z")

visual = gui.StringVar()
visual.set(0)

current_visual = ""

awnser = None
title = None
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
Fontsize = 30

CubebuttonSurface = None
CylinderbuttonSurface = None
SpherebuttonSurface = None
ConebuttonSurface = None
SquarePyramidbuttonSurface = None
TrianglePyramidbuttonSurface = None

Unit = None
entry = None
label2 = None
placeholder = None
question = None

num1 = "X"
num2 = "Y"
num3 = "Z"

titlecubevolumequestion = f"{num1}*{num2}*{num3}"
titleCylindervolumequestion = f"{round(math.pi, 4)}*{num2}*{num3}^2"
titleSpherevolumequestion = f"(4/3)*{round(math.pi, 4)}*{num3}^3"
titleConevolumequestion = f"{round(math.pi, 4)}*({num2}^2)*({num3}/3)"
titleSquarePyramidvolumequestion = f"({num1}*{num2}*{num3}/3)"
titleTrianglePyramidvolumequestion = f"(0.5*{num1}*{num2}*{num3}/3)"


##home_dir = os.path.expanduser("~") ##used for images, graphics and data storage.
##newpath = Path(home_dir) / "Desktop"
##os.chdir(newpath)

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
    global title, num1, num2, num3, awnser, visual, Unit
    default = f"calc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    content = f"{visual.get()}\n={awnser}{Unit}"
    #in write mode ('w')
    with open(default, "w") as text_file:
        open(default,"w").close()
        # Write the content to the file
        text_file.write(content)

def resetfunction():
    global Fontsize, Unit, CubebuttonSurface, CylinderbuttonSurface, SpherebuttonSurface, ConebuttonSurface, SquarePyramidbuttonSurface, TrianglePyramidbuttonSurface, current_visual, displaynum1, displaynum2, displaynum3, label, extra, visual, title, Volumebutton, extra2, extra3, extra4, Surfacebutton,Cubebutton,Cylinderbutton,Spherebutton,Conebutton,SquarePyramidbutton,TrianglePyramidbutton,BackButton,ButtonInput,entry,label2,num1,num2,num3,question,awnser, displaynum3, displaynum2, displaynum1
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
    Unit = None
    entry = None
    label2 = None
    CubebuttonSurface = None
    CylinderbuttonSurface = None
    SpherebuttonSurface = None
    ConebuttonSurface = None
    SquarePyramidbuttonSurface = None
    TrianglePyramidbuttonSurface = None
    Fontsize = 30
    num1 = "X"
    num2 = "Y"
    num3 = "Z"
    displaynum1 = gui.StringVar()
    displaynum1.set("X")
    displaynum2 = gui.StringVar()
    displaynum2.set("Y")
    displaynum3 = gui.StringVar()
    displaynum3.set("Z")
    visual = gui.StringVar()
    visual.set("0")
    current_visual = ""
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

def submit(event=None): #we may need a seccond submit function for 2 number equations.
    global num1, num2, num3, entry, placeholder, label2, label, ButtonInput, question, title, awnser, visual, current_visual, Unit
    placeholder = entry.get()
    if num1 == "X":
        try:
            placeholder = entry.get()
            placeholder = float(placeholder)
            if placeholder > 0:
              if isinstance(placeholder, (int, float)):
                    num1 = float(placeholder)
                    displaynum1.set(num1)
                    visual.set(
                        current_visual.format(
                        title=title,
                        x=displaynum1.get(),
                        y=displaynum2.get(),
                        z=displaynum3.get()
                        )
                    )
                    if label2 != None:
                        label2.destroy()
                        label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
                        label2.place(y=200)
                        if label != None:
                            label.destroy()
                            label = gui.Label(root, textvariable=visual, font=("Helvetica", Fontsize), wraplength=450)
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
                    displaynum2.set(num2)
                    visual.set(
                        current_visual.format(
                        title=title,
                        x=displaynum1.get(),
                        y=displaynum2.get(),
                        z=displaynum3.get()
                        )
                    )
                    if label2 != None:
                        label2.destroy()
                        label2 = gui.Label(root, text="Please type value for Z", font=("Helvetica", 14))
                        label2.place(y=200)
                        if label != None:
                            label.destroy()
                            label = gui.Label(root, textvariable=visual, font=("Helvetica", Fontsize), wraplength=450)
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
                    displaynum3.set(num3)
                    visual.set(
                        current_visual.format(
                        title=title,
                        x=displaynum1.get(),
                        y=displaynum2.get(),
                        z=displaynum3.get()
                        )
                    )
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
                        if label != None:
                            label.destroy()
                            label = gui.Label(root, textvariable=visual, font=("Helvetica", Fontsize), wraplength=450)
                            label.place(y=20)

                    
                        awnser = eval(question)
                        label2 = gui.Label(root, text=f"={round(awnser, 6)}{Unit}", font=("Helvetica", 18))
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
    global label, Volumebutton, Surfacebutton, Unit
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton
    Unit = "Units^3"
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
    SquarePyramidbutton = gui.Button(root, text="Square Based Pyramid\n☒", width=21, height=10, command=SquarePyramid_button_clicked, font=("Helvetica", 14))
    SquarePyramidbutton.place(x=8, y=490)
    SquarePyramidbutton.config(activebackground="#424242")
    TrianglePyramidbutton = gui.Button(root, text="Triangle Based Pyramid\n⛛", width=21, height=10, command=TrianglePyramid_button_clicked, font=("Helvetica", 14))
    TrianglePyramidbutton.place(x=252,y=490)
    TrianglePyramidbutton.config(activebackground="#424242")
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")

def button_clicked_Surface():
    global label, Volumebutton, Surfacebutton
    global Unit, CubebuttonSurface, CylinderbuttonSurface, SpherebuttonSurface, ConebuttonSurface, SquarePyramidbuttonSurface, TrianglePyramidbuttonSurface, BackButton
    Unit = "Units^2"
    if label is not None:
        label.destroy()
    if Volumebutton is not None:
        Volumebutton.destroy()
    if Surfacebutton is not None:
        Surfacebutton.destroy()
    CubebuttonSurface = gui.Button(root, text="Cuboid\n❒", width=21, height=10, command=Cube_button_Surface_clicked, font=("Helvetica", 14))
    CubebuttonSurface.place(x=8, y=10)
    CubebuttonSurface.config(activebackground="#424242")
    CylinderbuttonSurface = gui.Button(root, text="Cylinder\n🛢", width=21, height=10, command=Cylinder_button_Surface_clicked, font=("Helvetica", 14))
    CylinderbuttonSurface.place(x=252,y=10)
    CylinderbuttonSurface.config(activebackground="#424242")
    SpherebuttonSurface = gui.Button(root, text="Sphere\n🔵", width=21, height=10, command=Sphere_button_Surface_clicked, font=("Helvetica", 14))
    SpherebuttonSurface.place(x=8, y=250)
    SpherebuttonSurface.config(activebackground="#424242")
    ConebuttonSurface = gui.Button(root, text="Cone\n𓉴", width=21, height=10, command=Cone_button_Surface_clicked, font=("Helvetica", 14))
    ConebuttonSurface.place(x=252,y=250)
    ConebuttonSurface.config(activebackground="#424242")
    SquarePyramidbuttonSurface = gui.Button(root, text="Square Based Pyramid\n☒", width=21, height=10, command=SquarePyramid_button_Surface_clicked, font=("Helvetica", 14))
    SquarePyramidbuttonSurface.place(x=8, y=490)
    SquarePyramidbuttonSurface.config(activebackground="#424242")
    TrianglePyramidbuttonSurface = gui.Button(root, text="Triangle Based Pyramid\n⛛", width=21, height=10, command=TrianglePyramid_button_Surface_clicked, font=("Helvetica", 14))
    TrianglePyramidbuttonSurface.place(x=252,y=490)
    TrianglePyramidbuttonSurface.config(activebackground="#424242")
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")

def Cube_button_clicked():
    """
    so like, ummmm, this is when cube button is clicked umm, yeah.
    Thank you Cube button clicked,
    "why did you call me that?"
    because you happen when cube button is clicked.
    """
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, visual, current_visual
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
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}{x}*{y}*{z}"
    IMG = gui.Label(root, image=cubeimg)
    IMG.place(x=125, y=360)

def Cylinder_button_clicked():
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, CylinderVolumeFormula, title, num1
    question = CylinderVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cylinder Volume ="
    num1 = math.pi
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cylinder Volume =\nπ*X*Y^2", font=("Helvetica", 40))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    num1 = math.pi
    current_visual = "{title}π*{y}*{z}^2"
    IMG = gui.Label(root, image=cylinderimg)
    IMG.place(x=110, y=320)

def Sphere_button_clicked():
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, SphereVolumeFormula, title, num1, num2, num3
    question = SphereVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Sphere Volume ="
    num2 = round(math.pi, 4)
    num1 = round(4/3, 5)
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for Z", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Sphere Volume =\nπ*(4/3)*Z**3", font=("Helvetica", 45))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}π*(4/3)*{z}^3"
    IMG = gui.Label(root, image=sphereimg)
    IMG.place(x=125, y=360)
    

def Cone_button_clicked(): ##Working
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, ConeVolumeFormula, title, num1, num2, num3
    question = ConeVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
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
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}π*({y}^2)*({z}/3)"
    IMG = gui.Label(root, image=coneimg)
    IMG.place(x=130, y=340)

def SquarePyramid_button_clicked(): ##Working
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, SquarePyramidVolumeFormula, title, num1, num2, num3
    question = SquarePyramidVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Square Pyramid Volume = ("
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Square Pyramid Volume =(X*Y*Z)/3", font=("Helvetica", 32), wraplength=500)
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}{x}*{y}*{z})/3"
    IMG = gui.Label(root, image=pyramidsquareimg)
    IMG.place(x=130, y=340)

def TrianglePyramid_button_clicked(): ##Working
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, TrianglePyramidVolumeFormula, title, num1, num2, num3
    question = TrianglePyramidVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Triangle Pyramid Volume = (0.5*"
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Triangle Pyramid Volume =(0.5*X*Y*Z)/3", font=("Helvetica", 32), wraplength=500)
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}{x}*{y}*{z})/3"

def Cube_button_Surface_clicked():
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, visual, current_visual
    global entry, label2, label, ButtonInput, question, CubeSurfaceFormula, title
    question = CubeSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cube Surface Area ="
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cube Volume =\n2*(X*Y+X*Z+Y*Z)", font=("Helvetica", 40))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}2*({x}*{y}+{x}*{z}+{y}*{z})"
    IMG = gui.Label(root, image=cubeimg)
    IMG.place(x=125, y=360)

def Cylinder_button_Surface_clicked():
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, CylinderSurfaceFormula, title, num1, extra
    question = CylinderSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cylinder Surface Area ="
    num1 = round(math.pi, 4)
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cylinder Surface Area =\n2π*Y*Z+2π*Y^2", font=("Helvetica", 30))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    num1 = math.pi
    current_visual = "{title}2π*{y}*{z}+2π*{y}^2"
    IMG = gui.Label(root, image=cylinderimg)
    IMG.place(x=110, y=320)

def Sphere_button_Surface_clicked():
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, SphereSurfaceFormula, title, num1, extra, num2, num3
    question = SphereSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Sphere Surface Area ="
    num2 = round(math.pi, 4)
    num1 = 4
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for Z", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Sphere Surface Area =\n4*π*Z^2", font=("Helvetica", 35))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}4*π*{z}^2"
    IMG = gui.Label(root, image=sphereimg)
    IMG.place(x=125, y=360)
    

def Cone_button_Surface_clicked(): ##Working
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, ConeSurfaceFormula, title, num1, extra, extra2, extra3, extra4, num2, num3
    question = ConeSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cone Volume ="
    num1 = round(math.pi, 4)
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cone Volume =\nπ*Y*(Y+(Z**2+Y**2)**0.5)", font=("Helvetica", 25))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}π*{y}*({y}+({z}**2+{y}**2)**0.5)"
    IMG = gui.Label(root, image=coneimg)
    IMG.place(x=130, y=340)

def SquarePyramid_button_Surface_clicked(): ##Working
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, SquarePyramidSurfaceFormula, title, num1, num2, num3, Fontsize
    question = SquarePyramidSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    Fontsize = 20
    title = "Square Pyramid Surface Area ="
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Square Pyramid Surface Area =Y*X+Y*((X/2)**2+Z**2)**0.5+X*((Y/2)**2+Z**2)**0.5", font=("Helvetica", 20), wraplength=440)
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}{y}*{x}+{y}*(({x}/2)**2+{z}**2)**0.5+{x}*(({y}/2)**2+{z}**2)**0.5"
    IMG = gui.Label(root, image=pyramidsquareimg)
    IMG.place(x=130, y=340)


def TrianglePyramid_button_Surface_clicked(): ##Broken
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton, current_visual
    global entry, label2, label, ButtonInput, question, TrianglePyramidVolumeFormula, title, num1, extra, extra2, extra3, extra4, num2, num3
    question = TrianglePyramidVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Triangle Pyramid Surface Area = (0.5*"
    for widget in root.winfo_children():
        widget.destroy()
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Triangle Pyramid Surface Area =(0.5*X*Y*Z)/3", font=("Helvetica", 32), wraplength=500)
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    current_visual = "{title}{x}*{y}*{z})/3"

Volumebutton = gui.Button(root, font=("Helvetica", 19), text="Volume", width=15, height=21, command=button_clicked_Volume)
Volumebutton.place(x=10, y=180)
Volumebutton.config(activebackground="#424242")

Surfacebutton = gui.Button(root, font=("Helvetica", 19), text="Surface Area", width=15, height=21, command=button_clicked_Surface)
Surfacebutton.place(x=260, y=180)
Surfacebutton.config(activebackground="#424242")

label = gui.Label(root, text="What would you like to calculate?", font=("Helvetica", 25))
label.pack(pady=20)

##image for icon
img = gui.PhotoImage(file="Allsixes.png")
root.iconphoto(True, img)

##window icon
myappid = 'mycompany.myproduct.subproduct.version' # unique string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
##root.iconbitmap(img)

##diagram test
cubeimg = gui.PhotoImage(file="Cube.png")
cylinderimg = gui.PhotoImage(file="CylinderVolume.png")
sphereimg = gui.PhotoImage(file="Sphere.png")
coneimg = gui.PhotoImage(file="Cone.png")
pyramidsquareimg = gui.PhotoImage(file="PyramidSquare.png")
root.mainloop()