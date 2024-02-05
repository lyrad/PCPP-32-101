import tkinter as tk
from tkinter import messagebox


# Access through widget["prop"].
def on_off(event=None):
    global button
    if button["text"] == "ON":
        button["text"] = "OFF"
    else:
        button["text"] = "ON"


# Access through Widget.cget("prop")
def on_off_3(event=None):
    global button
    messagebox.showinfo("Button Text", button.cget("text"))


# Access through Widget.config(prop=newval)
def on_off_2(event=None):
    global button
    button.config(text="Pouet")


def blink():
    global is_white
    if is_white:
        color = 'black'
    else:
        color = 'white'
    is_white = not is_white
    frame.config(bg=color)
    # Self call to relauch the action.
    # after_cancel(id) would cancel (when invoked before the 500ms...).
    frame.after(500, blink)


def button_destroy(event=None):
    global button
    button.destroy()



window = tk.Tk()
button = tk.Button(window, text="OFF")
button.pack()
button.bind('<Button-1>', on_off)
button.bind('<Button-3>', on_off_3)
button.bind('<Button-2>', on_off_2)

button_1 = tk.Button(window, text="Destroy ON/OFF button")
button_1.pack()
button_1.bind('<Button-1>', button_destroy)

is_white = True
frame = tk.Frame(window, width=200, height=100, bg='white')
frame.after(500, blink)
frame.pack()

# Focus: Get and set the focus on a widget.
# wi.focus_get()
# wi.focus_set()

window.mainloop()
