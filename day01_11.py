def trapezoid_area(base_up, base_down, height=15):
    return 1 / 2 * (base_up + base_down) * height


result = trapezoid_area(1, 2, 3)
print(result)
