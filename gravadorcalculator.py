# Calculator made using pythons tkinter module
# Author - Redgie Gravador (Pn Class 2021)

from tkinter import *
import math


class Application(Frame):
    """ Main class for calculator
        This is a scientific calculator
        Operations :
          Basic Operations
            (+) >> addition
            (-) >> Subtraction
            (*) >> multiplication
            (/) >> division
          Scientific Operations
            (√)  >> Square root
                 - to use click (√ button, number button, = button)
            (!)  >> factorial
                 - to use click (number button, ! button, = button)
            (x²) >> Squared
                 - to use click (number button/s , x² button , = button)
            (x³) >> Cube
                 - to use click (number button/s , x³ button , = button)
            (%)  >> Modulo
                 - to use click (divident number button/s , % button , divisor number button,  = button)
            
            (//) >> Floored division
                 - to use click (divident number button/s , // button , divisor number button,  = button)
            (Exp)>> Exponential
                 - to use click (base number button, Exp button, exponent number button, = button)
            (nPr)>> Permutaion
                 - n >> numbers of things to choose from
                 - r >> number of repeatations allowed
                 - to use click (n number button, nPr button, r number button)
            (nCr)>> Combination
                 - n >> numbers of things to choose from
                 - r >> number of repeatations allowed
                 - to use click (n number button, nCr button, r number button)
            (nBr)>> Probability
                 - n >> numbers of things to choose from a set 
                 - r >> total number of things to choose from
                 - to use click (n number button, nBr button, r number button)
            
        Excemptions and Limitations:
                1. This calculator do not perform more than one scientific operations
                in a row.
                2. This calculator do not evaluate a series of expression if a scientific operation
                is present in the series of expression.
                3. If addition and subtraction comes a couple of times in a row
                   this calculator will evaluate the expression mathematically and will conseder the preceeding operation as sign of the numbner.
                4. Do not put any operation inside the radical sign
                5. Do not use a scientific operation as suboperation
            
            """

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
        insertwidth = 8, width = 18,
        font = ("Verdana", 20, "bold"), textvariable = self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 100)

        self.user_input.insert(0, "0")

        # Button for value 7
        self.button1 = Button(self, bg = "#98DBC6", bd = 4,
        text = "7", padx = 1, pady = 2, font = ("Helvetica", 20, "bold"), 
        command = lambda : self.buttonClick(7),height=1, width=5)
        self.button1.grid(row = 6, column = 0, sticky = W)

        # Button for value 8
        self.button2 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "8",  padx = 1, pady = 2, 
        command = lambda : self.buttonClick(8),height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button2.grid(row = 6, column = 1, sticky = W)

        # Button for value 9
        self.button3 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "9",  padx = 1, pady = 2,
        command = lambda : self.buttonClick(9),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.button3.grid(row = 6, column = 2, sticky = W)

        # Button for value 4
        self.button4 = Button(self, bg = "#98DBC6", bd = 4,
        text = "4",  padx = 1, pady = 2,
        command = lambda : self.buttonClick(4),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.button4.grid(row = 5, column = 0, sticky = W)

        # Button for value 5
        self.button5 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "5",  padx = 1, pady = 2,
        command = lambda : self.buttonClick(5),height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button5.grid(row = 5, column = 1, sticky = W)

        # Button for value 6
        self.button6 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "6",  padx = 1, pady = 2,
        command = lambda : self.buttonClick(6), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button6.grid(row = 5, column = 2, sticky = W)

        # Button for value 1
        self.button7 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "1",  padx = 1, pady = 2, 
        command = lambda : self.buttonClick(1), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button7.grid(row = 4, column = 0, sticky = W)

        # Button for value 2
        self.button8 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "2",  padx = 1, pady = 2,
        command = lambda : self.buttonClick(2),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.button8.grid(row = 4, column = 1, sticky = W)

        # Button for value 3
        self.button9 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "3",  padx = 1, pady = 2,
        command = lambda : self.buttonClick(3), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 4, column = 2, sticky = W)

        # Button for value 0
        self.button9 = Button(self, bg = "#98DBC6", bd = 4, 
        text = "0",  padx = 1, pady = 2,
        command = lambda : self.buttonClick(0), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 7, column = 0, sticky = W)

        # Button for value Period
        self.button9 = Button(self, bg = "#98DBC6", bd = 4, 
        text = ".",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("."), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 7, column = 1, sticky = W)

        # Operator buttons
        # Addition button
        self.Addbutton = Button(self, bg = "#F0E3F0", bd = 4, 
        text = "+",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("+"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Addbutton.grid(row = 4, column = 3, sticky = W)

        # Subtraction button
        self.Subbutton = Button(self, bg = "#F0E3F0", bd = 4, 
        text = "-",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("-"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Subbutton.grid(row = 5, column = 3, sticky = W)

        # Multiplication button
        self.Multbutton = Button(self, bg = "#F0E3F0", bd = 4, 
        text = "*",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("*"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Multbutton.grid(row = 6, column = 3, sticky = W)

        # Division button
        self.Divbutton = Button(self, bg = "#F0E3F0", bd = 4, 
        text = "/",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("/"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Divbutton.grid(row = 7, column = 3, sticky = W)

        # Equal button
        self.Equalbutton = Button(self, bg = "#E6D72A", bd = 4, 
        text = "=",  padx = 1, pady = 2,
        command = self.CalculateTask, height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.Equalbutton.grid(row = 7, column = 2,sticky = W)

        # Clear Button
        self.Clearbutton = Button(self, bg = "#E6D72A", bd = 4,
        text = "AC",  font = ("Helvetica", 20, "bold"), width = 5, padx = 1, pady = 2, command = self.ClearDisplay)
        self.Clearbutton.grid(row = 1, column = 3, sticky = W)

        # Delete Button
        self.Clearbutton = Button(self, bg = "#E6D72A", bd = 4,
        text = "Del",  font = ("Helvetica", 20, "bold"), width = 5, padx = 1, pady = 2, command = self.Del)
        self.Clearbutton.grid(row = 2, column = 3, sticky = W)

        #square root button
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "√",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("√"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 2, column = 0, sticky = W)

        #factorial button
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "x!",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("!"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 2, column = 1, sticky = W)

        #Exponent button
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "Exp",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("^"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 3, column = 0, sticky = W)

        #squared button
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "x²",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("²"),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 1, column = 0, sticky = W)

        #floored division button
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "//",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("//"),height=1, width=5,  font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 2, column = 2, sticky = W)

        #modulo button
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "%",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("%"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 1, column = 2, sticky = W)

        #cube button
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "x³",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("³"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 1, column = 1, sticky = W)

        #Permutaion
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "nPr",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("P"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 3, column = 1, sticky = W)

        #Combination
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "nCr",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("C"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 3, column = 2, sticky = W)

        #Probability Button
        self.sqrt = Button(self, bg = "#B7C4C0", bd = 4, 
        text = "pBc",  padx = 1, pady = 2,
        command = lambda : self.buttonClick("B"), height=1, width=5, font = ("Helvetica", 20, "bold"))
        self.sqrt.grid(row = 3, column = 3, sticky = W)

    def buttonClick(self, number):
        """Add the respective value of the clicked button to the user inputs"""
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        """Performs the operations
            or evaluate the user input in regards with the Excemptions and Limitation defined above"""
        self.data = self.user_input.get()
        try:
            #square root
            if "√" in str(self.data):
                operation =  str(self.data)[0]
                digit = str(self.data)[1:]
                self.answer = int(digit)**0.5
                self.displayText(self.answer)
                self.task = self.answer

            #for factorial        
            elif str(self.data)[-1]== "!":
                self.answer = math.factorial(int(str(self.data)[:-1]))
                self.displayText(self.answer)
                self.task = self.answer
            
            #for exponent    
            elif "^" in str(self.data):
                i = str(self.data).index("^")
                self.answer = int(str(self.data)[:i])**int(str(self.data)[i+1:])
                self.displayText(self.answer)
                self.task = self.answer
            
            #for squared    
            elif "²" in str(self.data):
                self.answer = int(str(self.data)[:-1])**2
                self.displayText(self.answer)
                self.task = self.answer
            
            #for floored division    
            elif "//" in str(self.data):
                i = str(self.data).index("/")
                self.answer = int(str(self.data)[:i])//int(str(self.data)[i+2:])
                self.displayText(self.answer)
                self.task = self.answer
                
            #for modulo    
            elif "%" in str(self.data):
                i = str(self.data).index("%")
                self.answer = int(str(self.data)[:i])%int(str(self.data)[i+1:])
                self.displayText(self.answer)
                self.task = self.answer
            
            #for cube
            elif "³" in str(self.data):
                self.answer = int(str(self.data)[:-1])**3
                self.displayText(self.answer)
                self.task = self.answer
              
            #condition for Permutation
            elif "P" in str(self.data):
                i = str(self.data).index("P")
                self.answer = math.factorial(int(str(self.data)[:i]))/math.factorial((int(str(self.data)[:i]))-(int(str(self.data)[i+1:])))
                self.displayText(self.answer)
                self.task = self.answer

            #condition for Combination
            elif "C" in str(self.data):
                i = str(self.data).index("C")
                n = str(self.data)[:i]
                r = str(self.data)[i+1]
                self.answer = math.factorial(int(n))/math.factorial(int(r))*math.factorial(int(r))
                self.displayText(self.answer)
                self.task = self.answer

            #condition for Probability
            elif "B" in str(self.data):
                i = str(self.data).index("B")
                p = str(self.data)[:i]
                c = str(self.data)[i+1:]
                self.answer = int(p)/int(c)
                self.displayText(self.answer)
                self.task = self.answer


            else:
                #Perform the series of operation with the 4 basic operations
                self.answer = eval(self.data)
                self.displayText(self.answer)
                self.task = self.answer

        except SyntaxError as e:
            #Addresses the user that he/she has made an invalid syntax
            self.displayText("Invalid Syntax!")
            self.task = ""

    def displayText(self, value):
        """This will display the user input data"""
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        """This will clear the user inputs"""
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

    def Del(self):
        """This will remove the last element of the user inputs
            Limitations:
                - Will not function when click in a row,
                if click in row this will only execute the first clicked"""
        self.answer = str(self.task)[:-1]
        self.UserIn.set(self.answer)
    

calculator = Tk()

calculator.title("Gravador's Scientific Calculator")
app = Application(calculator)
# Make window fixed (cannot be resized)
calculator.resizable(width = False, height = False)

calculator.mainloop()
