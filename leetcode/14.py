def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        curr = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != curr:
                return strs[0][:i]
    return strs[0]


strs = ["flower","flow","flight"]
# strs = "flower"
print(longestCommonPrefix(strs))