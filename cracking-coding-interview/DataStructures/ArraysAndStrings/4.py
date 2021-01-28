# Given a string, write a function to check if it is a permutation of a palindrome.
def palindromePermutation(word):
    word = word.lower()
    word = word.replace(" ", "") #replace any redundant extra characters
    letter_dictionary = {k:0 for k in word}
    # print(letter_dictionary)
    for letter in word:
        letter_dictionary[letter] += 1
    
    how_many_odd = 0
    # A palindrome has string has only one of the letters occuring odd-number of times, 
    # while the rest of the letters occur even number of times
    for value in letter_dictionary.values():
        if value % 2 == 1:
            how_many_odd += 1
        if how_many_odd >=2:
            return False
    return True

print(palindromePermutation("Tact Coa"))