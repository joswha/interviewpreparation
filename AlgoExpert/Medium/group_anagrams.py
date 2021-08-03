def groupAnagrams(words):
    table = {}
    res = []

    for word in words:
        temp = ''.join(sorted(word))
        if temp in table:
            table[temp].append(word)
        else:
            table[temp] = [word]
    
    for _, value in table.items():
        res.append(value)
    
    return list(table.values())    
    # return res