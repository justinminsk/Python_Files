def make_list(readfile):
    hold_list = []  # set up our lists
    main_list = []
    with open(readfile, 'r') as file:  # read out file
        for line in file:  # read each line
            line = line.strip()  # strip each line
            hold_list = line.split()  # create a list for each line
            main_list.insert(len(main_list), hold_list)  # add the list to the main list
        print(main_list)  # show the outcome
    return main_list


if __name__ == '__main__':  # Run the rewrite
    make_list('alkaline_metals.txt')
