def reverseWordsInString(string):
    words = []
    curr_index = len(string) - 1

    while curr_index >= 0:

        current_word = ""
        while curr_index >= 0 and string[curr_index] != ' ':
            current_word += string[curr_index]
            curr_index -= 1
        words.append(current_word[::-1])

        current_spaces = ""
        while curr_index >= 0 and string[curr_index] == ' ':
            current_spaces += ' '
            print(curr_index)
            curr_index -= 1
        words.append(current_spaces)
    
    return "".join(words)