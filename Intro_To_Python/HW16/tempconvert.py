from tkinter import *


class TempConverter:

    def __init__(self):
        pass

    def main_frame(self, master):

        def convert_to_Fahrenheit(fahrenheit, var):
            num = fahrenheit.get()
            end_num = (num - 32.0) * 5.0 / 9.0
            var.set('{:0.1f}'.format(end_num))

        var_int = DoubleVar()
        var_text = StringVar()
        print(var_text)
        Label(master, text='Temperature in Fahrenheit:').pack()
        Entry(master, textvar=var_int).pack()
        Label(master, textvar=var_text).pack()
        Button(master, text='Convert', command=lambda: convert_to_Fahrenheit(var_int, var_text)).pack()
        Button(master, text='Quit', command=quit).pack()


if __name__ == '__main__':
    master = Tk()
    app = TempConverter()
    app.main_frame(master)
    master.mainloop()