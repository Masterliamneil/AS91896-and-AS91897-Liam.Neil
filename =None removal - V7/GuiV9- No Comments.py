import tkinter as gui
from datetime import datetime
import math

class Calculator:

    Back_Button = None
    pi = math.pi
    Cube_Volume_Formula = 'self.num1*self.num2*self.num3'
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
        self.root = gui.Tk()
        self.root.title("Shape Surface Area and Volume Calculator")
        self.root.geometry("500x800") 
        self.root.resizable(False, False)
        img = gui.PhotoImage(file="Allsixes.png")
        self.root.iconphoto(True, img)
        self.resetfunction()

        self.cube_img = gui.PhotoImage(file="Cube.png")
        self.cylinder_img = gui.PhotoImage(file="CylinderVolume.png")
        self.sphere_img = gui.PhotoImage(file="Sphere.png")
        self.cone_img = gui.PhotoImage(file="Cone.png")
        self.pyramid_square_img = gui.PhotoImage(file="PyramidSquare.png")
        self.pyramid_triangle_img = gui.PhotoImage(file="TrianglePryamid.png")

    def savefunction(self):
        solution = self.visual.get()
        default = f"calc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        content = f"{solution}\n={self.awnser:g}{self.Unit}"
        with open(default, "w", encoding="utf-8") as text_file:
            text_file.write(content)

    def Menu_Buttons(self):
        Volume_button = gui.Button(self.root, font=("Helvetica", 19), text="Volume", width=15, height=21, command=self.button_clicked_Volume)
        Volume_button.place(x=10, y=180)
        Volume_button.config(activebackground="#424242")
        Surface_button = gui.Button(self.root, font=("Helvetica", 19), text="Surface Area", width=15, height=21, command=self.button_clicked_Surface)
        Surface_button.place(x=260, y=180)
        Surface_button.config(activebackground="#424242")
        self.label = gui.Label(self.root, text="What would you like to calculate?", font=("Helvetica", 25))
        self.label.pack(pady=20)

    def resetfunction(self):
        if self.Back_Button != None:
            self.Back_Button.destroy()
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
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Menu_Buttons()

    def Visual_Title(self):
        self.visual.set(
            self.current_visual.format(
            title=self.title,
            x=self.display_num1.get(),
            y=self.display_num2.get(),
            z=self.display_num3.get()
            )
        )

    def Visual_Message(self, message):
        if self.label2 != None:
            self.label2.destroy()
            self.label2 = gui.Label(self.root, text=message, font=("Helvetica", 14))
            self.label2.place(y=200)
            self.entry.delete(0, gui.END)

    def Current_Equation(self):
        if self.label != None:
            self.label.destroy()
            self.label = gui.Label(self.root, textvariable=self.visual, font=("Helvetica", self.Fontsize), wraplength=450)
            self.label.place(y=20)
            self.entry.delete(0, gui.END)

    def Back_Menu_Button(self):
        self.Back_Button = gui.Button(self.root, text="Back", width=43, height=2, command=self.resetfunction, font=("Helvetica", 14))
        self.Back_Button.place(x=8,y=730)
        self.Back_Button.config(activebackground="#424242")

    def Menu_Button_format(self, Shape, Shape_Command, Place_X, Place_Y):
        self.Menu_Button = gui.Button(self.root, text=Shape, width=21, height=10, command=Shape_Command, font=("Helvetica", 14), wraplength=(200))
        self.Menu_Button.place(x=Place_X,y=Place_Y)
        self.Menu_Button.config(activebackground="#424242")

    def Intial_Equation_Menu(self, Text_A, Text_B):
        self.label2 = gui.Label(self.root, text=Text_A, font=("Helvetica", 14))
        self.label2.place(y=200)
        self.label = gui.Label(self.root, text=Text_B, font=("Helvetica", 32), wraplength=500)
        self.label.place(y=20)
        self.entry = gui.Entry(self.root, width=20, font=("Helvetica", 20))
        self.entry.place(x=21, y=250)
        self.entry.bind("<Return>", self.submit)
        self.Button_Input = gui.Button(self.root, text="Submit", command=self.submit, height=2, width=15)
        self.Button_Input.place(x=345,y=250)

    def submit(self, event=None):
        placeholder = self.entry.get()
        if self.num1 == "X":
            try:
                placeholder = self.entry.get()
                placeholder = float(placeholder)
                if placeholder > 0:
                    if isinstance(placeholder, (int, float)):
                        self.num1 = float(placeholder)
                        self.display_num1.set(f"{self.num1:g}")
                        self.Visual_Title()
                        if self.label2 != None:
                            self.Visual_Message("Please type value for Y")
                            self.Current_Equation()
                            return
                else:
                    self.Visual_Message("Please use valid int for X")
                    return
            except ValueError:
                self.Visual_Message("Please use valid int for X")
                return
        elif self.num2 == "Y":
            try:
                placeholder = self.entry.get()
                placeholder = float(placeholder)
                if placeholder > 0:
                    if isinstance(placeholder, (int, float)):
                        self.num2 = float(placeholder)
                        self.display_num2.set(f"{self.num2:g}")
                        self.Visual_Title()
                        if self.label2 != None:
                            self.Visual_Message("Please type value for Z")
                            if self.label != None:
                                self.Current_Equation()
                                return
                else:
                    self.Visual_Message("Please use valid int for Y")
                    return
            except ValueError:
                self.Visual_Message("Please use valid int for Y")
                return
        elif self.num3 == "Z":
            try:
                placeholder = self.entry.get()
                placeholder = float(placeholder)
                if placeholder > 0:
                    if isinstance(placeholder, (int, float)):
                        self.num3 = float(placeholder)
                        self.display_num3.set(f"{self.num3:g}")
                        self.Visual_Title()
                        self.entry.delete(0, gui.END)
                        self.label2.destroy()
                        self.entry.destroy()
                        if self.Button_Input != None:
                            self.Button_Input.destroy()
                        self.num1 = float(self.num1)
                        self.num2 = float(self.num2)
                        self.num3 = float(self.num3)
                        if self.label != None:
                            self.label.destroy()
                            self.label = gui.Label(self.root, textvariable=self.visual, font=("Helvetica", self.Fontsize), wraplength=450)
                            self.label.place(y=20)
                            self.awnser = eval(self.question)
                            self.label2 = gui.Label(self.root, text=f"={round(self.awnser, 6):g}{self.Unit}", font=("Helvetica", 18))
                            self.label2.place(y=250)
                            SaveButton = gui.Button(self.root, text="Save results?", width=21, height=2, command=self.savefunction, font=("Helvetica", 14))
                            SaveButton.place(x=130,y=600)
                            SaveButton.config(activebackground="#424242")
                        return
                else:
                    self.Visual_Message("Please use valid int for Z")
                    return
            except ValueError:
                self.Visual_Message("Please use valid int for Z")
                return

    def button_clicked_Volume(self):
        self.Unit = "Units^3"
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Menu_Button_format(Shape="Cuboid\n❒",Shape_Command=self.Cube_button_clicked, Place_X=8, Place_Y=10)
        self.Menu_Button_format(Shape="Cylinder\n🛢" ,Shape_Command=self.Cylinder_button_clicked, Place_X=252, Place_Y=10)
        self.Menu_Button_format(Shape="Sphere\n🔵" ,Shape_Command=self.Sphere_button_clicked, Place_X=8, Place_Y=250)
        self.Menu_Button_format(Shape="Cone\n𓉴" ,Shape_Command=self.Cone_button_clicked, Place_X=252, Place_Y=250)
        self.Menu_Button_format(Shape="Square Based Pyramid\n☒" ,Shape_Command=self.SquarePyramid_button_clicked, Place_X=8, Place_Y=490)
        self.Menu_Button_format(Shape="Regular Triangle Based Pyramid\n⛛" ,Shape_Command=self.TrianglePyramid_button_clicked, Place_X=252, Place_Y=490) 
        self.Back_Menu_Button()

    def button_clicked_Surface(self):
        self.Unit = "Units^2"
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Menu_Button_format(Shape="Cuboid\n❒",Shape_Command=self.Cube_button_Surface_clicked, Place_X=8, Place_Y=10)
        self.Menu_Button_format(Shape="Cylinder\n🛢" ,Shape_Command=self.Cylinder_button_Surface_clicked, Place_X=252, Place_Y=10)
        self.Menu_Button_format(Shape="Sphere\n🔵" ,Shape_Command=self.Sphere_button_Surface_clicked, Place_X=8, Place_Y=250)
        self.Menu_Button_format(Shape="Cone\n𓉴" ,Shape_Command=self.Cone_button_Surface_clicked, Place_X=252, Place_Y=250)
        self.Menu_Button_format(Shape="Square Based Pyramid\n☒" ,Shape_Command=self.SquarePyramid_button_Surface_clicked, Place_X=8, Place_Y=490)
        self.Menu_Button_format(Shape="Regular Triangle Based Pyramid\n⛛" ,Shape_Command=self.TrianglePyramid_button_Surface_clicked, Place_X=252, Place_Y=490) 
        self.Back_Menu_Button()

    def Cube_button_clicked(self):
        self.question = self.Cube_Volume_Formula
        self.title = "Cube Volume ="
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for X", Text_B="Cube Volume =\nX*Y*Z")
        self.Back_Menu_Button()
        self.current_visual = "{title}{x}*{y}*{z}"
        IMG = gui.Label(self.root, image=self.cube_img)
        IMG.place(x=125, y=360)

    def Cylinder_button_clicked(self):
        self.question = self.Cylinder_Volume_Formula
        self.title = "Cylinder Volume ="
        self.num1 = round(math.pi, 4)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for Y", Text_B="Cylinder Volume =\nπ*X*Y^2")
        self.Back_Menu_Button()
        self.current_visual = "{title}π*{y}*{z}^2"
        IMG = gui.Label(self.root, image=self.cylinder_img)
        IMG.place(x=110, y=320)

    def Sphere_button_clicked(self):
        self.question = self.Sphere_Volume_Formula
        self.title = "Sphere Volume ="
        self.num2 = round(math.pi, 4)
        self.num1 = round(4/3, 5)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for Z", Text_B="Sphere Volume =\nπ*(4/3)*Z**3")
        self.Back_Menu_Button()
        self.current_visual = "{title}π*(4/3)*{z}^3"
        IMG = gui.Label(self.root, image=self.sphere_img)
        IMG.place(x=125, y=360)

    def Cone_button_clicked(self): 
        self.question = self.Cone_Volume_Formula
        self.title = "Cone Volume ="
        self.num1 = round(math.pi, 4)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for Y", Text_B="Cone Volume =\nπ*(Y**2)*(Z/3)")
        self.Back_Menu_Button()
        self.current_visual = "{title}π*({y}^2)*({z}/3)"
        IMG = gui.Label(self.root, image=self.cone_img)
        IMG.place(x=130, y=340)

    def SquarePyramid_button_clicked(self): 
        self.question = self.Square_Pyramid_Volume_Formula
        self.title = "Square Pyramid Volume = ("
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for X", Text_B="Square Pyramid Volume =(X*Y*Z)/3")
        self.Back_Menu_Button()
        self.current_visual = "{title}{x}*{y}*{z})/3"
        IMG = gui.Label(self.root, image=self.pyramid_square_img)
        IMG.place(x=130, y=340)

    def TrianglePyramid_button_clicked(self): 
        self.question = self.Triangle_Pyramid_Volume_Formula
        self.title = "Triangle Pyramid Volume = (0.5*"
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for X", Text_B="Triangle Pyramid Volume =(0.5*X*Y*Z)/3")
        self.Back_Menu_Button()
        self.current_visual = "{title}{x}*{y}*{z})/3"
        IMG = gui.Label(self.root, image=self.pyramid_triangle_img)
        IMG.place(x=115, y=360)

    def Cube_button_Surface_clicked(self):
        self.question = self.Cube_Surface_Formula
        self.title = "Cube Surface Area ="
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for X", Text_B="Cube Volume =\n2*(X*Y+X*Z+Y*Z)")
        self.Back_Menu_Button()
        self.current_visual = "{title}2*({x}*{y}+{x}*{z}+{y}*{z})"
        IMG = gui.Label(self.root, image=self.cube_img)
        IMG.place(x=125, y=360)

    def Cylinder_button_Surface_clicked(self):
        self.question = self.Cylinder_Surface_Formula
        self.title = "Cylinder Surface Area ="
        self.num1 = round(math.pi, 4)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for Y", Text_B="Cylinder Surface Area =\n2π*Y*Z+2π*Y^2")
        self.Back_Menu_Button()
        self.current_visual = "{title}2π*{y}*{z}+2π*{y}^2"
        IMG = gui.Label(self.root, image=self.cylinder_img)
        IMG.place(x=110, y=320)

    def Sphere_button_Surface_clicked(self):
        self.question = self.Sphere_Surface_Formula
        self.title = "Sphere Surface Area ="
        self.num2 = round(math.pi, 4)
        self.num1 = 4
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for Z", Text_B="Sphere Surface Area =\n4*π*Z^2")
        self.Back_Menu_Button()
        self.current_visual = "{title}4*π*{z}^2"
        IMG = gui.Label(self.root, image=self.sphere_img)
        IMG.place(x=125, y=360)

    def Cone_button_Surface_clicked(self):
        self.question = self.Cone_Surface_Formula
        self.title = "Cone Surface Area ="
        self.num1 = round(math.pi, 4)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for Y", Text_B="Cone Surface Area =\nπ*Y*(Y+(Z**2+Y**2)**0.5)")
        self.Back_Menu_Button()
        self.current_visual = "{title}π*{y}*({y}+({z}**2+{y}**2)**0.5)"
        IMG = gui.Label(self.root, image=self.cone_img)
        IMG.place(x=130, y=340)

    def SquarePyramid_button_Surface_clicked(self): 
        self.question = self.Square_Pyramid_Surface_Formula
        self.Fontsize = 20
        self.title = "Square Pyramid Surface Area ="
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for X", Text_B="Square Pyramid Surface Area =Y*X+Y*((X/2)^2+Z^2)^0.5+X*((Y/2)^2+Z^2)^0.5")
        self.Back_Menu_Button()
        self.current_visual = "{title}{y}*{x}+{y}*(({x}/2)^2+{z}^2)^0.5+{x}*(({y}/2)^2+{z}^2)^0.5"
        IMG = gui.Label(self.root, image=self.pyramid_square_img)
        IMG.place(x=130, y=340)

    def TrianglePyramid_button_Surface_clicked(self): 
        self.question = self.Triangle_Pyramid_Surface_Formula
        self.title = "Triangle Pyramid Surface Area ="
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Intial_Equation_Menu(Text_A="Please type value for X", Text_B="Triangle Pyramid Surface Area =0.5*(X*Y)+3/2*(Y*Z)")
        self.Back_Menu_Button()
        self.current_visual = "{title}0.5*({x}*{y})+3/2*({y}*{z})"
        IMG = gui.Label(self.root, image=self.pyramid_triangle_img)
        IMG.place(x=115, y=360)

calculator = Calculator()
calculator.root.mainloop()