import tkinter as gui
from datetime import datetime
import math
import ctypes

##defines window specifications
root = gui.Tk()
##name
root.title("Shape Surface Area and Volume Calculator")
##window size
root.geometry("500x800") 
##unscalable
root.resizable(False, False)

##prior nessacairy data
BackButton = None
pi = math.pi

##directory for all equation used to make easy eval solving.
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
TrianglePyramidSurfaceFormula = "0.5*(num1*num2)+3/2*(num2*num3)"

def savefunction():
    ##globals all data to keep it between functions
    global title, displaynum1, displaynum2, displaynum3, awnser, Unit
    ##Gets answer and defines it so it can be easily saved
    solution = visual.get()
    ##creates name based on exact time to prevent duplicates
    default = f"calc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    ##assembles data
    content = f"{solution}\n={awnser:g}{Unit}"
    #in write mode ('w')
    with open(default, "w", encoding="utf-8") as text_file:
        open(default,"w", encoding="utf-8").close()
        # Write the content to the file
        text_file.write(content)

def resetfunction():
    ##globals all data to keep it between functions
    global Fontsize, Unit, CubebuttonSurface, CylinderbuttonSurface, SpherebuttonSurface, ConebuttonSurface, SquarePyramidbuttonSurface, TrianglePyramidbuttonSurface, current_visual, displaynum1, displaynum2, displaynum3, label, extra, visual, title, Volumebutton, extra2, extra3, extra4, Surfacebutton,Cubebutton,Cylinderbutton,Spherebutton,Conebutton,SquarePyramidbutton,TrianglePyramidbutton,BackButton,ButtonInput,entry,label2,num1,num2,num3,question,awnser, displaynum3, displaynum2, displaynum1
    ##Sets all values to none so code can start fresh
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
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##The 2 main menu buttons and label
    Volumebutton = gui.Button(root, font=("Helvetica", 19), text="Volume", width=15, height=21, command=button_clicked_Volume)
    Volumebutton.place(x=10, y=180)
    Volumebutton.config(activebackground="#424242")
    Surfacebutton = gui.Button(root, font=("Helvetica", 19), text="Surface Area", width=15, height=21, command=button_clicked_Surface)
    Surfacebutton.place(x=260, y=180)
    Surfacebutton.config(activebackground="#424242")
    label = gui.Label(root, text="What would you like to calculate?", font=("Helvetica", 25))
    label.pack(pady=20)

def submit(event=None):
    ##globals all data to keep it between functions
    global num1, num2, num3, entry, placeholder, label2, label, ButtonInput, question, title, awnser, visual, current_visual, Unit
    ##gets number for comparison
    placeholder = entry.get()
    ## checks if there isn't already another value for X
    if num1 == "X":
        try:
            ##Compare for variable to prevent boundary error
            placeholder = entry.get()
            placeholder = float(placeholder)
            if placeholder > 0:
              if isinstance(placeholder, (int, float)):
                    num1 = float(placeholder)
                    displaynum1.set(f"{num1:g}")
                    ## uses tk variables for live updating of titles and labels, also models the equation in the form of pressed button.
                    visual.set(
                        current_visual.format(
                        title=title,
                        x=displaynum1.get(),
                        y=displaynum2.get(),
                        z=displaynum3.get()
                        )
                    )
                    ##changes label to suit next value to input
                    if label2 != None:
                        label2.destroy()
                        label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
                        label2.place(y=200)
                        ##shows current equation
                        if label != None:
                            label.destroy()
                            label = gui.Label(root, textvariable=visual, font=("Helvetica", Fontsize), wraplength=450)
                            label.place(y=20)
                            entry.delete(0, gui.END)
                            return
            ##if it doesn't work, tell them to input again until valid.
            else:
                label2 = gui.Label(root, text="Please use valid int for X", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
        
            ##if it doesn't work, tell them to input again until valid.
        except ValueError:
            if label2 != None:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for X", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
    ## checks if there isn't already another value for Y
    elif num2 == "Y":
        try:
            ##Compare for variable to prevent boundary error
            placeholder = entry.get()
            placeholder = float(placeholder)
            if placeholder > 0:
                if isinstance(placeholder, (int, float)):
                    ##if valid sets num to be what was entered.
                    num2 = float(placeholder)
                    displaynum2.set(f"{num2:g}")
                    ## uses tk variables for live updating of titles and labels, also models the equation in the form of pressed button.
                    visual.set(
                        current_visual.format(
                        title=title,
                        x=displaynum1.get(),
                        y=displaynum2.get(),
                        z=displaynum3.get()
                        )
                    )
                    ##moves on to next input
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
            ##if it doesn't work, tell them to input again until valid.
            else:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for Y", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
        ##if it doesn't work, tell them to input again until valid.
        except ValueError:
            if label2 != None:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for Y", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
    ## checks if there isn't already another value for Z
    elif num3 == "Z":
        try:
            ##Compare for variable to prevent boundary error
            placeholder = entry.get()
            placeholder = float(placeholder)
            if placeholder > 0:
                if isinstance(placeholder, (int, float)):
                    ##if valid sets num to be what was entered.
                    num3 = float(placeholder)
                    displaynum3.set(f"{num3:g}")
                    ## uses tk variables for live updating of titles and labels, also models the equation in the form of pressed button.
                    visual.set(
                        current_visual.format(
                        title=title,
                        x=displaynum1.get(),
                        y=displaynum2.get(),
                        z=displaynum3.get()
                        )
                    )
                    ##removes label and replaces it with answer
                    entry.delete(0, gui.END)
                    label2.destroy()
                    entry.destroy()
                    if ButtonInput != None:
                        ButtonInput.destroy()
                    ##allows decimals
                    num1 = float(num1)
                    num2 = float(num2)
                    num3 = float(num3)
                    if label != None:
                        label.destroy()
                        ##gives answer and asks to save
                        if label != None:
                            label.destroy()
                            label = gui.Label(root, textvariable=visual, font=("Helvetica", Fontsize), wraplength=450)
                            label.place(y=20)
                        awnser = eval(question)
                        label2 = gui.Label(root, text=f"={round(awnser, 6):g}{Unit}", font=("Helvetica", 18))
                        label2.place(y=250)
                        SaveButton = gui.Button(root, text="Save results?", width=21, height=2, command=savefunction, font=("Helvetica", 14))
                        SaveButton.place(x=130,y=600)
                        SaveButton.config(activebackground="#424242")
                    return
            ##if it doesn't work, tell them to input again until valid.
            else:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for Z", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return
        ##if it doesn't work, tell them to input again until valid.
        except ValueError:
            if label2 != None:
                label2.destroy()
                label2 = gui.Label(root, text="Please use valid int for Z", font=("Helvetica", 14))
                label2.place(y=200)
                entry.delete(0, gui.END)
                return

def button_clicked_Volume():
    ##globals all data to keep it between functions
    global label, Volumebutton, Surfacebutton, Unit
    global Cubebutton, Cylinderbutton, Spherebutton, Conebutton, SquarePyramidbutton, TrianglePyramidbutton, BackButton
    ##nessacairy to keep correct awnser and data for documents, changes based on either volume (^3) and surface area (^2)
    Unit = "Units^3"
    ##Full page removal of button and gui
    if label is not None:
        label.destroy()
    if Volumebutton is not None:
        Volumebutton.destroy()
    if Surfacebutton is not None:
        Surfacebutton.destroy()
    ##places all the buttons for the shapes and feeds back the command to their respective code
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
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")

def button_clicked_Surface():
    ##globals all data to keep it between functions
    global label, Volumebutton, Surfacebutton
    global Unit, CubebuttonSurface, CylinderbuttonSurface, SpherebuttonSurface, ConebuttonSurface, SquarePyramidbuttonSurface, TrianglePyramidbuttonSurface, BackButton
    Unit = "Units^2"
    ##Full page removal of button and gui
    if label is not None:
        label.destroy()
    if Volumebutton is not None:
        Volumebutton.destroy()
    if Surfacebutton is not None:
        Surfacebutton.destroy()
    ##places all the buttons for the shapes and feeds back the command to their respective code
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
    TrianglePyramidbuttonSurface = gui.Button(root, text="Regular Triangle Based Pyramid\n⛛", width=21, height=10, command=TrianglePyramid_button_Surface_clicked, font=("Helvetica", 14), wraplength=(200))
    TrianglePyramidbuttonSurface.place(x=252,y=490)
    TrianglePyramidbuttonSurface.config(activebackground="#424242")
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")

def Cube_button_clicked():
    ##globals all data to keep it between functions
    global entry, label2, label, ButtonInput, question, title, BackButton, current_visual
    question = CubeVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cube Volume ="
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cube Volume =\nX*Y*Z", font=("Helvetica", 50))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}{x}*{y}*{z}"
    ##places image
    IMG = gui.Label(root, image=cubeimg)
    IMG.place(x=125, y=360)

def Cylinder_button_clicked():
    ##globals all data to keep it between functions
    global entry, label2, label, ButtonInput, question, title, num1, BackButton, current_visual
    question = CylinderVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cylinder Volume ="
    ##sets num to the required without user input
    num1 = round(math.pi, 4)
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cylinder Volume =\nπ*X*Y^2", font=("Helvetica", 40))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    num1 = math.pi
    ##formats equation
    current_visual = "{title}π*{y}*{z}^2"
    ##places image
    IMG = gui.Label(root, image=cylinderimg)
    IMG.place(x=110, y=320)

def Sphere_button_clicked():
    ##globals all data to keep it between functions
    global entry, label2, label, ButtonInput, question, title, num1, num2, BackButton, current_visual
    question = SphereVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Sphere Volume ="
    ##sets num to the required without user input
    num2 = round(math.pi, 4)
    num1 = round(4/3, 5)
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for Z", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Sphere Volume =\nπ*(4/3)*Z**3", font=("Helvetica", 45))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}π*(4/3)*{z}^3"
    ##places image
    IMG = gui.Label(root, image=sphereimg)
    IMG.place(x=125, y=360)

def Cone_button_clicked(): ##Working
    ##globals all data to keep it between functions
    global BackButton, current_visual, entry, label2, label, ButtonInput, question, title, num1
    question = ConeVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cone Volume ="
    ##sets num to the required without user input
    num1 = round(math.pi, 4)
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cone Volume =\nπ*(Y**2)*(Z/3)", font=("Helvetica", 40))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}π*({y}^2)*({z}/3)"
    ##places image
    IMG = gui.Label(root, image=coneimg)
    IMG.place(x=130, y=340)

def SquarePyramid_button_clicked(): ##Working
    ##globals all data to keep it between functions
    global entry, label2, label, ButtonInput, question, title, BackButton, current_visual
    question = SquarePyramidVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Square Pyramid Volume = ("
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Square Pyramid Volume =(X*Y*Z)/3", font=("Helvetica", 32), wraplength=500)
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}{x}*{y}*{z})/3"
    ##Places image
    IMG = gui.Label(root, image=pyramidsquareimg)
    IMG.place(x=130, y=340)

def TrianglePyramid_button_clicked(): ##Working
    ##globals all data to keep it between functions
    global entry, label2, label, ButtonInput, question, title, BackButton, current_visual
    question = TrianglePyramidVolumeFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Triangle Pyramid Volume = (0.5*"
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Triangle Pyramid Volume =(0.5*X*Y*Z)/3", font=("Helvetica", 32), wraplength=500)
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}{x}*{y}*{z})/3"
    ##places image
    IMG = gui.Label(root, image=pyramidtriangleimg)
    IMG.place(x=115, y=360)

def Cube_button_Surface_clicked():
    ##globals all data to keep it between functions
    global BackButton, current_visual, entry, label2, label, ButtonInput, question, title
    question = CubeSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cube Surface Area ="
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cube Volume =\n2*(X*Y+X*Z+Y*Z)", font=("Helvetica", 40))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}2*({x}*{y}+{x}*{z}+{y}*{z})"
    ##places image
    IMG = gui.Label(root, image=cubeimg)
    IMG.place(x=125, y=360)

def Cylinder_button_Surface_clicked():
    ##globals all data to keep it between functions
    global entry, label2, label, ButtonInput, question, title, num1, BackButton, current_visual
    question = CylinderSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cylinder Surface Area ="
    ##sets num to the required without user input
    num1 = round(math.pi, 4)
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cylinder Surface Area =\n2π*Y*Z+2π*Y^2", font=("Helvetica", 30))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##sets num to the required without user input
    num1 = math.pi
    ##formats equation
    current_visual = "{title}2π*{y}*{z}+2π*{y}^2"
    ##Places image
    IMG = gui.Label(root, image=cylinderimg)
    IMG.place(x=110, y=320)

def Sphere_button_Surface_clicked():
    ##globals all data to keep it between functions
    global entry, label2, label, ButtonInput, question, title, num1, num2, BackButton, current_visual
    question = SphereSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Sphere Surface Area ="
    ##sets num to the required without user input
    num2 = round(math.pi, 4)
    num1 = 4
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for Z", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Sphere Surface Area =\n4*π*Z^2", font=("Helvetica", 35))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}4*π*{z}^2"
    ##places image
    IMG = gui.Label(root, image=sphereimg)
    IMG.place(x=125, y=360)

def Cone_button_Surface_clicked(): ##Working
    ##globals all data to keep it between functions
    global BackButton, current_visual, entry, label2, label, ButtonInput, question, title, num1
    question = ConeSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Cone Surface Area ="
    ##sets num to the required without user input
    num1 = round(math.pi, 4)
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for Y", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Cone Surface Area =\nπ*Y*(Y+(Z**2+Y**2)**0.5)", font=("Helvetica", 25))
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}π*{y}*({y}+({z}**2+{y}**2)**0.5)"
    ##places image
    IMG = gui.Label(root, image=coneimg)
    IMG.place(x=130, y=340)

def SquarePyramid_button_Surface_clicked(): ##Working
    ##globals all data to keep it between functions
    global BackButton, current_visual, entry, label2, label, ButtonInput, question, title, Fontsize
    question = SquarePyramidSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    ##sets font size so equation fits
    Fontsize = 20
    title = "Square Pyramid Surface Area ="
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Square Pyramid Surface Area =Y*X+Y*((X/2)^2+Z^2)^0.5+X*((Y/2)^2+Z^2)^0.5", font=("Helvetica", 20), wraplength=440)
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}{y}*{x}+{y}*(({x}/2)^2+{z}^2)^0.5+{x}*(({y}/2)^2+{z}^2)^0.5"
    ##Places image
    IMG = gui.Label(root, image=pyramidsquareimg)
    IMG.place(x=130, y=340)

def TrianglePyramid_button_Surface_clicked(): ##working
    ##globals all data to keep it between functions
    global BackButton, current_visual, entry, label2, label, ButtonInput, question, title
    question = TrianglePyramidSurfaceFormula ##use this to set what button and equation instead of making a new submit function for each.
    title = "Triangle Pyramid Surface Area ="
    ##Full page removal of button and gui
    for widget in root.winfo_children():
        widget.destroy()
    ##intializes the calculator input box for use
    label2 = gui.Label(root, text="Please type value for X", font=("Helvetica", 14))
    label2.place(y=200)
    label = gui.Label(root, text="Triangle Pyramid Surface Area =0.5*(X*Y)+3/2*(Y*Z)", font=("Helvetica", 32), wraplength=500)
    label.place(y=20)
    entry = gui.Entry(root, width=20, font=("Helvetica", 20))
    entry.place(x=21, y=250)
    entry.bind("<Return>", submit)
    ButtonInput = gui.Button(root, text="Submit", command=submit, height=2, width=15)
    ButtonInput.place(x=345,y=250)
    ##Button that resets back to inital state
    BackButton = gui.Button(root, text="Back", width=43, height=2, command=resetfunction, font=("Helvetica", 14))
    BackButton.place(x=8,y=730)
    BackButton.config(activebackground="#424242")
    ##formats equation
    current_visual = "{title}0.5*({x}*{y})+3/2*({y}*{z})"
    ##places image
    IMG = gui.Label(root, image=pyramidtriangleimg)
    IMG.place(x=115, y=360)

##image for icon
img = gui.PhotoImage(file="Allsixes.png")
root.iconphoto(True, img)

##window icon
myappid = 'mycompany.myproduct.subproduct.version' # unique string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
##root.iconbitmap(img)

##resets all data to same as start
resetfunction()

##diagrams for all equation being defined before starting
cubeimg = gui.PhotoImage(file="Cube.png")
cylinderimg = gui.PhotoImage(file="CylinderVolume.png")
sphereimg = gui.PhotoImage(file="Sphere.png")
coneimg = gui.PhotoImage(file="Cone.png")
pyramidsquareimg = gui.PhotoImage(file="PyramidSquare.png")
pyramidtriangleimg = gui.PhotoImage(file="TrianglePryamid.png")

##this starts and complies it all, mainly gui.
root.mainloop()
