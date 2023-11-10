from tkinter import *
from tkinter import messagebox

import password_generator
import json


LOCK_IMAGE = "Days_21-30/Password_manager_JSON/logo.png"
FILE_LOCATION = "Days_21-30/Password_manager_JSON/"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = password_generator.generate()
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
    }
    
    if len(website_input) or len(password_input) > 0:
        
        try:
            with open(f"{FILE_LOCATION}data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(f"{FILE_LOCATION}data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)  
            with open(f"{FILE_LOCATION}data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:   
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
    else:
        messagebox.showerror(title="Password Manager", message="Either website or password cannot be empty.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50, bg="white")

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
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "demo@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1 )

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=2, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()