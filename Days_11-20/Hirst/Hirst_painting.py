
from turtle import color
import colorgram, os

course_base_directory = os.getcwd()
project_directory = "\Days_11-20\Hirst\\"
image_file = "hirst.jpg"

file = course_base_directory + project_directory + image_file

colors = colorgram.extract(file, 30)

colors_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors_list.append(new_color)
        
print(colors_list)

