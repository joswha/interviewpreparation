def generateDocument(characters, document):
    dict_chars = {char: 0 for char in characters}

    for char in characters:
        dict_chars[char] += 1

    for elem in document:
        if elem not in dict_chars or dict_chars[elem] < 0:
            return False
        else:
            dict_chars[elem] -= 1
            if dict_chars[elem] < 0:
                return False

    return True