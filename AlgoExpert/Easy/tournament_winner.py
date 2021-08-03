def tournamentWinner(competitions, results):
    scores = {}

    max_val = 0
    best_team = ""

    for [c1, c2] in competitions:
        scores[c1] = 0
        scores[c2] = 0
    for i in range(len(results)):
        if results[i] == 1:
            scores[competitions[i][0]] += 1
        else:
            scores[competitions[i][1]] += 1
    for key, val in scores.items():
        if val > max_val:
            max_val = val
            best_team = key
            
    return best_team

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

results = [0, 0, 1]

tournamentWinner(competitions, results)