# Write a class that represents a rectangle shape and has a method for each of the following:
#   Calculate the area
#   Calculate the perimeter
#   Calculate the length of the diagonal
#   Determine whether or not the rectangle is square
import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        return self.width * self.height

    def perimeter_calc(self):
        return (self.width + self.height) * 2

    def diagonal_calc(self):
        return f"{math.sqrt(self.width ** 2 + self.height ** 2):.1f}"

    def square_check(self):
        if self.width == self.height:
            return "Shape is a square"
        else:
            return "Shape is a rectangle"

trial_rec1 = Rectangle(3, 4)

print(trial_rec1.area_calc())
print(trial_rec1.perimeter_calc())
print(trial_rec1.diagonal_calc())
print(trial_rec1.square_check())

trial_rec1 = Rectangle(280, 280)

print(trial_rec1.area_calc())
print(trial_rec1.perimeter_calc())
print(trial_rec1.diagonal_calc())
print(trial_rec1.square_check())