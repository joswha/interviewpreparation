def firstUniqueChar(s):
    chars = {k:[] for k in s}
    # print(chars)
    for index, char in enumerate(s):
        chars[char].append(index)
    # print(chars)
    for char in s:
        if len(chars[char]) == 1:
            return chars[char][0]
    return -1

s = "loveleetcode"
print(firstUniqueChar(s))