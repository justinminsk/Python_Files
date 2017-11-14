import tkinter
import datetime
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
first = tkinter.Label(frame, text='Date and Time')
first.pack()
second = tkinter.Label(frame, text='Date: ' + datetime.datetime.strptime(str(datetime.datetime.now())[0:10], '%Y-%m-%d').strftime('%m/%d/%y') )
second.pack()
third = tkinter.Label(frame, text='Time: ' + str(datetime.datetime.now())[10:16])
third.pack()
window.mainloop()
