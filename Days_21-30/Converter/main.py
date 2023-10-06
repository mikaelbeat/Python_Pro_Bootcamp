
from tkinter import *

window = Tk()
window.title("*** Mile to Km Converter ***")
window.minsize(width=350, height=150)

mile_in_km = 1.609344

def calculate():
    miles = int(input.get())
    miles_as_km = round(miles * mile_in_km)
    result_label["text"] = miles_as_km


# First row    
input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)

# Second row

equal_label = Label(text="is equal to", font=("Arial", 15))
equal_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Arial", 15))
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 15))
km_label.grid(column=2, row=1)

# Third row

button = Button(text="Calculate", font=("Arial", 15), command=calculate)
button.grid(column=1, row=2)


window.mainloop()