'''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
'''
# Curve function for calculating radiation
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    # When the end time is reached return 0 so add nothing
    if (start >= stop):
        return 0
    # Calculate the area of the square (radiation * little_time_slot)
    rad = f(start) * step
    # Sum up the whole radiation
    return rad + radiationExposure(start+step, stop, step)

# Tests
print radiationExposure(0, 5, 1)
print radiationExposure(5, 11, 1)
print radiationExposure(0, 11, 1)
print radiationExposure(40, 100, 1.5)
