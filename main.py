from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_data = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    is_ok = messagebox.askokcancel(title=website_data,message=f"These are the details entered: \n Username: {username} \n Password: {password}")
    if is_ok:
        with open("data.txt",mode="a") as file:

            file.write(f"{website_data} | {username} | {password}\n")

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
    width=15
)
generate_btn.grid(row=3, column=2, padx=(5,0),sticky="W")

add_btn = Button(
    text="Add",
    width=36,
    command=save_data
)
add_btn.grid(row=4, column=1, columnspan=2, pady=10,sticky="W")

window.mainloop()
window.mainloop()