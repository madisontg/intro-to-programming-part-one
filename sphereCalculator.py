# Madison Thorburn-Gundlach, 8/30/15
# I have acted honorably.

import math

# calculate the area and circumference of a sphere from its radius

# Step 1: prompt for a radius of sphere
radius_str = input("Enter the radius of your sphere:\n# ")

#convert from string type to integer type
radius_int = int(radius_str)

# Step 2: apply the volume formula
volume = 4/3 * math.pi * radius_int **2

# Step 3: apply the surface area formula
surface_area = 4 * math.pi * radius_int **3

# Step 3: Print out the results
print ("The volume is:",volume,  \
      " and the surface area is:",surface_area, ". :-)")
