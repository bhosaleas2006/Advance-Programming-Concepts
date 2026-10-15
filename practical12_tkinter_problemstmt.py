
import tkinter as tk

root = tk.Tk()
root.title("Student Registration")
root.geometry("400x400")

title = tk.Label(root, text="Student Registration",
                 font=("Arial", 16, "bold"))
title.pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Roll No:").grid(row=0, column=0, sticky="w", pady=8)
roll_entry = tk.Entry(frame)
roll_entry.grid(row=0, column=1, pady=8)

tk.Label(frame, text="Name:").grid(row=1, column=0, sticky="w", pady=8)
name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=1, pady=8)

tk.Label(frame, text="Subject:").grid(row=2, column=0, sticky="nw", pady=8)

subjects = ["Python", "Java", "C++", "HTML"]
variables = []

subject_frame = tk.Frame(frame)
subject_frame.grid(row=2, column=1, sticky="w")

for subject in subjects:
    var = tk.IntVar()
    tk.Checkbutton(subject_frame, text=subject,
                   variable=var).pack(anchor="w")
    variables.append(var)


tk.Button(root, text="Submit",
          width=12).pack(pady=20)


root.mainloop()

