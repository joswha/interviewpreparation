# Implement an algorithm to determine if a string has all unique characters
def check(word):
    dictionary = {k:0 for k in word}
    for letter in word:
        if dictionary[letter] == 1:
            return False
        dictionary[letter] = 1
    return True

print(check("hey"))