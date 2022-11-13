
import tkinter

window = tkinter.Tk()
window.title("*** My first GUI program ***")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="Test label", font=("Arial", 25, "bold"))
my_label.pack(side="left")



window.mainloop()