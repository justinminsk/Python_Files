import tkinter
import datetime
window = tkinter.Tk()
ldata = tkinter.StringVar()
ldata.set(str(datetime.datetime.now())[11:16])
label = tkinter.Label(window, textvariable=ldata)
ldata.set(str(datetime.datetime.now())[0:10])
label = tkinter.Label(window, textvariable=ldata)
label.pack()
window.mainloop()

# change format of date:
print (datetime.datetime.strptime(str(datetime.datetime.now())[0:10], '%Y-%m-%d').strftime('%m/%d/%y'))

