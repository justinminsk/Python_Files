import tkinter

# The controller (modifies data)
def click():
    counter.set(counter.get() + 1)

if __name__ == '__main__':
    window = tkinter.Tk()

    # The model (stores data)
    counter = tkinter.IntVar()
    counter.set(0)

    # The views (displays data)
    frame = tkinter.Frame(window)
    frame.pack()
    button = tkinter.Button(frame, text='Click', command=click)
    button.pack()
    label = tkinter.Label(frame, textvariable=counter)
    label.pack()

    # Start the machinery!
    window.mainloop()

# IF you want to print the last number
#print(counter.get())
