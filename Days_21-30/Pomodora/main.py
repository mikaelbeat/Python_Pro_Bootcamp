
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
TOMATO_IMAGE = "Days_21-30/Pomodora/tomato.png"
CHECK_MARK = "✓"

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=TOMATO_IMAGE)
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

title_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=("Arial", 25, "bold"))
title_label.grid(column=1, row=0)


canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", font=("Arial", 20, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Arial", 20, "bold"))
reset_button.grid(column=2, row=2)

check_mark_label = Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN, font=("Arial", 25, "bold"))
check_mark_label.grid(column=1, row=3)



window.mainloop()

#TEST