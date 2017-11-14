import tkinter

window = tkinter.Tk()

# The model.
counter = tkinter.IntVar()
counter.set(0)

# One general controller. This also works - we are only modifying counter in this program
def click(value):
    counter.set(counter.get() + value)

# The views.
frame = tkinter.Frame(window)
frame.pack()

button = tkinter.Button(frame, text='Up', command=lambda: click(1))
button.pack()
button = tkinter.Button(frame, text='Down', command=lambda: click(-1))
button.pack()

label = tkinter.Label(frame, textvariable=counter)
label.pack()

window.mainloop()
