
def is_isogram(string):
    vf = {}
    for letter in string:
        if letter != '-' and letter != ' ' and letter in  vf:
            vf[letter] += 1
        elif letter != '-' and letter != ' ' and letter not in  vf:
            vf[letter] = 1
        if vf[letter] >= 2:
            return False
    return True
