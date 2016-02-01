"""
Write a function called ndigits, that takes an integer x (either positive or negative) as an argument. This function should return the number of digits in x.
"""
def ndigits(x):
    # If x is 0 the test output wanted 0 digits
    if x == 0:
        return 0
    # If x is smaller than than 10 it can't have more than one digit
    if abs(x) < 10:
        return 1
    x /= 10
    # Increment count after each succesful division if it gets that far
    return 1 + ndigits(x)

# Tests
print ndigits(0)
print ndigits(3)
print ndigits(28)
print ndigits(1023)