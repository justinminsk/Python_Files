from tkinter import *


class MainWindow:

    def __init__(self, master):
        frame = Frame(root)
        frame.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()
        frame4 = Frame(root)
        frame4.pack()
        frame5 = Frame(root)
        frame5.pack()
        frame6 = Frame(root)
        frame6.pack()
        self.master = master
        var1 = IntVar
        self.cb1 = Checkbutton(frame, text="cheese", variable=var1)
        var2 = IntVar()
        self.cb2 = Checkbutton(frame, text="yogurt", variable=var2)
        var3 = IntVar()
        self.cb3 = Checkbutton(frame, text="milk", variable=var3)
        var4 = IntVar()
        self.cb4 = Checkbutton(frame, text="chicken", variable=var4)
        var5 = IntVar()
        self.cb5 = Checkbutton(frame, text="beef", variable=var5)
        var6 = IntVar()
        self.cb6 = Checkbutton(frame2, text="pork", variable=var6)
        var7 = IntVar()
        self.cb7 = Checkbutton(frame2, text="tv dinners", variable=var7)
        var8 = IntVar()
        self.cb8 = Checkbutton(frame2, text="ice cream", variable=var8)
        var9 = IntVar()
        self.cb9 = Checkbutton(frame2, text="waffles", variable=var9)
        var10 = IntVar()
        self.cb10 = Checkbutton(frame2, text="cereal", variable=var10)
        var11 = IntVar()
        self.cb11 = Checkbutton(frame3, text="coffee", variable=var11)
        var12 = IntVar()
        self.cb12 = Checkbutton(frame3, text="tea", variable=var12)
        var13 = IntVar()
        self.cb13 = Checkbutton(frame3, text="bread", variable=var13)
        var14 = IntVar()
        self.cb14 = Checkbutton(frame3, text="cake", variable=var14)
        var15 = IntVar()
        self.cb15 = Checkbutton(frame3, text="crackers", variable=var15)
        var16 = IntVar()
        self.cb16 = Checkbutton(frame4, text="cookies", variable=var16)
        var17 = IntVar()
        self.cb17 = Checkbutton(frame4, text="water", variable=var17)
        var18 = IntVar()
        self.cb18 = Checkbutton(frame4, text="soda", variable=var18)
        var19 = IntVar()
        self.cb19 = Checkbutton(frame4, text="juice", variable=var19)
        var20 = IntVar()
        self.cb20 = Checkbutton(frame4, text="vegetables", variable=var20)
        var21 = IntVar()
        self.cb21 = Checkbutton(frame5, text="fruit", variable=var21)
        var22 = IntVar()
        self.cb22 = Checkbutton(frame5, text="salads", variable=var22)
        var23 = IntVar()
        self.cb23 = Checkbutton(frame5, text="nuts", variable=var23)
        var24 = IntVar()
        self.cb24 = Checkbutton(frame5, text="jam", variable=var24)
        var25 = IntVar()
        self.cb25 = Checkbutton(frame5, text="peanut butter", variable=var25)
        var26 = IntVar()
        self.cb26 = Checkbutton(frame6, text="paper towels", variable=var26)
        var27 = IntVar()
        self.cb27 = Checkbutton(frame6, text="tooth paste", variable=var27)
        var28 = IntVar()
        self.cb28 = Checkbutton(frame6, text="laundry detergent", variable=var28)

        def get_var():
            v_list = []
            for var in (var1, var2, var3, var4, var5, var6 , var7, var8, var9, var10, var11, var12, var13, var14,
                        var15, var16, var17, var18, var19, var20, var21, var22, var23, var24, var25, var26,
                        var27, var28):
                v_list.append(var.get())
            return v_list

        def get_list(self):
            end_list = []
            grid = {'cheese': (0, 1), 'milk': (0, 2), 'yogurt': (0, 3), 'chicken': (0, 4), 'beef': (0, 5),
                    'pork': (0, 6),
                    'tv dinners': (0, 7), 'ice cream': (0, 8), 'waffles': (0, 9), 'cereal': (0, 1), 'coffee': (3, 1),
                    'tea': (3, 2), 'bread': (3, 3), 'cake': (3, 4), 'crackers': (3, 5), 'cookies': (3, 6),
                    'water': (3, 7),
                    'soda': (3, 8), 'juice': (3, 9), 'vegetables': (6, 1), 'fruit': (6, 1), 'salads': (6, 2),
                    'nuts': (6, 3), 'jam': (6, 4), 'peanut butter': (6, 5), 'paper towels': (6, 6),
                    'tooth paste': (6, 7),
                    'laundry detergent': (6, 8)}
            v_list = get_var()
            index = 0
            for item in v_list:
                if item == 1:
                    end_list.append(grid[index])
                index += 1
            print(end_list)
            return end_list

        self.b2 = Button(self.master, text="Confirm", command=lambda: [f() for f in [self.new_window(), get_list()]])
        self.b1 = Button(self.master, text="Quit", command=quit)
        self.cb1.pack(side=LEFT)
        self.cb2.pack(side=LEFT)
        self.cb3.pack(side=LEFT)
        self.cb4.pack(side=LEFT)
        self.cb5.pack(side=LEFT)
        self.cb6.pack(side=LEFT)
        self.cb7.pack(side=LEFT)
        self.cb8.pack(side=LEFT)
        self.cb9.pack(side=LEFT)
        self.cb10.pack(side=LEFT)
        self.cb11.pack(side=LEFT)
        self.cb12.pack(side=LEFT)
        self.cb13.pack(side=LEFT)
        self.cb14.pack(side=LEFT)
        self.cb15.pack(side=LEFT)
        self.cb16.pack(side=LEFT)
        self.cb17.pack(side=LEFT)
        self.cb18.pack(side=LEFT)
        self.cb19.pack(side=LEFT)
        self.cb20.pack(side=LEFT)
        self.cb21.pack(side=LEFT)
        self.cb22.pack(side=LEFT)
        self.cb23.pack(side=LEFT)
        self.cb24.pack(side=LEFT)
        self.cb25.pack(side=LEFT)
        self.cb26.pack(side=LEFT)
        self.cb27.pack(side=LEFT)
        self.cb28.pack(side=LEFT)
        self.b2.pack()
        self.b1.pack()

    def state(self):
        return map((lambda var: var.get()), self.vars)

    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.get_list()
        bb = Result(self.newWindow)

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func


class Result:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)


if __name__ == '__main__':
    root = Tk()
    b = MainWindow(root)
    root.mainloop()
