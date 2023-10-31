from tkinter import *


LOCK_IMAGE = "Days_21-30/Password_manager/logo.png"









# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file=LOCK_IMAGE)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1 )

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=2, column=2 )
add_button = Button(text="Add")
add_button.grid(row=4, column=1)




window.mainloop()
