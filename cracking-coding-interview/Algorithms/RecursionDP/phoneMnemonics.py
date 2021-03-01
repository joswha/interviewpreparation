mapping = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrx',
    '8': 'tuv',
    '9': 'wxyz'
}

def phone_mnemonics(digits, word):
    
    letters = mapping[digits[0]]
    if len(digits) == 1:
        for letter in letters:
            print(word + letter)
    else:
        for letter in letters:
            phone_mnemonics(digits[1:], word + letter)

def generateWords(digits):
    phone_mnemonics(digits, '')

generateWords('22834')