import random
import os
import time
import json

food_dict = {
    "Water": [0, 1],
    "Coke": [2, 1],
    "Sprite": [2, 1],
    "Orange Juice": [3, 1],
    "Hamburger": [7, 2],
    "Chicken Fingers": [8, 2],
    "Spaghetti": [10, 4],
    "Salad": [5, 2]
}

fn = 'input.txt'
ofn = 'output.txt'

old_time = os.path.getmtime(fn)
while True:
    if (os.path.getmtime(fn) > old_time):
        arr = []
        with open(fn, 'r') as f:
            line = f.readline()
            if line.strip() == "Request":
                line = f.readline().strip()
                while line != "Special instructions:":
                    arr += [line]
                    line = f.readline().strip()

        with open(ofn, 'w') as f:
            f.write('Pending \n')

        money = 0
        prep_time = 0

        for item in arr:
            money += food_dict[item][0]
            prep_time += food_dict[item][1]

        with open(ofn, 'w') as f:
            json.dump({"money": money, "time": prep_time}, f)

        old_time = os.path.getmtime(fn)