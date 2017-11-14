import tkinter
import datetime
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
frame2 = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
frame2.pack()
first = tkinter.Label(frame, text='Date and Time')
first.pack()
second = tkinter.Label(frame2, text='Date: ' + str(datetime.datetime.now())[0:10])
second.pack()
third = tkinter.Label(frame2, text='Time: ' + str(datetime.datetime.now())[10:16])
third.pack()
window.mainloop()
