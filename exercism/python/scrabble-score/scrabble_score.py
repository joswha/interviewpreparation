def score(word):
    scrabble_scores = {
        1: ["A","E","I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    total = 0

    for letter in word:
        for key in scrabble_scores.keys():
            if letter in scrabble_scores[key] or letter.upper() in scrabble_scores[key]:
                total += key

    return total

