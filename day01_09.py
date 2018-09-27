import math


def get_triangle_the_third_slide_length(a, b):
    c = math.sqrt(a * a + b * b)
    return c

print("The right triangle third side's lenth is " + str(get_triangle_the_third_slide_length(3, 4)))
