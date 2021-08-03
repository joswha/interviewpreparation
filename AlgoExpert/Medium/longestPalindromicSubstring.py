def longestPalindromicSubstring(string):
    
    trier = 0
    max_len = float('-inf')
    start_index = 0

    while trier < len(string):

        left = trier
        right = len(string) - 1
        current_len = 0

        while left <= right:
            if string[left] == string[right]:
                if current_len == 0:
                    start_index = left
                current_len += 2
                left += 1
            right -= 1

        max_len = max(max_len, current_len)

        if max_len >= len(string) // 2:
            break

        trier += 1

    return string[start_index: start_index + max_len]
    