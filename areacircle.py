import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Prompt the user for input
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
circle_area = calculate_circle_area(radius)

# Print the result
print("The area of the circle is:", circle_area)