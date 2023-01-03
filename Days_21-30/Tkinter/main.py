
from tkinter import *

window = Tk()
window.title("*** My first GUI program ***")
window.minsize(width=500, height=400)

my_label = Label(text="Test label", font=("Arial", 25, "bold"))
my_label.pack(side="left")
my_label["text"] = "Kiisseli"


def button_clicked():
    data = input.get()
    my_label["text"] = data
    



button = Button(text="Click me", command=button_clicked)
button.pack()


input = Entry(width=50)
input.pack()




window.mainloop()