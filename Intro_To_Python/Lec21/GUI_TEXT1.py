import tkinter
def cross(text):
    text.insert(tkinter.INSERT, 'X')

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

text = tkinter.Text(frame, height=4, width=10)
text.pack()

button = tkinter.Button(frame, text='Add', font=('Arial', 18, 'bold'),command=lambda: cross(text))
button.pack()

window.mainloop()
