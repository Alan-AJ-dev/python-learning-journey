from tkinter import *
import random
from tkinter import messagebox
from xml.etree.ElementTree import indent

import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from asyncio.windows_events import NULL
from random import shuffle
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = 3
    nr_symbols = 4
    nr_numbers = 5

    ran_password = ""
    for let in range(nr_letters):
        ran_password +=str(random.choice(letters))

    for sym in range(nr_symbols):
        ran_password +=str(random.choice(symbols))
    for num in range(nr_numbers):
        ran_password +=str(random.choice(numbers))
    print(ran_password)
    ran_password = list(ran_password)
    shuf_pass =""
    for i in range(len(ran_password)//2):
        shuf_pass += str(ran_password[-i])
    for i in range(len(ran_password)//2,len(ran_password)):
        shuf_pass += str(ran_password[i])
    password_entry.insert(0,shuf_pass)
    pyperclip.copy(shuf_pass)

def search():
    website = website_entry.get()
    with open("data.json","r") as file:
        data = json.load(file)
        try:
            username = data[website]['email']
            password = data[website]['password']
            messagebox.askokcancel(title=website,message=f"These are the stored Credentials: \n Username: {username} \n Password: {password}")

            pyperclip.copy(password)
        except :
            messagebox.askokcancel(title="Error",
                                   message="File not Found")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_data = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_data:{
           "email" : username,
            "password" : password
        }
    }
    if len(website_data) == 0  or len(username)== 0 or  len(password)== 0:

        canvas.create_text(110,190,text="Oops! Something went wrong!",fill="red")
    else:
        is_ok = messagebox.askokcancel(title=website_data,message=f"These are the details entered: \n Username: {username} \n Password: {password}")
        if is_ok:
            try:

                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            except :
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                print("success")







            password_entry.delete(0,END)
            website_entry.delete(0, END)
            website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---------------- Canvas ---------------- #

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

# ---------------- Labels ---------------- #

Label(text="Website:").grid(row=1, column=0, sticky="E", pady=5)

Label(text="Email/Username:").grid(row=2, column=0, sticky="E", pady=5)

Label(text="Password:").grid(row=3, column=0, sticky="E", pady=5)

# ---------------- Entries ---------------- #

website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
email_entry.insert(0, "alanjoseph52006@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="W")

# ---------------- Buttons ---------------- #

generate_btn = Button(
    text="Generate Password",
    width=15,
    command=generate_password
)
generate_btn.grid(row=3, column=2, padx=(5,0),sticky="W")

add_btn = Button(
    text="Add",
    width=36,
    command=save_data
)
add_btn.grid(row=4, column=1, columnspan=2, pady=10,sticky="W")

search_btn = Button(
    text="Search",
    width=13,
    command=search
)
search_btn.grid(row=1, column=2,  pady=20)

window.mainloop()