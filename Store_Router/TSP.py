def get_from_grid(item):
    """dict -> set
    Call the grid item and get it's coordinates.
    """
    import Grid_Creator
    grid = Grid_Creator.grid()
    item_coord = grid[item]
    return item_coord


def get_distance(start_location, end_location):
    """set -> float
    Finds the distance between two points in our grid.
    >>>get_distance('cheese', 'pork')
    5.0
    >>>get_distance('cheese', 'laundry detergent')
    10.0
    """
    coord1 = get_from_grid(start_location)
    coord_x1 = coord1[0]
    coord_y1 = coord1[1]
    coord2 = get_from_grid(end_location)
    coord_x2 = coord2[0]
    coord_y2 = coord2[1]
    distance = ((coord_x1 - coord_x2)**2 + (coord_y1 - coord_y2)**2)**0.5
    return distance


def grocery_list(gl):
    """text doc -> list
    Takes a text document list with one item per a line and makes into a list or strings.
    """
    import Grid_Creator
    grid = Grid_Creator.grid()
    end_list = []
    with open(gl, 'r') as gr_list:
        for word in gr_list:
            word = word.strip()
            for key in grid:
                if key == word:
                    end_list.append(word)
    return end_list


def tsp(start_item, gl):
    """string -> string
    Part of the greedy tsp algorithm comparing the distances form location to next location.
    """
    smallest_distance = 100000
    next_item = ''
    for item in gl:
        if item == start_item:
            continue
        else:
            distance = get_distance(start_item, item)
            if distance < smallest_distance:
                smallest_distance = distance
                next_item = item
    return next_item


def tsp_greedy(gl):
    """string -> list
     Greedy tsp algorithm, finding the shortest distance at each interval.
    """
    g_list = grocery_list(gl)
    entrance = 'entrance'
    g_list.insert(0, entrance)
    item = tsp(g_list[0], g_list)
    g_list.remove('entrance')
    end_list = []
    while len(g_list) > 0:
        end_list.append(item)
        item = tsp(item, g_list)
        g_list.remove(item)
    return end_list


if __name__ == '__main__':
    print(tsp_greedy('grocer_list.txt'))
