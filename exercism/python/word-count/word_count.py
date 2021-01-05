import re

def count_words(sentence):
    sentence = re.findall(r"[a-z]+'?[a-z]+|[a-z]+|\d+", sentence.lower())
    
    word_list = {}

    for word in sentence:
        word_list[word] = sentence.count(word)

    return word_list   
    # print(word_list)        

# count_words("Joe can't tell between 'large' and large.")
