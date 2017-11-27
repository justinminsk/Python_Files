from tkinter import *


class Goodbye:

    def __init__(self):
        pass

    def main_frame(self, master):
        Button(master, text='Goodbye', command=quit).pack()


if __name__ == '__main__':
    master = Tk()
    app = Goodbye()
    app.main_frame(master)
    master.mainloop()
