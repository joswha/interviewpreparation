# Implement a method to perform basic string compression using the counts of repeated characters
# aabcccccaaa becomes a2b1c5a3

def compression(word):
    final_string = ""
    k = 1
    for index in range(len(word)):
        if k == 1 :
            final_string += word[index]
        if index + 1 < len(word) and word[index] == word[index + 1]:
            k += 1
        else:
            final_string += str(k)
            k = 1
    
    print(final_string)

compression("bbbbuuuuciiouuuu")