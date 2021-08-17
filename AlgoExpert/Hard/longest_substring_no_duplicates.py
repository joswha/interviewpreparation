def longestSubstringWithoutDuplication(string):
    table = {}
    queue = []
    
    max_length = float('-inf')
    curr_string = ""
    max_length_string = ""
    curr_len = 0

    for char in string:
        if char not in table:
            table[char] = 1
            queue.append(char)
            
            curr_len += 1
            curr_string += char

            if curr_len > max_length:
                max_length_string = curr_string
                max_length = curr_len
        
        else: # it already exists in the table
            check_char = queue.pop(0)
            table.pop(check_char)
            curr_string = curr_string[1:]
            curr_len -= 1

            # we get rid of the already existing character, wherever it is
            # (and with the characters in front of it) since we won't use them anyway
            while check_char != char:
                check_char = queue.pop(0)
                table.pop(check_char)
                curr_string = curr_string[1:]
                curr_len -= 1
            
            # and then reappend it, since we're going to continue from 
            # the element next to the `char`'s previous position in the string
            table[char] = 1
            queue.append(char)
            curr_len += 1
            curr_string += char
            
    return max_length_string