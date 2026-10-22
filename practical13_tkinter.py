
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter GUI Collection")
root.geometry("350x400")

tk.Label(root, text="Tkinter GUI Programs",
         font=("Arial", 16, "bold")).pack(pady=20)


# 1. Registration Form - Entry and OptionMenu
def registration():
    win = tk.Toplevel(root)
    win.title("Registration Form")
    win.geometry("300x300")

    tk.Label(win, text="Registration Form",
             font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(win, text="Name").pack()
    name = tk.Entry(win)
    name.pack()

    tk.Label(win, text="Course").pack()
    course = tk.StringVar(value="Python")
    tk.OptionMenu(win, course, "Python", "Java", "C++").pack()

    def submit():
        messagebox.showinfo(
            "Details", f"Name: {name.get()}\nCourse: {course.get()}"
        )

    tk.Button(win, text="Submit", command=submit).pack(pady=15)


# 2. Hobby Selection - Checkbutton
def hobbies():
    win = tk.Toplevel(root)
    win.title("Hobby Selection")
    win.geometry("250x300")

    tk.Label(win, text="Select Your Hobbies",
             font=("Arial", 14, "bold")).pack(pady=10)

    reading = tk.IntVar()
    music = tk.IntVar()
    sports = tk.IntVar()

    tk.Checkbutton(win, text="Reading",
                   variable=reading).pack()
    tk.Checkbutton(win, text="Music",
                   variable=music).pack()
    tk.Checkbutton(win, text="Sports",
                   variable=sports).pack()

    def show():
        selected = []
        if reading.get():
            selected.append("Reading")
        if music.get():
            selected.append("Music")
        if sports.get():
            selected.append("Sports")

        messagebox.showinfo("Hobbies", ", ".join(selected) or "None selected")

    tk.Button(win, text="Submit", command=show).pack(pady=15)


# 3. Feedback Form - Radiobutton and Scale
def feedback():
    win = tk.Toplevel(root)
    win.title("Feedback Form")
    win.geometry("300x300")

    tk.Label(win, text="Feedback Form",
             font=("Arial", 14, "bold")).pack(pady=10)

    rating = tk.StringVar(value="Good")

    tk.Label(win, text="Rate our service").pack()

    for item in ["Excellent", "Good", "Poor"]:
        tk.Radiobutton(win, text=item, variable=rating,
                       value=item).pack()

    tk.Label(win, text="Satisfaction (0-10)").pack(pady=5)
    score = tk.Scale(win, from_=0, to=10, orient="horizontal")
    score.pack()

    def submit():
        messagebox.showinfo(
            "Feedback",
            f"Rating: {rating.get()}\nScore: {score.get()}"
        )

    tk.Button(win, text="Submit", command=submit).pack(pady=10)


# 4. Shopping List - Listbox
def shopping():
    win = tk.Toplevel(root)
    win.title("Shopping List")
    win.geometry("300x350")

    tk.Label(win, text="Shopping List",
             font=("Arial", 14, "bold")).pack(pady=10)

    item = tk.Entry(win)
    item.pack(pady=5)

    items = tk.Listbox(win, width=30)
    items.pack(pady=10)

    def add():
        if item.get().strip():
            items.insert(tk.END, item.get())
            item.delete(0, tk.END)

    def delete():
        selected = items.curselection()
        if selected:
            items.delete(selected[0])

    tk.Button(win, text="Add Item", command=add).pack(pady=3)
    tk.Button(win, text="Delete Item", command=delete).pack(pady=3)


# 5. Message Editor - Text and Spinbox
def message_editor():
    win = tk.Toplevel(root)
    win.title("Message Editor")
    win.geometry("300x300")

    tk.Label(win, text="Message Editor",
             font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(win, text="Enter your message").pack()
    message = tk.Text(win, width=30, height=5)
    message.pack(pady=5)

    tk.Label(win, text="Number of copies").pack()
    copies = tk.Spinbox(win, from_=1, to=10)
    copies.pack()

    def show():
        text = message.get("1.0", "end-1c")
        messagebox.showinfo(
            "Your Message",
            f"Message: {text}\nCopies: {copies.get()}"
        )

    tk.Button(win, text="Display", command=show).pack(pady=10)


# Main Menu
tk.Button(root, text="1. Registration Form",
          width=25, command=registration).pack(pady=5)

tk.Button(root, text="2. Hobby Selection",
          width=25, command=hobbies).pack(pady=5)

tk.Button(root, text="3. Feedback Form",
          width=25, command=feedback).pack(pady=5)

tk.Button(root, text="4. Shopping List",
          width=25, command=shopping).pack(pady=5)

tk.Button(root, text="5. Message Editor",
          width=25, command=message_editor).pack(pady=5)

tk.Button(root, text="Exit",
          width=15, command=root.destroy).pack(pady=15)

root.mainloop()
