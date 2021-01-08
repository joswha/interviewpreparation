import string

def is_pangram(sentence):
    d = dict.fromkeys(string.ascii_lowercase, 0)

    for word in sentence:
        if word.isalpha():
            d[word.lower()] += 1
    
    for val in d.values():
        if val == 0:
            return False

    return True
    # print(d)

# is_pangram("HELLO")
