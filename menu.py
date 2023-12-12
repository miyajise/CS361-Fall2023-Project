# Name: Sharyn Miyaji
# Course: CS361 Section 400
# Assignment 12: Portfolio (Milestone #4)
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import json


def isPressed():
    # Ensures the table number is not blank nor an invalid number.
    if table_num.get() == '' or int(table_num.get()) <= 0:
        messagebox.showinfo(title='Invalid Table Number', message='You must enter a table number higher than 0.')
    else:
        # Writes each item selected to the input file.
        item_count = 0
        input_file = open('input.txt', 'w')
        input_file.write("Request \n")
        if drink1_button.get():
            input_file.write("Water \n")
            item_count += 1
        if drink2_button.get():
            input_file.write("Coke \n")
            item_count += 1
        if drink3_button.get():
            input_file.write("Sprite \n")
            item_count += 1
        if drink4_button.get():
            input_file.write("Orange Juice \n")
            item_count += 1
        if food1_button.get():
            input_file.write("Hamburger \n")
            item_count += 1
        if food2_button.get():
            input_file.write("Chicken Fingers \n")
            item_count += 1
        if food3_button.get():
            input_file.write("Spaghetti \n")
            item_count += 1
        if food4_button.get():
            input_file.write("Salad \n")
            item_count += 1
        input_file.write("Special instructions:\n" + instructions.get())
        input_file.close()

        if item_count == 0:
            # If no items are not selected, a message will pop up.
            messagebox.showinfo(title='Order Submission', message='No food/drink items have been selected.')
        else:
            # Program is delayed so James's microservice calculates the total cost
            # and time it will take to the complete the order.
            time.sleep(2)
            output_file = open('output.txt')
            output_data = json.load(output_file)
            cost = output_data['money']
            wait_time = output_data['time']
            output_file.close()
            text_message = "Your order has been received!\nTotal wait time: " + str(wait_time) + \
                           " minutes\nTotal amount: $" + str(cost) + "\nTable Number: " + str(table_num.get())
            messagebox.showinfo(title='Order Submission', message=text_message)

            # Resets/clears the GUI.
            drink1_button.set(False)
            drink2_button.set(False)
            drink3_button.set(False)
            drink4_button.set(False)
            food1_button.set(False)
            food2_button.set(False)
            food3_button.set(False)
            food4_button.set(False)
            instructions.set("")
            table_num.set("")


def isCleared():
    # Clears the GUI.
    drink1_button.set(False)
    drink2_button.set(False)
    drink3_button.set(False)
    drink4_button.set(False)
    food1_button.set(False)
    food2_button.set(False)
    food3_button.set(False)
    food4_button.set(False)
    instructions.set("")
    table_num.set("")


def isHelp():
    # Message box with instructions for users.
    messagebox.showinfo(title='Help', message="To create an order, you must select the food and/or drink of your "
                                              "choosing by using the checkbox next to each item. "
                                              "A table number is required, which can be found on the edge of the table "
                                              "you are currently sitting at.  Special instructions may be added by "
                                              "manually typing in the text box in the 'Special Instruction' section.  "
                                              "If you would like to start over, click the 'Clear' button.  If you are "
                                              "satisfied with your order, click 'Submit'.")


# Creates the GUI
table_order = Tk()
table_order.geometry('700x600')
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

drink1 = Checkbutton(label_frame, variable=drink1_button, onvalue=True, offvalue=False, text='Water - Free',
                     font=('Times New Roman', 16))
drink1.grid(column=1, row=3, columnspan=15, sticky=W)

drink2 = Checkbutton(label_frame, variable=drink2_button, onvalue=True, offvalue=False, text='Coke - $2',
                     font=('Times New Roman', 16))
drink2.grid(column=1, row=4, columnspan=15, sticky=W)

drink3 = Checkbutton(label_frame, variable=drink3_button, onvalue=True, offvalue=False, text='Sprite - $2',
                     font=('Times New Roman', 16))
drink3.grid(column=1, row=5, columnspan=15, sticky=W)

drink4 = Checkbutton(label_frame, variable=drink4_button, onvalue=True, offvalue=False, text='Orange Juice - $3',
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

food1 = Checkbutton(label_frame, variable=food1_button, onvalue=True, offvalue=False, text='Hamburger - $7',
                    font=('Times New Roman', 16))
food1.grid(column=1, row=9, columnspan=15, sticky=W)

food2 = Checkbutton(label_frame, variable=food2_button, onvalue=True, offvalue=False, text='Chicken Fingers - $8',
                    font=('Times New Roman', 16))
food2.grid(column=1, row=10, columnspan=15, sticky=W)

food3 = Checkbutton(label_frame, variable=food3_button, onvalue=True, offvalue=False, text='Spaghetti - $10',
                    font=('Times New Roman', 16))
food3.grid(column=1, row=11, columnspan=15, sticky=W)

food4 = Checkbutton(label_frame, variable=food4_button, onvalue=True, offvalue=False, text='Salad - $5',
                    font=('Times New Roman', 16))
food4.grid(column=1, row=12, columnspan=15, sticky=W)
space_label2 = Label(label_frame, text='').grid(column=0, row=13, columnspan=10, sticky=W)

space_label3 = Label(label_frame, text='').grid(column=0, row=24, columnspan=10, sticky=W)

instructions = StringVar()
spec_instr_title = Label(table_order, text='Add Special Instructions (Optional)', font=('Times New Roman', 20, 'underline')).grid(column=0, row=15, columnspan=20, sticky=W)
spec_instr_textbox = Entry(table_order, textvariable=instructions, width=20, bd=2).grid(column=0, row=16, columnspan=20, rowspan=5, sticky=W)

table_num = StringVar()
table_num_title = Label(table_order, text='Enter Your Table Number (Required)', font=('Times New Roman', 20, 'underline')).grid(column=0, row=25, columnspan=20, sticky=W)
table_num_textbox = Entry(table_order, textvariable=table_num, width=20, bd=2).grid(column=0, row=26, columnspan=20, rowspan=5, sticky=W)

help_button = Button(label_frame, text="Help", width=10, height=2, command=isHelp).grid(column=0, row=35, columnspan=3)

submit = Button(label_frame, text="Submit", width=10, height=2, command=isPressed).grid(column=13, row=35, columnspan=3)

cancel = Button(label_frame, text="Clear", width=10, height=2, command=isCleared).grid(column=17, row=35, columnspan=3)

# print(table_order)
table_order.mainloop()
