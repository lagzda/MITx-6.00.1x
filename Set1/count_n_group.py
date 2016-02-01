"""
A catering company has hired you to help with organizing and preparing customer's orders. You are given a list of each customer's desired items, and must write a program that will count the number of each items needed for the chefs to prepare. The items that a customer can order are: salad, hamburger, and water.
Write a function called item_order that takes as input a string named order. The string contains only words for the items the customer can order separated by one space.
"""

def item_order(order):
    items = order.split(" ")
    #Initialise the counters
    salad = 0
    hamburger = 0
    water = 0
    
    for item in items:
        if item == "salad":
            salad += 1
        elif item == "hamburger":
            hamburger += 1
        elif item == "water":
            water += 1
    return "Salad : %i, Hamburger: %i, Water: %i" %(salad, hamburger, water)

#Tests
print item_order("salad water water hamburger")
    