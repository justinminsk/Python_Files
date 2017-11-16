from tkinter import *
from tsp_solver.greedy import solve_tsp

class StoreRouter:

    def __init__(self):
        pass

    def main_frame(self, master):
        # get frames to make the lists more organized
        frame = Frame(master)
        frame.pack()
        frame2 = Frame(master)
        frame2.pack()
        frame3 = Frame(master)
        frame3.pack()
        frame4 = Frame(master)
        frame4.pack()
        frame5 = Frame(master)
        frame5.pack()
        frame6 = Frame(master)
        frame6.pack()
        # create the check boxes and the variable that goes along with them
        self.var1 = IntVar()
        Checkbutton(frame, text="cheese", variable=self.var1).pack(side=LEFT)
        self.var2 = IntVar()
        Checkbutton(frame, text="yogurt", variable=self.var2).pack(side=LEFT)
        self.var3 = IntVar()
        Checkbutton(frame, text="milk", variable=self.var3).pack(side=LEFT)
        self.var4 = IntVar()
        Checkbutton(frame, text="chicken", variable=self.var4).pack(side=LEFT)
        self.var5 = IntVar()
        Checkbutton(frame, text="beef", variable=self.var5).pack(side=LEFT)
        self.var6 = IntVar()
        Checkbutton(frame2, text="pork", variable=self.var6).pack(side=LEFT)
        self.var7 = IntVar()
        Checkbutton(frame2, text="tv dinners", variable=self.var7).pack(side=LEFT)
        self.var8 = IntVar()
        Checkbutton(frame2, text="ice cream", variable=self.var8).pack(side=LEFT)
        self.var9 = IntVar()
        Checkbutton(frame2, text="waffles", variable=self.var9).pack(side=LEFT)
        self.var10 = IntVar()
        Checkbutton(frame2, text="cereal", variable=self.var10).pack(side=LEFT)
        self.var11 = IntVar()
        Checkbutton(frame3, text="coffee", variable=self.var11).pack(side=LEFT)
        self.var12 = IntVar()
        Checkbutton(frame3, text="tea", variable=self.var12).pack(side=LEFT)
        self.var13 = IntVar()
        Checkbutton(frame3, text="bread", variable=self.var13).pack(side=LEFT)
        self.var14 = IntVar()
        Checkbutton(frame3, text="cake", variable=self.var14).pack(side=LEFT)
        self.var15 = IntVar()
        Checkbutton(frame3, text="crackers", variable=self.var15).pack(side=LEFT)
        self.var16 = IntVar()
        Checkbutton(frame4, text="cookies", variable=self.var16).pack(side=LEFT)
        self.var17 = IntVar()
        Checkbutton(frame4, text="water", variable=self.var17).pack(side=LEFT)
        self.var18 = IntVar()
        Checkbutton(frame4, text="soda", variable=self.var18).pack(side=LEFT)
        self.var19 = IntVar()
        Checkbutton(frame4, text="juice", variable=self.var19).pack(side=LEFT)
        self.var20 = IntVar()
        Checkbutton(frame4, text="vegetables", variable=self.var20).pack(side=LEFT)
        self.var21 = IntVar()
        Checkbutton(frame5, text="fruit", variable=self.var21).pack(side=LEFT)
        self.var22 = IntVar()
        Checkbutton(frame5, text="salads", variable=self.var22).pack(side=LEFT)
        self.var23 = IntVar()
        Checkbutton(frame5, text="nuts", variable=self.var23).pack(side=LEFT)
        self.var24 = IntVar()
        Checkbutton(frame5, text="jam", variable=self.var24).pack(side=LEFT)
        self.var25 = IntVar()
        Checkbutton(frame5, text="peanut butter", variable=self.var25).pack(side=LEFT)
        self.var26 = IntVar()
        Checkbutton(frame6, text="paper towels", variable=self.var26).pack(side=LEFT)
        self.var27 = IntVar()
        Checkbutton(frame6, text="tooth paste", variable=self.var27).pack(side=LEFT)
        self.var28 = IntVar()
        Checkbutton(frame6, text="laundry detergent", variable=self.var28)
        # create our quit button and our button that creates the results
        Button(master, text="Confirm", command=self.result_frame).pack()
        Button(master, text="Quit", command=quit).pack()

    def result_frame(self):
        v_list = []
        x = 0
        while x < 28:
            query = [self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.var8, self.var9,
             self.var10, self.var11, self.var12, self.var13, self.var14, self.var15, self.var16, self.var17,
             self.var18, self.var19, self.var20, self.var21, self.var22, self.var23, self.var24, self.var25,
             self.var26, self.var27, self.var28]
            v_list.append(query[x].get())
            x += 1
        grocery_list = []
        grid = {'cheese': (0, 1), 'milk': (0, 2), 'yogurt': (0, 3), 'chicken': (0, 4), 'beef': (0, 5), 'pork': (0, 6),
                'tv dinners': (0, 7), 'ice cream': (0, 8), 'waffles': (0, 9), 'cereal': (0, 1), 'coffee': (3, 1),
                'tea': (3, 2), 'bread': (3, 3), 'cake': (3, 4), 'crackers': (3, 5), 'cookies': (3, 6), 'water': (3, 7),
                'soda': (3, 8), 'juice': (3, 9), 'vegetables': (6, 1), 'fruit': (6, 1), 'salads': (6, 2),
                'nuts': (6, 3), 'jam': (6, 4), 'peanut butter': (6, 5), 'paper towels': (6, 6) ,'tooth paste': (6, 7),
                'laundry detergent': (6, 8)}
        food_lst = ['cheese', 'milk', 'yogurt', 'chicken', 'beef', 'pork', 'tv dinners', 'ice cream', 'waffles',
                    'cereal', 'coffee', 'tea', 'bread', 'cake', 'crackers', 'cookies', 'water', 'soda', 'juice',
                    'vegetables', 'fruit', 'salads', 'nuts', 'jam', 'peanut butter', 'paper towels', 'tooth paste',
                    'laundry detergent']
        index = 0
        g_food_list = []
        while index < 28:
            if v_list[index] == 1:
                grocery_list.append(grid[food_lst[index]])
                g_food_list.append(food_lst[index])
            index += 1
        result = Toplevel()
        result.title('Shopping list')
        shopping_matrix = []
        index = 0
        for coord in grocery_list:
            temp_list = []
            index_2 = 0
            for item in grocery_list:
                coord1 = grocery_list[index]
                coord_x1 = coord1[0]
                coord_y1 = coord1[1]
                coord2 = grocery_list[index_2]
                coord_x2 = coord2[0]
                coord_y2 = coord2[1]
                if coord_x2 == coord_x1:
                    distance = ((coord_x1 - coord_x2) ** 2 + (coord_y1 - coord_y2) ** 2) ** 0.5
                else:
                    if coord_y1 > 4:
                        distance = (10 - coord_y1) + abs(coord_x2 - coord_x1) + (10 - coord_y2)
                    if coord_y1 <= 4:
                        distance = coord_y1 + abs(coord_x2 - coord_x1) + coord_y2
                index_2 += 1
                temp_list.append(distance)
            shopping_matrix.append(temp_list)
            index += 1
        ordered_list = solve_tsp(shopping_matrix)
        shopping_list = []
        for number in ordered_list:
            shopping_list.append(g_food_list[number])
        Label(result, text=shopping_list).pack()
        Button(result, text="OK", command=result.destroy).pack()


if __name__ == '__main__':
    master = Tk()
    app = StoreRouter()
    app.main_frame(master)
    master.mainloop()


""" def get_var(self):
        v_list = []
        for var in [self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.var8, self.var9,
                    self.var10, self.var11, self.var12, self.var13, self.var14, self.var15, self.var16, self.var17,
                    self.var18, self.var19, self.var20, self.var21, self.var22, self.var23, self.var24, self.var25,
                    self.var26, self.var27, self.var28]:
            v_list.append(self.var.get())
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
        v_list = self.get_var()
        index = 0
        for item in v_list:
            if item == 1:
                end_list.append(grid[index])
            index += 1
        print(end_list)
        return end_list"""
