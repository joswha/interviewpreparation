# Write a method to replace all spaces in a string with `%20`(in place).  You are given the length of the string.
# Input: "Mr John Smith", 13
# Output: "Mr%20John%20Smith"
def urlify(word):
    final_string = ""
    for letter in word:
        if letter == " ":
            final_string += "%20"
        else:
            final_string += letter
    return final_string

print(urlify("Mr John Smith"))