# Purpose: Get the area of the room
# Parameter: none
# Return: area
def floor_size():
    width = input('Please enter the width of the room: ')
    temp = width.replace('.', '')

    while not temp.isdigit():
        print("invalid input")
        width = input('Please enter the width of the room: ')
        temp = width.replace('.', '')

    length = input('Please enter the length of the room: ')
    temp = length.replace('.', '')

    while not temp.isdigit():
        print("invalid input")
        length = input('length')
        temp = length.replace('.', '')
    area = float(width) * float(length)
    return area

# Purpose: Get the floor style
# Parameter: none
# Return: floor type
def floor_style():
    floor_type = input('Enter the desired floor type (hardwood, carpet, or tile): ')
    while floor_type not in {'hardwood', 'carpet', 'tile'}:
        print('invalid input')
        floor_type = input('Please enter the desired floor type (hardwood, carpet, or tile): ')
    return floor_type

# Purpose: determine cost for 1 room's floor from area and floor style
# Parameter: none
# Return: cost
def room_cost():
    floor_type = floor_style()
    area = floor_size()
    hardwood_cost = 1.39
    carpet_cost = 3.99
    tile_cost = 4.99
    if floor_type == 'hard':
        cost = hardwood_cost * area
    elif floor_type == 'carpet':
        cost = carpet_cost * area
    else:
        cost = tile_cost * area
    return cost

# Purpose: put code together and repeat 5 times
# Parameter: none
# Return: none
def main():
    count = 0
    total_cost = 0
    print('This program will calculate the total cost to re-do all of your flooring.\n')
    while count < 5:
        cost = room_cost()
        count += 1
        print(f'Your cost to replace the flooring in room {count} is ${cost:.2f}\n')
        total_cost += cost
    print(f'Your total cost for all the rooms is ${total_cost:.2f}')


main()
