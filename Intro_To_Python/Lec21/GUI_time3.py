import tkinter
import datetime
window = tkinter.Tk()
# date (yyyy-mm-dd 24:12.12.123456)
label = tkinter.Label(window, text=datetime.datetime.now()).pack()
# time only
#label = tkinter.Label(window, text=str(datetime.datetime.now())[11:16]).pack()
# date only
#label = tkinter.Label(window, text=str(datetime.datetime.now())[0:10]).pack()
# date and time
#label = tkinter.Label(window, text=str(datetime.datetime.now())[0:16]).pack()
window.mainloop()
