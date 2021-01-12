from itertools import groupby

def decode(string):
    number = ''
    s = ''
    for index in range(len(string)):
        if string[index].isdigit():
            number += string[index]
        elif not number:
            s += string[index]
        else:
            s += str(int(number) * string[index])
            number = ''
    return s


def encode(string):
    # k = 1
    # val = ''
    # final = ''
    # for index in range(len(string) - 1):
    #     if string[index] == string[index + 1]:
    #         k += 1
    #         val = string[index]
    #     else:
    #         if k > 1:
    #             final += str(k) + val
    #         else:
    #             final += string[index]
    #         val = ''
    #         k = 1

    # if string[-1] != string [-2]: #check for final character, as for goes (len - 1)
    #     final += string[-1]
	final = ''
	for k, g in groupby(string):
		section = sum(1 for _ in g)
		if section > 1:
			final += str(section) + k
		else:
		 	final += k
	return final

# encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
# print(decode("12WB12W3B24WB"))
# should_be = "12WB12W3B24WB"
# actual =    "12WB12W3B24WB"
