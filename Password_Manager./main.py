from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    password_entry["text"] = password


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password_entered = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password_entered
        }
    }

    if len(website) == 0 or len(password_entered) == 0:
        messagebox.showinfo(title="Oops", message="Please Make sure to enter all the fields")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Detail Entered \n Email : {email} | Password : "
                                                              f"{password_entered}\n Is it OK?")
        if is_ok:
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
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


def find_password():
    try:
        website = website_entry.get()
        data = ""
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No file found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="password", message=f"Email : {email}\n Password : {password}")
        else:
            messagebox.showinfo(title="Error", message="No details on website {website}")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website : ")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/ username : ")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abc@gmail.com")

password_label = Label(text="Password : ")
password_label.grid(row=3, column=0)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=3)

add_password = Button(text="Add", command=save_password)
add_password.grid(row=4, column=1)

search = Button(text="Search", command=find_password)
search.grid(row=1, column=3)

window.mainloop()
