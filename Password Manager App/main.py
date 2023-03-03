from tkinter import *
from tkinter import messagebox
import pass_generator as p
import pyperclip
import json

BLACK = "#20262E"
WHITE = "#FEFCF3"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_input.delete(0, END)
    new_pass = p.create_pass()
    password_input.insert(END, new_pass)
    pyperclip.copy(new_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves website, username and password to a file"""
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    } 

    # Checks if website or password is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any of the fields empty!")
    else:
        try:
            with open("./data.json", mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("./data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("./data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

# ---------------------------- SEARCH USERNAME ------------------------------- #

def search_password():
    """Searches username and password from the data file if it exists."""
    website = website_input.get()

    try:
        with open("./data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There is no website called {website}.\n"
                                "Check if you forgot a capital letter")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=BLACK)

logo_image = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BLACK)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_input = Entry()
website_input.focus()
website_input.grid(row=1, column=1, sticky=EW, pady=(0,5), padx=(0,5))
website_label = Label(text="Website:", bg=BLACK, fg=WHITE)
website_label.grid(row=1, column=0, pady=(0,5))

username_input = Entry()
username_input.grid(row=2, column=1, columnspan=2, sticky=EW, pady=(0,5))
username_input.insert(END, "jere.viitasalo@gmail.com")
username_label = Label(text="Username/Email:", bg=BLACK, fg=WHITE)
username_label.grid(row=2, column=0, pady=(0,5))

password_input = Entry()
password_input.grid(row=3, column=1, sticky=EW, pady=(0,5), padx=(0,5))
password_label = Label(text="Password:", bg=BLACK, fg=WHITE)
password_label.grid(row=3, column=0, pady=(0,5))

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2, sticky=EW, pady=(0,5))

generate_pass_button = Button(text="Generate Password", command=generate_pass)
generate_pass_button.grid(row=3, column=2, sticky=EW, pady=(0,5))

add_button = Button(width=30, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()