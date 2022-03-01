from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols

    shuffle(password_list)

    new_password = "".join(password_list)
    pass_input.insert(0, new_password)
    pyperclip.copy(new_password)

# ------------------------------- SAVE PASSWORD --------------------------------- #
def add_button():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
            web_input.focus()

# ------------------------------- SEARCH WEBSITE -------------------------------- #
def search_button():
    website = web_input.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

# ---------------------------------- UI SETUP ----------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

web_label = Label(text="Website:")
web_label.grid(column=1, row=2)
email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)
pass_label = Label(text="Password:")
pass_label.grid(column=1, row=4)

web_input = Entry(width=26)
web_input.grid(column=2, row=2)
web_input.focus()
email_input = Entry(width=44)
email_input.grid(column=2, row=3, columnspan=2)
email_input.insert(0, "ty@gmail.com")
pass_input = Entry(width=26)
pass_input.grid(column=2, row=4)

search_butt = Button(text="Search", width=14, command=search_button)
search_butt.grid(column=3, row=2)
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=3, row=4)
add_butt = Button(text="Add", width=36, command=add_button)
add_butt.grid(column=2, row=5, columnspan=2)




window.mainloop()
