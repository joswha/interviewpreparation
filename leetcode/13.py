def romanToInt(s):
    switch = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    int_number = 0

    for i in range(len(s) - 1):
        if switch[s[i]] < switch[s[i + 1]]:
            print(s[i], s[i + 1])
            int_number -= switch[s[i]]
            continue
        int_number += switch[s[i]]
    int_number += switch[s[len(s) - 1]]

    return int_number

s = "IV"
print(romanToInt(s))
