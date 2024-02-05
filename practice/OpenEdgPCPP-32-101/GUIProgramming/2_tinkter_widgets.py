import tkinter as tk
from tkinter import messagebox


def clicked():
    # showinfo: alert in javascript.
    messagebox.showinfo("info", "some\ninfo")


def question():
    # icon: ERROR|INFO|QUESTION|WARNING.
    # Yes/No (returns True/False).
    # answer = messagebox.askyesno("?", "To be or not to be?", icon=messagebox.WARNING)
    # Yes/No (returns yes/no).
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    # Ok/Cancel.
    # answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
    # Retry / Cancel.
    # answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
    # Error message, the only button returns ok.
    error = messagebox.showerror("!", "Your code does nothing!")
    # Warning message.
    # error = messagebox.showwarning("Be careful!", "Big Brother is watching you!")
    print(answer)
    print(error)


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


def count():
    global counter
    counter += 1


def digits_only(*args):
    global last_string
    string = text_entry.get()
    if string == '' or string.isdigit():
        # Field's content is valid (digit)
        last_string = string
    else:
        # Set to last valid value
        text_entry.set(last_string)

window = tk.Tk()
window.title('Window title')
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='ca.png'))
window.geometry("400x400")
window.minsize(width=200, height=200)
window.maxsize(width=500, height=500)
window.resizable(width=True, height=True)
# When window is deleted in another way than windows.destroy.
window.protocol("WM_DELETE_WINDOW", clicked)

## Scale.
# A progress bar bound to an IntVar.

## Listbox.
# Create a list
listbox = tk.Listbox(window)
listbox.insert(1, "Python")
listbox.insert(2, "Perl")
listbox.insert(3, "C")
listbox.pack()

## Label, fonts are represented by a tuple, style: bold|italic|underline|overstrike.
# Parameters: text, textvariable (use a stringVar).
label = tk.Label(window, text="My label:", font=("Arial", "16", "bold"))
label.pack()


## Messaqe (very similar to label, with widget size autoformatting).
text = tk.StringVar()
message = tk.Message(window, textvariable=text, width=400)
text.set("A Message")
message.pack()


## Frame.
# Widget mainly used as a container for other widgets: tk.Button(<myFrame>, ...).
# Methods: takefocus (normally would not; but still possible).
frame = tk.Frame(window, height=30, width=100, bg="#000099", cursor="clock")
frame.pack()


## LabelFrame.
# labelanchor: nw|n|ne|wn|w|ws|en|e|es|sw|s|se
labelFrame = tk.LabelFrame(window, text="Label Frame #2", labelanchor='se', width=200, height=100, bg='yellow')
labelFrame.pack()


## Button (inside the label frame).
# Anchor (text position): NW|N|NE|W|CENTER|E|SW|S|SE
# justify=LEFT|CENTER|RIGHT: text alignment inside the button.
# state=DISABLED|NORMAL|ACTIVE: state of the button.
# flash(): the button flashes a few times but does not change its state.
# invoke(): activates the callback assigned to the widget and returns the same value the callback returned.
# master.quit??? Quit and close all???
button = tk.Button(labelFrame, text="Button", command=question)
button["anchor"] = tk.SW
button["borderwidth"] = 10
button["highlightthickness"] = 10
button["padx"] = 10
button["pady"] = 5
button["underline"] = 1
button.pack(fill=tk.X)


## IntVar: observable variable, value change may be observed.
# Typed, also BooleanVar, DoubleVar, StringVar.
# Allows to store a value within the widget, does not appear.
# Allow a bidirectional link between the widget and the variable.
switch = tk.IntVar()
switch.set(1)
switch_value = switch.get()
# Adding an observer to the observable variable (trace_vdelete(id)) would remove the observer).
r_obsid = switch.trace("r", r_observer)
w_obsid = switch.trace("w", w_observer)


# Check button.
# Methods: deselect(), select(), toggle(), invoke(), flash().
# Parameters: bd (frame width), command, variable, justify, state, offvalue, onvalue.
counter=0
checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch, command=count)
checkbutton.pack()


## Text input.
# Parameters: command (tracer function), show (char display replacement), state, textvariable, width
# Methods: get(), set(), delete, (a part of content), insert (a string at an index).
last_string = ''
text_entry = tk.StringVar()
entry = tk.Entry(window, width=30, show="*", textvariable=text_entry)
text_entry.set(last_string)
text_entry.trace('w', digits_only)
entry.pack()


## Radio button.
# Default value depends on switch.
# Methods: deselect(), select(), invoke(), flash().
# Parameters: variable, state, justify, command.
radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
radiobutton_2.pack()


## Menu.

def open_file():
    messagebox.showinfo('title', 'opening a file')


main_menu = tk.Menu(window)
sub_menu_file = tk.Menu(main_menu, tearoff=0)
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
window.config(menu=main_menu)

# Underline: ALT+<Letter> to open the menu.
# tearoff: display a line of dash on the top of the menu.
# accelerator: display text right justified (Still need to bind the event to the window...)
# postcommand: callback invoked every time a menu’s item is activated.
sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q", underline=0, command=window.destroy)

sub_menu_file.add_separator()
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)
sub_menu_file.add_command(label="Disabled", state=tk.DISABLED)
sub_menu_file.add_command(label="Disabled/Enabled entryconfigure", state=tk.DISABLED)
# Change configuration of a menu item/entry.
sub_menu_file.entryconfigure(5, state=tk.ACTIVE)

for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

# sub_menu_help = tk.Menu(main_menu)

main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
main_menu.add_command(label="About...", command=clicked, underline=1)


window.mainloop()