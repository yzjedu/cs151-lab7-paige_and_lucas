# your code
def input_float():

def floor_size():
    width = input('width')
    while not width.isdigit()
    length = int(input('length'))
    area = width * length
    return area
def floor_style():
    floor_type = input('flooring type')
    return floor_type
def room_cost():
    floor_type = floor_style()
    area = floor_size()
    hardwood_cost = 1.39
    carpet_cost = 3.99
    tile_cost = 4.99
    if floor_type == 'hard':
        cost = hardwood_cost * area
        return cost
    elif floor_type == 'carpet':
        cost = carpet_cost * area
        return cost
    else:
        cost = tile_cost * area
        return cost


def main():
    count = 0
    while count < 5:
        cost = room_cost()
        count += 1
        print(cost)


main()