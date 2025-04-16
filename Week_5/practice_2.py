import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTK

def welcomeMessage(username):
    # Create a Tkinter window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("800x600")
    
    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is python GUI with Tkinter")
    label_2.pack()
    
    # Run the Tkinter event loop
    root.mainloop()
    
def submit():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Login", "Invalid username or password")
# create main window 
root = tk.Tk()
root.title("Login Form")
root.geometry("800x600")


# Create username label and entry
username_label = tk.Label(root,teXt="username;")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create password label and entry
Password_label = tk.Label(root, text="password:")
Password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create submit button
submit_button = tk.Button(root,text="submit", command=submit)
submit_button.pack()

# Run the main event loop
root.mainloop()