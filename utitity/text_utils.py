def is_palindrome (text1):
    if text1 == text1[:: -1]:
        return True
    else:
        return False

def name_format(list_name : list[str]):
    formated_text = []
    for name in list_name:
        prob = name[:-1].capitalize()
        number = name[-1:]

        formated_text.append(prob + ' ' + number)

    return formated_text

def de_format(name : str):
    return name.lower().replace(' ', '')

def squared_grid_from_string (string : str, size):
    grid = [([0] * size)] * size
    num_array = string.split(' ')

    for line in range(len(grid)):
        start = line * size;
        grid[line] = to_int(num_array[start: start + 20])

    return grid

def to_int (str_list : list[str]):
    array = []
    for i in str_list:
        array.append(int(i))
    return array