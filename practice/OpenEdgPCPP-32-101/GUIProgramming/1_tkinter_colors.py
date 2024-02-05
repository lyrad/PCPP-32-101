import tkinter as tk

window = tk.Tk()
window.title("Window Colors")

# Basic color.
button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
button.pack()

# Color changes on mouse over.
# Colors may be defined using RGB, ex: #9370DB.
button_1 = tk.Button(
    window,
    text="Button #1",
    bg="MediumPurple",
    fg="LightSalmon",
    activeforeground="LavenderBlush",
    activebackground="HotPink"
)

button_1.pack()



window.mainloop()

