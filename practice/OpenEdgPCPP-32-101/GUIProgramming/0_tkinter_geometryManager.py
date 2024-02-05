import tkinter
from tkinter import messagebox


# Handler/Callback.
# Should be invoked ONLY BY the controller.
def click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        window_place.destroy()


## Place.
window_place = tkinter.Tk()
window_place.title("Window Place")

# Button widget.
button = tkinter.Button(window_place, text="Place Bye", command=click)
button_1 = tkinter.Button(window_place, text="Place 1")

# Placement in handled by a geometry manager.
# For place, upper left corner as a reference for x/y, height/width are optional.
button.place(x=10, y=10)
button_1.place(x=10, y=50, width=150, height=50)

# Starts the controller.
window_place.mainloop()

## Grid.
window_grid = tkinter.Tk()
window_grid.title("Window Grid")
button_2 = tkinter.Button(window_grid, text="Grid 2")
button_3 = tkinter.Button(window_grid, text="Grid 3")
button_4 = tkinter.Button(window_grid, text="Grid 4")

# For grid, automated dividing into columns and rows (total number depending on the number of items?).
button_2.grid(row=0, column=0)
button_3.grid(row=1, column=1)
button_4.grid(row=2, column=0, columnspan=2)

# Starts the controller.
window_grid.mainloop()

## Pack.
# side=s: Forces the manager to pack the widgets in a specified direction, TOP|BOTTOM|LEFT|RIGHT
# fill=f: Suggests to the manager how to expand the widget if you want it to occupy more space than the default
window_pack = tkinter.Tk()
window_pack.title("Window Pack")
button_pack_1 = tkinter.Button(window_pack, text="Pack 1")
button_pack_2 = tkinter.Button(window_pack, text="Pack 2")
button_pack_3 = tkinter.Button(window_pack, text="Pack 3")
button_pack_1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
button_pack_2.pack()
button_pack_3.pack()
window_pack.mainloop()