def underscorifySubstring(string, substring):
    """
    "string": "testthis is a testest to see if testestes it works",
    "substring": "test"

    Output: "_test_this is a _testest_ to see if _testest_es it works"
    """
    index = 0
    j = 0
    possible_finish = 0
    possible_begin = 0
    print(string, substring)
    while index < len(string):
        if string[index] == substring[0]:
            if possible_finish == 0:
                possible_begin = index
            index += 1
            j = 1

            while j < len(substring) and index < len(string) and string[index] == substring[j]:
                index += 1
                j += 1

            if j == len(substring) - 1: # finished matching the entire substring
                possible_finish = index
            j = 0
        else:
            index += 1
            if possible_finish != 0:
                print(f"POSSIBLE BEGIN INDEX: {str(possible_begin)} WITH ENDING INDEX: {str(possible_finish)} ")
                possible_finish = 0

    # j = 0
    # good_finish = []

    # # print(string)
    # for i in range(len(string)):
    #     if j < len(substring) and string[i] == substring[j]:
    #         j += 1
    #         print(string[i], j)
        
    #     if j == len(substring) - 1:
    #         good_finish.append(i) #  +1 to get the `test` last index in the string a
    #         j = 0


    # print(string, good_finish)

    # cuvinte = string.split(" ")
    # res = []

    # for cuv in cuvinte:
        
    #     j = 0
    #     good_finish = 0
    #     for i in range(len(cuv)):
    #         if j < len(substring) - 1 and substring[j] == cuv[i]:
    #             j += 1

    #         if j == len(substring) - 1:
    #             good_finish = i
    #             j = 0
        
    #     if good_finish != 0:
    #         res.append(f"_{cuv[:good_finish + 2]}_{cuv[good_finish + 2:]}")
    #     else:
    #         res.append(cuv)

    # return " ".join(res)

# string = "testthis is a testtest to see if testestes it works"
# substring = "test"
string = "tzttztttzttz"
substring = "ttt"
expected_output = "tztz_ttt_z"

underscorifySubstring(string, substring)