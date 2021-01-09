def hashNew(word):
    total = 0
    word = word.lower()
    for letter in word:
        total += ord(letter)
    return total

def checkLetters(stringa,stringb):
    stringa = stringa.lower()
    stirngb = stringb.lower()
    for a in stringa:
        if a not in stringb:
            return False
    return True

def checkIfSameWord(word1,word2):
    return (word1.lower() == word2.lower())

def find_anagrams(word, candidates):
    expected = []
    word = word.lower()
    for candidate in candidates:
        if (hashNew(word) == hashNew(candidate)) and checkLetters(candidate, word) and not checkIfSameWord(candidate, word):
            expected.append(candidate)
    return expected

# Could have also ordered the characters in the word and checked if it was equal to the other word...
