# Given two strings, write a method to decide if one is a permutation of the other
# eg. abba baab
def hashing(word):
    sum = 0
    for letter in word:
        sum += ord(letter)
    return sum


def check(word1, word2):
    if len(word1) == len(word2) and hashing(word1) == hashing(word2):
        return True
    return False

print(check("hello", "ellho"))