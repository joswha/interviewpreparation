# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to
# isSubstring(e.g, "waterbottle" is rotation of "erbottlewat"
def isSubstring(s1, s2):

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2:
            return True

    return False

print(isSubstring("waterbottle", "erbottlewat"))