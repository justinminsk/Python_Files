def grid_name():
    """() -> 2d array
    Create a store array to use in the store router program. This creates the item name.
    """
    store_item = ['entrance', 'cheese', 'milk', 'yogurt', 'chicken', 'beef', 'pork', 'tv dinners', 'ice cream', 'waffles',
                  'cereal', 'coffee', 'tea', 'bread', 'cake', 'crackers', 'cookies', 'water', 'soda', 'juice'
                  'vegetables', 'fruit', 'salads', 'nuts', 'jam', 'peanut butter', 'paper towels', 'tooth paste',
                  'laundry detergent']
    return store_item


def grid_measurements():
    """() -> 2d array
    Create a store array to use in store router program. This creates a list of measurements.
    """
    store_mesurements = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    return store_mesurements


def grid_id(grid_measurements):
    """(array) -> 2d array
    Create a store array to use in store router program. This creates a list of ids.
    """
    store_id =[0]
    count = 1
    for mesurement in grid_measurements:
        if count <= 9:
            store_id.append(count)
            count += 1
        else:
            count = 1
            store_id.append(count)
    return store_id


def grid_create(grid_name, grid_measurements, grid_id):
    """(arrays) -> dict
    Create the grid for the store router app.
    """
    grid_zip = zip(grid_measurements, grid_id)
    grid_list = tuple(grid_zip)
    grid_zip = zip(grid_name, grid_list)
    grid_dict = dict(grid_zip)
    return grid_dict


def grid():
    """() -> dict
    Create an easy to get grid function.
    """
    return grid_create(grid_name(), grid_measurements(), grid_id(grid_measurements()))


if __name__ == '__main__':
    print(grid())