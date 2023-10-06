
from tkinter import *

window = Tk()
window.title("*** My first GUI program ***")
window.minsize(width=500, height=400)

my_label = Label(text="Test label", font=("Arial", 25, "bold"))
my_label["text"] = "Kiisseli"
#my_label.pack(side="left")
my_label.grid(column=6, row=0)

def button_clicked():
    data = input.get()
    my_label["text"] = data
    



button = Button(text="Click me", command=button_clicked)
button.grid(column=6, row=4)



input = Entry(width=50)
input.grid(column=6, row=3)





window.mainloop()