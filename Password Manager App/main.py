from tkinter import *
from tkinter import messagebox
import pass_generator as p
import pyperclip

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
    line = f"{website} | {username} | {password}\n"

    # Checks if website or password is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops an error!", message="Please don't leave any of the fields empty!")
    else:
        # Stores boolean value to is_ok variable (true or false)
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: "
                                   f"{username}\nPassword: {password}\nDo you want to save?")
        if is_ok:
            with open ("./data.txt", mode="a") as f:
                f.write(line)
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

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
website_input.grid(row=1, column=1, columnspan=2, sticky=EW, pady=(0,5))
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

generate_pass_button = Button(text="Generate Password", command=generate_pass)
generate_pass_button.grid(row=3, column=2, sticky=EW, pady=(0,5))

add_button = Button(width=30, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)




window.mainloop()