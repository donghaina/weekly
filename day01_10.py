def trapezoid_area(base_up, base_down, height):
    return 1 / 2 * (base_up + base_down) * height


# result = trapezoid_area(1, 2, 3)
# result = trapezoid_area(base_up=1, base_down=2, height=3)
# result = trapezoid_area(base_down=1, base_up=2, height=3)
# result = trapezoid_area(base_up=1,base_down=2,3) # wrong
# result = trapezoid_area(1, 2, height=3)

base_up = 1
base_down = 2
height = 3

result = trapezoid_area(base_up, base_down, height)
print(result)
