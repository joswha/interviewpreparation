def groupAnagrams(strs):

    def prod_hash(word):
        word_prod = 1
        for letter in word:
            word_prod *= ord(letter)
        return word_prod

    def sum_hash(word):
        word_sum = 0
        for letter in word:
            word_sum += ord(letter)
        return word_sum

    hash_dict = {prod_hash(k) + sum_hash(k): [] for k in strs}

    for elem in strs:
        hash_dict[prod_hash(elem) + sum_hash(elem)].append(elem)
    
    res = []
    for key, value in hash_dict.items():
        res.append(value)

    return(res)

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)
