import re
def abbreviate(words):
    result = ""
    # list_words = re.findall(r'\b\S+\b', words)
    words = words.split()
    for word in words:
        word = word.split('-')
        # print(word)

    print(words)
    for word in words:
        word = word.split('-')
        for word1 in word:
            for letter in word1:
                if letter.isalpha():
                    result += letter.upper()
                    break
        # print(word)
    return result


# print(abbreviate("Hello th-ere"))