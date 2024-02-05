import tkinter as tk
from tkinter import messagebox

## Some events:
# <Button-1|2|3>: Single left|middle|right click.
# <DoubleButton-1>: Double left click (will also trigger Button-1.
# <Enter>: Mouse cursor appears over the widget.
# <Focus-In>: The widget gains the focus.
# <Key>: The user presses any key (also one dedicated event for every key).

## The Event class parameters:
# widget: The widget object.
# type: The event type (integer).
# num: Number of mouse click (mouse events).
# keysym/keycode: Key symbol/numerical code pressed (keyboard events).
# char: Character code pressed (keyboard events).
# x/y, x_root/y_root: Mouse pointer coordinates when event triggered (relative to widget or screen).


def clickEvent(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clickEvent None!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)

def click(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")

# Bind event to the widget. (when no parameter callback for the event/widget).
label.bind("<Button-1>", click)
label.pack()

# No binding: command parameter. !!! Event will be None !!!
button = tk.Button(window, text="Button", command=clickEvent)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# Bind event to the widget.
frame.bind("<Button-1>", clickEvent)
frame.pack()

button_1 = tk.Button(window, text="Unbound, from bind/unbind")
# Bind event to the widget.
button_1.bind("<Button-1>", clickEvent)
button_1.pack()
button_1.unbind("<Button-1>")

button_2 = tk.Button(window, text="Unbound", command=clickEvent)
# Bind event to the widget.
button_2.pack()
button_2.config(command=lambda: None)
button_2.config(text="Unbound, from command parameter config overwrite")

# Bind/Unbind an event to all widget in the window.
window.bind_all("<Button-3>", click)
# window.unbind_all("<Button-3>")

window.mainloop()
