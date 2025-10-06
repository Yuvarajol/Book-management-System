from tkinter import *
from tkinter import ttk, messagebox
import selector
import sales

# Root window setup
root = Tk()
root.title("📚 Book Manager")
root.geometry("500x300")
root.configure(bg="#f0f4f7")

# Menu bar
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)

def select():
    selector.v()

def sale():
    sales.v()

filemenu.add_command(label='View', command=select)
filemenu.add_command(label='Open', command=sale)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=lambda: messagebox.showinfo("About", "Book Manager v1.0\nCreated by Yuva"))

# Frame for form
form_frame = Frame(root, bg="#f0f4f7")
form_frame.pack(pady=20)

# Labels and Entries
Label(form_frame, text='Name of the Book:', font=('Segoe UI', 10), bg="#f0f4f7").grid(row=0, column=0, padx=10, pady=5, sticky=E)
e1 = ttk.Entry(form_frame, width=30)
e1.grid(row=0, column=1, padx=10, pady=5)

Label(form_frame, text='Price:', font=('Segoe UI', 10), bg="#f0f4f7").grid(row=1, column=0, padx=10, pady=5, sticky=E)
e2 = ttk.Entry(form_frame, width=15)
e2.grid(row=1, column=1, padx=10, pady=5, sticky=W)

# Save button
def save():
    g1 = e1.get().strip()
    g2 = e2.get().strip()
    if not g1 or not g2:
        messagebox.showwarning("Input Error", "Please fill in both fields.")
        return
    try:
        with open("data/data.csv", "a") as file:
            file.write(f"{g1}:{g2}\n")
        messagebox.showinfo("Success", "Book details saved successfully!")
        e1.delete(0, END)
        e2.delete(0, END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data:\n{e}")

ttk.Button(root, text="💾 Save", command=save).pack(pady=20)

root.mainloop()