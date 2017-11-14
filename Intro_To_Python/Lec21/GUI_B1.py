import tkinter
window = tkinter.Tk()
label = tkinter.Label(window, text='This is our label.')
label.pack()  # makes sure label is readable
# or label = tkinter.Label(window, text='This is our label.').pack()
window.mainloop()
