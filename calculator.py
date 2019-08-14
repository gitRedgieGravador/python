# Calculator made using pythons tkinter module
# Author - Mohamed Akil

from tkinter import *
import math

class Application(Frame):
    """ Main class for calculator"""

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create all the buttons for calculator. """
        # User input stored as an Entry widget.

        self.user_input = Entry(self, bg = "#5BC8AC", bd = 20, 
        insertwidth = 8, width = 20,
        font = ("Verdana", 20, "bold"), textvariable = self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 100)

        self.user_input.insert(0, "0")

        # Button for value 7
        self.button1 = Button(self, bg = "#98DBC6", bd = 4,
        text = "7", padx = 5, pady = 10, font = ("Helvetica", 20, "bold"), 
        command = lambda : self.buttonClick(7),height=1, width=5)
        self.button1.grid(row = 6, column = 0, sticky = W)

        # Button for value 8
        self.button2 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "8",  padx = 5, pady = 10, 
        command = lambda : self.buttonClick(8),height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button2.grid(row = 6, column = 1, sticky = W)

        # Button for value 9
        self.button3 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "9",  padx = 5, pady = 10,
        command = lambda : self.buttonClick(9),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.button3.grid(row = 6, column = 2, sticky = W)

        # Button for value 4
        self.button4 = Button(self, bg = "#98DBC6", bd = 4,
        text = "4",  padx = 5, pady = 10,
        command = lambda : self.buttonClick(4),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.button4.grid(row = 5, column = 0, sticky = W)

        # Button for value 5
        self.button5 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "5",  padx = 5, pady = 10,
        command = lambda : self.buttonClick(5),height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button5.grid(row = 5, column = 1, sticky = W)

        # Button for value 6
        self.button6 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "6",  padx = 5, pady = 10,
        command = lambda : self.buttonClick(6), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button6.grid(row = 5, column = 2, sticky = W)

        # Button for value 1
        self.button7 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "1",  padx = 5, pady = 10, 
        command = lambda : self.buttonClick(1), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button7.grid(row = 4, column = 0, sticky = W)

        # Button for value 2
        self.button8 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "2",  padx = 5, pady = 10,
        command = lambda : self.buttonClick(2),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.button8.grid(row = 4, column = 1, sticky = W)

        # Button for value 3
        self.button9 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "3",  padx = 5, pady = 10,
        command = lambda : self.buttonClick(3), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 4, column = 2, sticky = W)

        # Button for value 0
        self.button9 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "0",  padx = 5, pady = 10,
        command = lambda : self.buttonClick(0), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 7, column = 0, sticky = W)

        # Operator buttons
        # Addition button
        self.Addbutton = Button(self, bg = "#98DBC6", bd = 4, 
        text = "+",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("+"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Addbutton.grid(row = 4, column = 3, sticky = W)

        # Subtraction button
        self.Subbutton = Button(self, bg = "#98DBC6", bd = 4, 
        text = "-",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("-"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Subbutton.grid(row = 5, column = 3, sticky = W)

        # Multiplication button
        self.Multbutton = Button(self, bg = "#98DBC6", bd = 4, 
        text = "*",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("*"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Multbutton.grid(row = 6, column = 3, sticky = W)

        # Division button
        self.Divbutton = Button(self, bg = "#98DBC6", bd = 4, 
        text = "/",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("/"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Divbutton.grid(row = 7, column = 3, sticky = W)

        # Equal button
        self.Equalbutton = Button(self, bg = "#E6D72A", bd = 4, 
        text = "=",  padx = 8, pady = 10,
        command = self.CalculateTask, height=1, width=11, font = ("Helvetica", 20, "bold"))
        self.Equalbutton.grid(row = 7, column = 1, columnspan = 100,sticky = W)

        # Clear Button
        self.Clearbutton = Button(self, bg = "#E6D72A", bd = 4,
        text = "AC",  font = ("Helvetica", 20, "bold"), width = 5, padx = 5, pady = 10, command = self.ClearDisplay)
        self.Clearbutton.grid(row = 1, column = 3, sticky = W)

        # Delete Button
        self.Clearbutton = Button(self, bg = "#E6D72A", bd = 4,
        text = "Del",  font = ("Helvetica", 20, "bold"), width = 5, padx = 5, pady = 10, command = self.Ans)
        self.Clearbutton.grid(row = 2, column = 3, sticky = W)

        #square root button
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "√",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("√"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 2, column = 0, sticky = W)

        #factorial button
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "x!",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("!"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 2, column = 1, sticky = W)

        #Exponent button
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "Exp",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("^"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 3, column = 0, sticky = W)

        #squared button
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "x²",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("²"),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 1, column = 0, sticky = W)

        #floored division button
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "//",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("//"),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 2, column = 2, sticky = W)

        #modulo button
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "%",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("%"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 1, column = 2, sticky = W)

        #cube button
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "x³",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("³"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 1, column = 1, sticky = W)

        #Permutaion
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "nPr",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("P"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 3, column = 1, sticky = W)

        #Combination
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "nCr",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("C"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 3, column = 2, sticky = W)

        #tan
        self.sqrt = Button(self, bg = "#98DBC6", bd = 4, 
        text = "tan",  padx = 5, pady = 10,
        command = lambda : self.buttonClick("tan"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 3, column = 3, sticky = W)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            if str(self.data)[0].isdigit()==False:#square root
                operation =  str(self.data)[0]
                digit = str(self.data)[1:]
                if operation == "√":
                    self.answer = int(digit)**0.5
                    self.displayText(self.answer)
                    self.task = self.answer
                    
            elif str(self.data)[-1]== "!":#for factorial
                self.answer = math.factorial(int(str(self.data)[:-1]))
                self.displayText(self.answer)
                self.task = self.answer
                
            elif "^" in str(self.data):#for exponent
                i = str(self.data).index("^")
                self.answer = int(str(self.data)[:i])**int(str(self.data)[i+1:])
                self.displayText(self.answer)
                self.task = self.answer
                
            elif "²" in str(self.data):#for squared
                self.answer = int(str(self.data)[:-1])**2
                self.displayText(self.answer)
                self.task = self.answer
                
            elif "//" in str(self.data):#for floored division
                i = str(self.data).index("/")
                self.answer = int(str(self.data)[:i])//int(str(self.data)[i+2:])
                self.displayText(self.answer)
                self.task = self.answer
                
            elif "%" in str(self.data):#for modulo
                i = str(self.data).index("%")
                self.answer = int(str(self.data)[:i])%int(str(self.data)[i+1:])
                self.displayText(self.answer)
                self.task = self.answer

            elif "³" in str(self.data):#for cube
                self.answer = int(str(self.data)[:-1])**3
                self.displayText(self.answer)
                self.task = self.answer

            elif "P" in str(self.data):#condition for Permutation
                i = str(self.data).index("P")
                self.answer = math.factorial(int(str(self.data)[:i]))/math.factorial((int(str(self.data)[:i]))-(int(str(self.data)[i+1:])))
                self.displayText(self.answer)
                self.task = self.answer

            elif "C" in str(self.data):#condition for Combination
                i = str(self.data).index("C")
                n = str(self.data)[:i]
                r = str(self.data)[i+1]
                self.answer = math.factorial(int(n))/math.factorial(int(r))*math.factorial(int(r))
                self.displayText(self.answer)
                self.task = self.answer


            else:
                self.answer = eval(self.data)
                self.displayText(self.answer)
                self.task = self.answer

        except SyntaxError as e:
            self.displayText("Invalid Syntax!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

    def Ans(self):
        self.UserIn.set(self.task)


calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)
# Make window fixed (cannot be resized)
calculator.resizable(width = False, height = False)

calculator.mainloop()
