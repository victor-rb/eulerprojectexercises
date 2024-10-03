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