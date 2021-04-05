def lengthOfLongestSubstring(s):
    window = []
    max_len = 0
    for elem in s:
        if elem not in window:
            window.append(elem)
            n = len(window)
            if n > max_len:
                max_len = n
        else:
            cont = window.index(elem)
            window = window[cont + 1:] + [elem]
    return max_len

s = "aab"

print(lengthOfLongestSubstring(s))