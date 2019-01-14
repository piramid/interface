import serial
from tkinter import *
window = Tk()
window.title("โปรแกรมปิดเปิดอุปกรณ์ไฟฟ้า")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid()
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
ser = serial.Serial('COM5', 9600)

def clicked():
    lbl.configure(text="Button was clicked !!")

def ontiolet():
    ser.write(b'A')
    message = ser.readline()
    print(message)

def offtiolet():
    ser.write(b'B')
    message = ser.readline()
    print(message)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

btn1 = Button(window, text="เปิดไฟห้องน้ำ", command=ontiolet)
btn1.grid()

btn1 = Button(window, text="ปิดไฟห้องน้ำ ", command=offtiolet)
btn1.grid()

window.mainloop()
