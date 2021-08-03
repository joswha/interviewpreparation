def isPalindrome(string):
    if len(string) % 2 == 1:
        return (string[:(len(string) // 2)] == string[(len(string) // 2 + 1):][::-1])
    else:
        return (string[:(len(string) // 2)] == string[(len(string) // 2):][::-1])