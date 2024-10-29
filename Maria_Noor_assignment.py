import math 
def triangle_area(base, height):
    return 0.5 * base * height
# Square area
def square_area(side):
    return side ** 2
# Circle area
def circle_area(radius):
    return math.pi * (radius ** 2)
#rectangle area
def rectangle_area(length, width):
    return length * width
print("Triangle Area =", triangle_area(5, 6))
print("Square Area =", square_area(6))  
print("Circle Area =", circle_area(4))           
print("Rectangle Area =", rectangle_area(8, 6))