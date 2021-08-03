def firstNonRepeatingCharacter(string):
    alphabet = {k: 0 for k in string}
    for letter in string:
        alphabet[letter] += 1
    for i in range(len(string)):
        if alphabet[string[i]] == 1:
            return i

print(firstNonRepeatingCharacter("abcdcaf"))