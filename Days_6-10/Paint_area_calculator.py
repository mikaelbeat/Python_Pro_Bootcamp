
import math

print("*** Paint area calculator ***\n")

height = 7
widht = 13
paint_can_coverage = 5


def calculate_paint(height, widht, coverage):
    result = (height * widht) / coverage
    rounded_result = math.ceil(result)
    
    print(
        f"Paint cans needed for wall {height} * {widht} is {rounded_result}.")
    

calculate_paint(height, widht, paint_can_coverage)
