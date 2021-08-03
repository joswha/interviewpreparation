def minimumCharactersForWords(words):
    dicts = [dict() for i in range(len(words))]
    res = {}
    final = []
    
    for index, word in enumerate(words):
        for char in word:
            if char in dicts[index]:
                dicts[index][char] += 1
            else:
                dicts[index][char] = 1
    
    for dictionary in dicts:
        for key, val in dictionary.items():
            if key in res:
                res[key] = max(val, res[key])
            else:
                res[key] = val

    for key in res.keys():
        while res[key] > 0:
            final.append(key)
            res[key] -= 1

    return final