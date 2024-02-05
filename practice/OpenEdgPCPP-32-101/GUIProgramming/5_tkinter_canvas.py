import tkinter as tk
# import Pillow as PIL

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# smooth: change the angles.
canvas.create_line(
    10, 380, 200, 10, 380, 380, 10, 380,
    arrow=tk.BOTH,
    fill='red',
    smooth=True,
    width=3
)
canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')
canvas.create_polygon(100, 380, 50, 68, 50, 380, outline='red', width=5, fill='yellow')
canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')
# style: PIESLICE|CHORD|ARC
canvas.create_arc(
    10, 100, 380, 300,
    outline='green',
    width=5,
    style=tk.PIESLICE,
    start=180,
    extent=180
)
canvas.create_text(200, 200, text="Mary\nhad", font=("Arial","40","bold"), justify=tk.CENTER, fill='black')

image = tk.PhotoImage(file='ca.png')
# jpg
# jpg = PIL.Image.open('logo.jpg')
# image = PIL.ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)

button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
