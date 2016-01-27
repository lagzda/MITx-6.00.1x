"""
Complete programming experience - Polysum

A regular polygon has n number of sides. Each side has length s.


Write a function called polysum that takes 2 arguments n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""

# Import the math module to access the constants and functions like pi and tan
import math
def polysum(n, s):
    #Calculate the area and perimeters by applying the formulas
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    perimeter = n * s
    #Return the output rounding it to 4 decimal places
    return round(area + perimeter ** 2, 4)

#Test the return value
print polysum(4,4)