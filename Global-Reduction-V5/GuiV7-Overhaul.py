import tkinter as gui
from datetime import datetime
import math
import ctypes


class Calculator:


    #############################################
    #Formulas
    #############################################
    Back_Button = None
    pi = math.pi
    ##directory for all equation used to make easy eval solving.
    Cube_Volume_Formula = 'self.num1*self.num2*self.num3' ##With use of eval(Cubeformula) can be used as an equation directory.
    Cylinder_Volume_Formula = "self.pi*self.num2*self.num3**2"
    Sphere_Volume_Formula = "(4/3)*self.pi*self.num3**3"
    Cone_Volume_Formula = "self.pi*(self.num2**2)*(self.num3/3)"
    Square_Pyramid_Volume_Formula = "(self.num1*self.num2*self.num3)/3"
    Triangle_Pyramid_Volume_Formula = "(0.5*self.num1*self.num2*self.num3)/3"
    Cube_Surface_Formula = "2*(self.num1*self.num2+self.num1*self.num3+self.num2*self.num3)"
    Cylinder_Surface_Formula = "2*self.num1*self.num2*self.num3+2*self.num1*self.num2**2"
    Sphere_Surface_Formula = "4*self.pi*self.num3**2"
    Cone_Surface_Formula = "self.pi*self.num2*(self.num2+(self.num3**2+self.num2**2)**0.5)"
    Square_Pyramid_Surface_Formula = "self.num2*self.num1+self.num2*((self.num1/2)**2+self.num3**2)**0.5+self.num1*((self.num2/2)**2+self.num3**2)**0.5"
    Triangle_Pyramid_Surface_Formula = "0.5*(self.num1*self.num2)+3/2*(self.num2*self.num3)"

    
    def __init__(self):
        ##defines window specifications
        self.root = gui.Tk()
        ##name
        self.root.title("Shape Surface Area and Volume Calculator")
        ##window size
        self.root.geometry("500x800") 
        ##unscalable
        self.root.resizable(False, False)

            ##image for icon
        img = gui.PhotoImage(file="Allsixes.png")
        self.root.iconphoto(True, img)
            ##resets all data to same as start
        self.resetfunction()

        ##diagrams for all equation being defined before starting
        self.cube_img = gui.PhotoImage(file="Cube.png")
        self.cylinder_img = gui.PhotoImage(file="CylinderVolume.png")
        self.sphere_img = gui.PhotoImage(file="Sphere.png")
        self.cone_img = gui.PhotoImage(file="Cone.png")
        self.pyramid_square_img = gui.PhotoImage(file="PyramidSquare.png")
        self.pyramid_triangle_img = gui.PhotoImage(file="TrianglePryamid.png")

    def savefunction(self):
        ##Gets answer and defines it so it can be easily saved
        solution = self.visual.get()
        ##creates name based on exact time to prevent duplicates
        default = f"calc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        ##assembles data
        content = f"{solution}\n={self.awnser:g}{self.Unit}"
        #in write mode ('w')
        with open(default, "w", encoding="utf-8") as text_file:
            open(default,"w", encoding="utf-8").close()
            # Write the content to the file
            text_file.write(content)

    def resetfunction(self):
        ##Sets all values to none so code can start fresh
        self.label = None ##this fixes all my problems
        if self.Back_Button != None:
            self.Back_Button.destroy()
        self.Volume_button = None
        self.Surface_button = None
        self.Cube_button = None
        self.Cylinder_button = None
        self.Sphere_button = None
        self.Cone_button = None
        self.Square_Pyramid_button = None
        self.Triangle_Pyramid_button = None
        self.Back_Button = None
        self.Button_Input = None
        self.awnser = None
        self.title = None
        self.Unit = None
        self.entry = None
        self.label2 = None
        self.Cube_button_Surface = None
        self.Cylinder_button_Surface = None
        self.Sphere_button_Surface = None
        self.Cone_button_Surface = None
        self.Square_Pyramid_button_Surface = None
        self.Triangle_Pyramid_button_Surface = None
        self.Fontsize = 30
        self.num1 = "X"
        self.num2 = "Y"
        self.num3 = "Z"
        self.display_num1 = gui.StringVar()
        self.display_num1.set("X")
        self.display_num2 = gui.StringVar()
        self.display_num2.set("Y")
        self.display_num3 = gui.StringVar()
        self.display_num3.set("Z")
        self.visual = gui.StringVar()
        self.visual.set("0")
        self.current_visual = ""
        self.question = None
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##The 2 main menu buttons and label
        self.Volume_button = gui.Button(self.root, font=("Helvetica", 19), text="Volume", width=15, height=21, command=self.button_clicked_Volume)
        self.Volume_button.place(x=10, y=180)
        self.Volume_button.config(activebackground="#424242")
        self.Surface_button = gui.Button(self.root, font=("Helvetica", 19), text="Surface Area", width=15, height=21, command=self.button_clicked_Surface)
        self.Surface_button.place(x=260, y=180)
        self.Surface_button.config(activebackground="#424242")
        self.label = gui.Label(self.root, text="What would you like to calculate?", font=("Helvetica", 25))
        self.label.pack(pady=20)

    def submit(self, event=None):
        ##gets number for comparison
        placeholder = self.entry.get()
        ## checks if there isn't already another value for X
        if self.num1 == "X":
            try:
                ##Compare for variable to prevent boundary error
                placeholder = self.entry.get()
                placeholder = float(placeholder)
                if placeholder > 0:
                    if isinstance(placeholder, (int, float)):
                        self.num1 = float(placeholder)
                        self.display_num1.set(f"{self.num1:g}")
                        ## uses tk variables for live updating of titles and labels, also models the equation in the form of pressed button.
                        self.visual.set(
                            self.current_visual.format(
                            title=self.title,
                            x=self.display_num1.get(),
                            y=self.display_num2.get(),
                            z=self.display_num3.get()
                            )
                        )
                        ##changes self.label to suit next value to input
                        if self.label2 != None:
                            self.label2.destroy()
                            self.label2 = gui.Label(self.root, text="Please type value for Y", font=("Helvetica", 14))
                            self.label2.place(y=200)
                            ##shows current equation
                            if self.label != None:
                                self.label.destroy()
                                self.label = gui.Label(self.root, textvariable=self.visual, font=("Helvetica", self.Fontsize), wraplength=450)
                                self.label.place(y=20)
                                self.entry.delete(0, gui.END)
                                return
                ##if it doesn't work, tell them to input again until valid.
                else:
                    self.label2 = gui.Label(self.root, text="Please use valid int for X", font=("Helvetica", 14))
                    self.label2.place(y=200)
                    self.entry.delete(0, gui.END)
                    return
            
                ##if it doesn't work, tell them to input again until valid.
            except ValueError:
                if self.label2 != None:
                    self.label2.destroy()
                    self.label2 = gui.Label(self.root, text="Please use valid int for X", font=("Helvetica", 14))
                    self.label2.place(y=200)
                    self.entry.delete(0, gui.END)
                    return
        ## checks if there isn't already another value for Y
        elif self.num2 == "Y":
            try:
                ##Compare for variable to prevent boundary error
                placeholder = self.entry.get()
                placeholder = float(placeholder)
                if placeholder > 0:
                    if isinstance(placeholder, (int, float)):
                        ##if valid sets num to be what was entered.
                        self.num2 = float(placeholder)
                        self.display_num2.set(f"{self.num2:g}")
                        ## uses tk variables for live updating of titles and labels, also models the equation in the form of pressed button.
                        self.visual.set(
                            self.current_visual.format(
                            title=self.title,
                            x=self.display_num1.get(),
                            y=self.display_num2.get(),
                            z=self.display_num3.get()
                            )
                        )
                        ##moves on to next input
                        if self.label2 != None:
                            self.label2.destroy()
                            self.label2 = gui.Label(self.root, text="Please type value for Z", font=("Helvetica", 14))
                            self.label2.place(y=200)
                            if self.label != None:
                                self.label.destroy()
                                self.label = gui.Label(self.root, textvariable=self.visual, font=("Helvetica", self.Fontsize), wraplength=450)
                                self.label.place(y=20)
                                self.entry.delete(0, gui.END)
                            return
                ##if it doesn't work, tell them to input again until valid.
                else:
                    self.label2.destroy()
                    self.label2 = gui.Label(self.root, text="Please use valid int for Y", font=("Helvetica", 14))
                    self.label2.place(y=200)
                    self.entry.delete(0, gui.END)
                    return
            ##if it doesn't work, tell them to input again until valid.
            except ValueError:
                if self.label2 != None:
                    self.label2.destroy()
                    self.label2 = gui.Label(self.root, text="Please use valid int for Y", font=("Helvetica", 14))
                    self.label2.place(y=200)
                    self.entry.delete(0, gui.END)
                    return
        ## checks if there isn't already another value for Z
        elif self.num3 == "Z":
            try:
                ##Compare for variable to prevent boundary error
                placeholder = self.entry.get()
                placeholder = float(placeholder)
                if placeholder > 0:
                    if isinstance(placeholder, (int, float)):
                        ##if valid sets num to be what was entered.
                        self.num3 = float(placeholder)
                        self.display_num3.set(f"{self.num3:g}")
                        ## uses tk variables for live updating of titles and labels, also models the equation in the form of pressed button.
                        self.visual.set(
                            self.current_visual.format(
                            title=self.title,
                            x=self.display_num1.get(),
                            y=self.display_num2.get(),
                            z=self.display_num3.get()
                            )
                        )
                        ##removes label and replaces it with answer
                        self.entry.delete(0, gui.END)
                        self.label2.destroy()
                        self.entry.destroy()
                        if self.Button_Input != None:
                            self.Button_Input.destroy()
                        ##allows decimals
                        self.num1 = float(self.num1)
                        self.num2 = float(self.num2)
                        self.num3 = float(self.num3)
                        if self.label != None:
                            self.label.destroy()
                            ##gives answer and asks to save
                            if self.label != None:
                                self.label.destroy()
                                self.label = gui.Label(self.root, textvariable=self.visual, font=("Helvetica", self.Fontsize), wraplength=450)
                                self.label.place(y=20)
                            self.awnser = eval(self.question)
                            self.label2 = gui.Label(self.root, text=f"={round(self.awnser, 6):g}{self.Unit}", font=("Helvetica", 18))
                            self.label2.place(y=250)
                            self.SaveButton = gui.Button(self.root, text="Save results?", width=21, height=2, command=self.savefunction, font=("Helvetica", 14))
                            self.SaveButton.place(x=130,y=600)
                            self.SaveButton.config(activebackground="#424242")
                        return
                ##if it doesn't work, tell them to input again until valid.
                else:
                    self.label2.destroy()
                    self.label2 = gui.Label(self.root, text="Please use valid int for Z", font=("Helvetica", 14))
                    self.label2.place(y=200)
                    self.entry.delete(0, gui.END)
                    return
            ##if it doesn't work, tell them to input again until valid.
            except ValueError:
                if self.label2 != None:
                    self.label2.destroy()
                    self.label2 = gui.Label(self.root, text="Please use valid int for Z", font=("Helvetica", 14))
                    self.label2.place(y=200)
                    self.entry.delete(0, gui.END)
                    return

    def button_clicked_Volume(self):
        ##nessacairy to keep correct awnser and data for documents, changes based on either volume (^3) and surface area (^2)
        self.Unit = "Units^3"
        ##Full page removal of button and gui
        if self.label is not None:
            self.label.destroy()
        if self.Volume_button is not None:
            self.Volume_button.destroy()
        if self.Surface_button is not None:
            self.Surface_button.destroy()
        ##places all the buttons for the shapes and feeds back the command to their respective code
        self.Cube_button = gui.Button(self.root, text="Cuboid\n❒", width=21, height=10, command=self.Cube_button_clicked, font=("Helvetica", 14))
        self.Cube_button.place(x=8, y=10)
        self.Cube_button.config(activebackground="#424242")
        self.Cylinder_button = gui.Button(self.root, text="Cylinder\n🛢", width=21, height=10, command=self.Cylinder_button_clicked, font=("Helvetica", 14))
        self.Cylinder_button.place(x=252,y=10)
        self.Cylinder_button.config(activebackground="#424242")
        self.Sphere_button = gui.Button(self.root, text="Sphere\n🔵", width=21, height=10, command=self.Sphere_button_clicked, font=("Helvetica", 14))
        self.Sphere_button.place(x=8, y=250)
        self.Sphere_button.config(activebackground="#424242")
        self.Cone_button = gui.Button(self.root, text="Cone\n𓉴", width=21, height=10, command=self.Cone_button_clicked, font=("Helvetica", 14))
        self.Cone_button.place(x=252,y=250)
        self.Cone_button.config(activebackground="#424242")
        self.Square_Pyramid_button = gui.Button(self.root, text="Square Based Pyramid\n☒", width=21, height=10, command=self.SquarePyramid_button_clicked, font=("Helvetica", 14))
        self.Square_Pyramid_button.place(x=8, y=490)
        self.Square_Pyramid_button.config(activebackground="#424242")
        self.Triangle_Pyramid_button = gui.Button(self.root, text="Triangle Based Pyramid\n⛛", width=21, height=10, command=self.TrianglePyramid_button_clicked, font=("Helvetica", 14))
        self.Triangle_Pyramid_button.place(x=252,y=490)
        self.Triangle_Pyramid_button.config(activebackground="#424242")
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")

    def button_clicked_Surface(self):
        self.Unit = "Units^2"
        ##Full page removal of button and gui
        if self.label is not None:
            self.label.destroy()
        if self.Volume_button is not None:
            self.Volume_button.destroy()
        if self.Surface_button is not None:
            self.Surface_button.destroy()
        ##places all the buttons for the shapes and feeds back the command to their respective code
        self.Cube_button_Surface = gui.Button(self.root, text="Cuboid\n❒", width=21, height=10, command=self.Cube_button_Surface_clicked, font=("Helvetica", 14))
        self.Cube_button_Surface.place(x=8, y=10)
        self.Cube_button_Surface.config(activebackground="#424242")
        self.Cylinder_button_Surface = gui.Button(self.root, text="Cylinder\n🛢", width=21, height=10, command=self.Cylinder_button_Surface_clicked, font=("Helvetica", 14))
        self.Cylinder_button_Surface.place(x=252,y=10)
        self.Cylinder_button_Surface.config(activebackground="#424242")
        self.Sphere_button_Surface = gui.Button(self.root, text="Sphere\n🔵", width=21, height=10, command=self.Sphere_button_Surface_clicked, font=("Helvetica", 14))
        self.Sphere_button_Surface.place(x=8, y=250)
        self.Sphere_button_Surface.config(activebackground="#424242")
        self.Cone_button_Surface = gui.Button(self.root, text="Cone\n𓉴", width=21, height=10, command=self.Cone_button_Surface_clicked, font=("Helvetica", 14))
        self.Cone_button_Surface.place(x=252,y=250)
        self.Cone_button_Surface.config(activebackground="#424242")
        self.Square_Pyramid_button_Surface = gui.Button(self.root, text="Square Based Pyramid\n☒", width=21, height=10, command=self.SquarePyramid_button_Surface_clicked, font=("Helvetica", 14))
        self.Square_Pyramid_button_Surface.place(x=8, y=490)
        self.Square_Pyramid_button_Surface.config(activebackground="#424242")
        self.Triangle_Pyramid_button_Surface = gui.Button(self.root, text="Regular Triangle Based Pyramid\n⛛", width=21, height=10, command=self.TrianglePyramid_button_Surface_clicked, font=("Helvetica", 14), wraplength=(200))
        self.Triangle_Pyramid_button_Surface.place(x=252,y=490)
        self.Triangle_Pyramid_button_Surface.config(activebackground="#424242")
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")

    def Cube_button_clicked(self):
        self.question = self.Cube_Volume_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Cube Volume ="
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for X", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Cube Volume =\nX*Y*Z", font=("Helvetica", 50))
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}{x}*{y}*{z}"
        ##places image
        IMG = gui.Label(self.root, image=self.cube_img)
        IMG.place(x=125, y=360)

    def Cylinder_button_clicked(self):
        self.question = self.Cylinder_Volume_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Cylinder Volume ="
        ##sets num to the required without user input
        self.num1 = round(math.pi, 4)
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for Y", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Cylinder Volume =\nπ*X*Y^2", font=("Helvetica", 40))
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}π*{y}*{z}^2"
        ##places image
        IMG = gui.Label(self.root, image=self.cylinder_img)
        IMG.place(x=110, y=320)

    def Sphere_button_clicked(self):
        self.question = self.Sphere_Volume_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Sphere Volume ="
        ##sets num to the required without user input
        self.num2 = round(math.pi, 4)
        self.num1 = round(4/3, 5)
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for Z", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Sphere Volume =\nπ*(4/3)*Z**3", font=("Helvetica", 45))
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}π*(4/3)*{z}^3"
        ##places image
        IMG = gui.Label(self.root, image=self.sphere_img)
        IMG.place(x=125, y=360)

    def Cone_button_clicked(self): ##Working
        self.question = self.Cone_Volume_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Cone Volume ="
        ##sets num to the required without user input
        self.num1 = round(math.pi, 4)
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for Y", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Cone Volume =\nπ*(Y**2)*(Z/3)", font=("Helvetica", 40))
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}π*({y}^2)*({z}/3)"
        ##places image
        IMG = gui.Label(self.root, image=self.cone_img)
        IMG.place(x=130, y=340)

    def SquarePyramid_button_clicked(self): ##Working
        self.question = self.Square_Pyramid_Volume_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Square Pyramid Volume = ("
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for X", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Square Pyramid Volume =(X*Y*Z)/3", font=("Helvetica", 32), wraplength=500)
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}{x}*{y}*{z})/3"
        ##Places image
        IMG = gui.Label(self.root, image=self.pyramid_square_img)
        IMG.place(x=130, y=340)

    def TrianglePyramid_button_clicked(self): ##Working
        self.question = self.Triangle_Pyramid_Volume_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Triangle Pyramid Volume = (0.5*"
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for X", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Triangle Pyramid Volume =(0.5*X*Y*Z)/3", font=("Helvetica", 32), wraplength=500)
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}{x}*{y}*{z})/3"
        ##places image
        IMG = gui.Label(self.root, image=self.pyramid_triangle_img)
        IMG.place(x=115, y=360)

    def Cube_button_Surface_clicked(self):
        self.question = self.Cube_Surface_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Cube Surface Area ="
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for X", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Cube Volume =\n2*(X*Y+X*Z+Y*Z)", font=("Helvetica", 40))
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}2*({x}*{y}+{x}*{z}+{y}*{z})"
        ##places image
        IMG = gui.Label(self.root, image=self.cube_img)
        IMG.place(x=125, y=360)

    def Cylinder_button_Surface_clicked(self):
        self.question = self.Cylinder_Surface_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Cylinder Surface Area ="
        ##sets num to the required without user input
        self.num1 = round(math.pi, 4)
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for Y", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Cylinder Surface Area =\n2π*Y*Z+2π*Y^2", font=("Helvetica", 30))
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##sets num to the required without user input
        ##formats equation
        self.current_visual = "{title}2π*{y}*{z}+2π*{y}^2"
        ##Places image
        IMG = gui.Label(self.root, image=self.cylinder_img)
        IMG.place(x=110, y=320)

    def Sphere_button_Surface_clicked(self):
        self.question = self.Sphere_Surface_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Sphere Surface Area ="
        ##sets num to the required without user input
        self.num2 = round(math.pi, 4)
        self.num1 = 4
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for Z", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Sphere Surface Area =\n4*π*Z^2", font=("Helvetica", 35))
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}4*π*{z}^2"
        ##places image
        IMG = gui.Label(self.root, image=self.sphere_img)
        IMG.place(x=125, y=360)

    def Cone_button_Surface_clicked(self):
        self.question = self.Cone_Surface_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Cone Surface Area ="
        ##sets num to the required without user input
        self.num1 = round(math.pi, 4)
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for Y", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Cone Surface Area =\nπ*Y*(Y+(Z**2+Y**2)**0.5)", font=("Helvetica", 25))
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}π*{y}*({y}+({z}**2+{y}**2)**0.5)"
        ##places image
        IMG = gui.Label(self.root, image=self.cone_img)
        IMG.place(x=130, y=340)

    def SquarePyramid_button_Surface_clicked(self): ##Working
        self.question = self.Square_Pyramid_Surface_Formula ##use this to set what button and equation instead of making a new submit function for each.
        ##sets font size so equation fits
        self.Fontsize = 20
        self.title = "Square Pyramid Surface Area ="
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for X", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Square Pyramid Surface Area =Y*X+Y*((X/2)^2+Z^2)^0.5+X*((Y/2)^2+Z^2)^0.5", font=("Helvetica", 20), wraplength=440)
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}{y}*{x}+{y}*(({x}/2)^2+{z}^2)^0.5+{x}*(({y}/2)^2+{z}^2)^0.5"
        ##Places image
        IMG = gui.Label(self.root, image=self.pyramid_square_img)
        IMG.place(x=130, y=340)

    def TrianglePyramid_button_Surface_clicked(self): ##working
        self.question = self.Triangle_Pyramid_Surface_Formula ##use this to set what button and equation instead of making a new submit function for each.
        self.title = "Triangle Pyramid Surface Area ="
        ##Full page removal of button and gui
        for widget in self.root.winfo_children():
            widget.destroy()
        ##intializes the calculator input box for use
        self.label2 = gui.Label(self.root, text="Please type value for X", font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text="Triangle Pyramid Surface Area =0.5*(X*Y)+3/2*(Y*Z)", font=("Helvetica", 32), wraplength=500)
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)
        ##Button that resets back to inital state
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")
        ##formats equation
        self.current_visual = "{title}0.5*({x}*{y})+3/2*({y}*{z})"
        ##places image
        IMG = gui.Label(self.root, image=self.pyramid_triangle_img)
        IMG.place(x=115, y=360)

    ##window icon
    myappid = 'mycompany.myproduct.subproduct.version' # unique string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    ##root.iconbitmap(img)

##this starts and complies it all, mainly gui.
calculator = Calculator()
calculator.root.mainloop()