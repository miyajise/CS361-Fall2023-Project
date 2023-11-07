# Name: Sharyn Miyaji
# Course: CS361 Section 400
# Milestone 1
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def isPressed():
    input_file = open('input.txt', 'w')
    input_file.write("Request \n")
    if drink1_button.get():
        input_file.write("Water \n")
    if drink2_button.get():
        input_file.write("Coke \n")
    if drink3_button.get():
        input_file.write("Sprite \n")
    if drink4_button.get():
        input_file.write("Orange Juice \n")
    if food1_button.get():
        input_file.write("Hamburger \n")
    if food2_button.get():
        input_file.write("Chicken Fingers \n")
    if food3_button.get():
        input_file.write("Spaghetti \n")
    if food4_button.get():
        input_file.write("Salad \n")
    input_file.write("Special instructions: " + instructions.get())
    input_file.close()
    messagebox.showinfo(title='Order Submission', message="Your order has been received!")

    drink1_button.set(False)
    drink2_button.set(False)
    drink3_button.set(False)
    drink4_button.set(False)
    food1_button.set(False)
    food2_button.set(False)
    food3_button.set(False)
    food4_button.set(False)
    instructions.set("")

def isCancelled():
    table_order.destroy()



# Creates the GUI
table_order = Tk()
table_order.geometry('600x500')
table_order.title('Food and Drink Menu')

label_frame = Label(table_order, text='Please select the food/drink you would like to order.',
                    font=('Times New Roman', 24, 'bold')).grid(column=0, row=0, columnspan=20)

# Drink Menu

drink_title = Label(table_order, text='DRINKS', font=('Times New Roman', 20, 'underline')).grid(column=0, row=2,
                                                                                                columnspan=10, sticky=W)

drink1_button = BooleanVar()
drink2_button = BooleanVar()
drink3_button = BooleanVar()
drink4_button = BooleanVar()

drink1 = Checkbutton(label_frame, variable=drink1_button, onvalue=True, offvalue=False, text='Water',
                     font=('Times New Roman', 16))
drink1.grid(column=1, row=3, columnspan=15, sticky=W)

drink2 = Checkbutton(label_frame, variable=drink2_button, onvalue=True, offvalue=False, text='Coke',
                     font=('Times New Roman', 16))
drink2.grid(column=1, row=4, columnspan=15, sticky=W)

drink3 = Checkbutton(label_frame, variable=drink3_button, onvalue=True, offvalue=False, text='Sprite',
                     font=('Times New Roman', 16))
drink3.grid(column=1, row=5, columnspan=15, sticky=W)

drink4 = Checkbutton(label_frame, variable=drink4_button, onvalue=True, offvalue=False, text='Orange Juice',
                     font=('Times New Roman', 16))
drink4.grid(column=1, row=6, columnspan=15, sticky=W)

space_label1 = Label(label_frame, text='').grid(column=0, row=7, columnspan=10, sticky=W)

# Food Menu

food_title = Label(table_order, text='FOOD', font=('Times New Roman', 20, 'underline')).grid(column=0, row=8,
                                                                                             columnspan=5, sticky=W)
food1_button = BooleanVar()
food2_button = BooleanVar()
food3_button = BooleanVar()
food4_button = BooleanVar()

food1 = Checkbutton(label_frame, variable=food1_button, onvalue=True, offvalue=False, text='Hamburger',
                    font=('Times New Roman', 16))
food1.grid(column=1, row=9, columnspan=15, sticky=W)

food2 = Checkbutton(label_frame, variable=food2_button, onvalue=True, offvalue=False, text='Chicken Fingers',
                    font=('Times New Roman', 16))
food2.grid(column=1, row=10, columnspan=15, sticky=W)

food3 = Checkbutton(label_frame, variable=food3_button, onvalue=True, offvalue=False, text='Spaghetti',
                    font=('Times New Roman', 16))
food3.grid(column=1, row=11, columnspan=15, sticky=W)

food4 = Checkbutton(label_frame, variable=food4_button, onvalue=True, offvalue=False, text='Salad',
                    font=('Times New Roman', 16))
food4.grid(column=1, row=12, columnspan=15, sticky=W)
space_label2 = Label(label_frame, text='').grid(column=0, row=13, columnspan=10, sticky=W)

space_label3 = Label(label_frame, text='').grid(column=0, row=24, columnspan=10, sticky=W)

instructions = StringVar()
spec_instr_title = Label(table_order, text='Add Special Instructions', font=('Times New Roman', 20, 'underline')).grid(column=0, row=15, columnspan=20, sticky=W)
spec_instr_textbox = Entry(table_order, textvariable=instructions, width=20, bd=2).grid(column=0, row=16, columnspan=20, rowspan=5, sticky=W)


submit = Button(label_frame, text="Submit", width=10, height=2, command=isPressed).grid(column=13, row=25, columnspan=3)

cancel = Button(label_frame, text="Cancel", width=10, height=2, command=isCancelled).grid(column=17, row=25,
                                                                                          columnspan=3)

# print(table_order)
table_order.mainloop()
