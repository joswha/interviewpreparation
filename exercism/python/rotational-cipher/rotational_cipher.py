import string

# https://stackoverflow.com/questions/63915659/create-dictionary-with-alphabet-characters-mapping-to-numbers
d_lower = dict(enumerate(string.ascii_lowercase))
d_upper = dict(enumerate(string.ascii_uppercase))
# print(d)

# function to return key for any value
def get_key(val):
    if val.islower():
        for key, value in d_lower.items():
            if val == value:
                return key
    elif val.isupper():
        for key, value in d_upper.items():
            if val == value:
                return key
 
    return "no"
    
def rotate(text, key):
    final_string = ""
    for char in text:
        if get_key(char) == "no":
            final_string += char
        else:
            current_key = get_key(char)
            if current_key + key > 25:
                correct_key = key - (26 - current_key)
            else:
                correct_key = current_key + key
            if char.isupper():
                final_string += d_upper[correct_key]
            else:
                final_string += d_lower[correct_key]
    return(final_string)

# print(d_lower)
# print(d_upper)
# print(rotate("Let's eat, Grandma!", 21))