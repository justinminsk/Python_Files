from tkinter import *


class DNACounter:

    def __init__(self):
        pass

    def main_frame(self, master):
        text = Text(master)
        text.pack()
        var_text = StringVar()

        def count(text, var):
            str_text = text.get('0.0', END)
            A = 0
            T = 0
            C = 0
            G = 0
            for char in str_text:
                if 'A' in char:
                    A += 1
                elif 'T' in char:
                    T += 1
                elif 'C' in char:
                    C += 1
                elif 'G' in char:
                    G += 1
            var.set('Num As: {0} \t Num Ts: {1} \t Num Cs: {2} \t Num Gs: {3}'.format(A, T, C, G))

        Button(master, text='Count', command=lambda: count(text, var_text)).pack()
        Label(master, textvar=var_text).pack()


if __name__ == '__main__':
    master = Tk()
    app = DNACounter()
    app.main_frame(master)
    master.mainloop()
