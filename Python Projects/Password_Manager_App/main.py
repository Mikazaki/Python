from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for _ in range(randint(8, 10))]

    symbol = [choice(symbols) for _ in range(randint(2, 4))]

    number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter + number + symbol

    shuffle(password_list)

    PASSWORD = "".join(password_list)
    password_input.insert(0, PASSWORD)
    pyperclip.copy(PASSWORD)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    info = {
        website_input.get(): {
            "email/username": email_input.get(),
            "password": password_input.get(),
        }
    }

    if len(website_input.get()) == 0 or len(email_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Error", message="Please don't leave empty fields!")

    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(info, file, indent=4)

        else:
            data.update(info)

            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    websitei = website_input.get()
    emaili = email_input.get()

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Data File Not Found", message='No Such Data File Found')

    else:

        if websitei in data and emaili == data[websitei]['email/username']:
            messagebox.showinfo(title=websitei,
                                message=f"Email: {data[websitei]['email/username']}\nPassword: {data[websitei]['password']}")

        else:
            messagebox.showerror(title="Data Not Found", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_input = Entry(width=27)
website_input.grid(column=1, row=1, sticky="w")
website_input.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="ew")
email_input.insert(END, ".com")

password = Label(text="Password:")
password.grid(column=0, row=3)

password_input = Entry(width=27)
password_input.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", padx=0, pady=0, command=gen_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=10)

copy = Label(text="© Copyright Mikazaki™", font=("Courier", 10, "bold"))
copy.grid(column=1, row=5, columnspan=2, sticky="ew")

search_button = Button(text="Search", padx=0, pady=0, command=find_password)
search_button.grid(column=2, row=1, sticky="ew")

window.mainloop()
