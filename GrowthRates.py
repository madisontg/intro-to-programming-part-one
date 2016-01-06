# Madison Thorburn-Gundlach
# Due September 13, 2015
# Graph y=x^2, y=e^x, y=x against each other, different colors, for 1 <= x <= 20

import pylab
import math

# variables (lists) for axis
x_values = []
quadratic = []
exponential = []
linear = []
number = 1

# collect numbers
while number <= 20:
    x_values.append(number)
    quadratic.append(number ** 2)
    exponential.append(math.e ** number)
    linear.append(number)
    number += 1

# label
pylab.xlabel("Data Size")
pylab.ylabel("Time")
pylab.title("Different Growth Rates of Functions")

# plot
pylab.plot(x_values,quadratic,"ro")
pylab.plot(x_values,exponential,"go")
pylab.plot(x_values,linear,"ko")
pylab.show()

# NOTE: exponential is large by x = 20 that the quadratic and linear
# equations aren't visible.  Comment out 2/3 to better see the results.
