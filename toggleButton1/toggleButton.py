"""A simple program to create a GUI to communicate with an Arduino and toggle an LED on and off.
Created to demonstrate how to use Python with tkinter to create a GUI.
- Colin Diehl
"""
from tkinter import * #import the modules for the GUI
import serial #and the serial communications

PORT = "COM5"
ser = serial.Serial(PORT, 9600) #start the serial com w/ 9600 baudrate

class Application(Frame): #create the class for the GUI to run
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid() # create the grid on the GUI for the part to snap onto
        self.create_widgets() #the function to create the GUI parts

    def create_widgets(self): #define all GUI parts
        self.label = Label(self) #create a label
        self.label["text"] = "Use the button to toggle the LED on and off:" #set the text of the label
        self.label.grid( row = 0, column = 0)#snap the label to the top left of the grid

        self.button = Button(self) #create a button
        self.button["text"] = "LED: OFF" #set the original text of the button
        self.button["height"] = 2 #set the height of the button to 2 characters tall
        self.button["width"] = 12 #set the button width to 12 characters wide
        self.button["command"] = self.toggle #the function the button will run when pressed
        self.button.grid(row = 1, column = 0) #snap the button to the second row of the grid
        self.button["bg"] = "green"

        self.text = Text(self) #create a text box
        self.text["height"] = 2 #set the text box height to 2 characters
        self.text["width"] = 20 #set the text box width to 20 characters
        self.text.grid(row = 2, column = 0) #snap the text box to the third row of the grid

        self.end = Button(self) #create another button to end the program
        self.end["text"] = "END" #set the text on the button
        self.end["height"] = 2 #set the button height to 2 characters
        self.end["width"] = 12 #set the button width to 12 characters
        self.end["bg"] = "yellow" #set the background color of the button to red
        self.end["command"] = self.quit #the quit function the button will run
        self.end.grid(row = 2, column = 1, sticky = E) #snap the button to the right side of the third row, second column(

    def toggle(self): #define the function from the first button
        index_dict={"OFF": "ON" , "ON": "OFF"} #define a sequence that switches from off to on to off
        index[0] = index_dict[index[0]] #progresses through the sequence, toggling the inital string in the sequence
        self.button["text"] = "LED: " + str(index[0]) #updates the button text with the current state of the LED
        if index[0] == "OFF": #when the inital string is off
            ser.write(bytes("a", encoding="ascii")) #writes lowercase a into the serial com, Arduino reads and sets output low
            self.text.delete(0.0, END) #deletes the contents of the text box
            self.text.insert(0.0, "The LED is OFF") #inserts the string into the text box to display OFF state of the LED
            self.button["bg"]="green"
        if index[0] == "ON": #when the inital string is on
            ser.write(bytes("A", encoding="ascii")) #writes uppercase A into the serial com, Arduino reads and sets output high
            self.text.delete(0.0, END) #clears the text box
            self.text.insert(0.0, "The LED is ON") #inserts the string into the text box to display ON state of the LED
            self.button["bg"] = "red"

    def quit(self): #define the function to kill the program
        ser.write(bytes("a", encoding="ascii")) #write lowercase a into serial com, to make sure LED goes off when program ends
        ser.close() #close the serial communication
        root.destroy() #destroy the GUI
index = ["OFF"] #set the intial string in the sequence to off, LED starts off
root = Tk() #these three lines start and run the GUI window in a loop
root.title("Interface Demo")
app = Application(root)
root.mainloop()