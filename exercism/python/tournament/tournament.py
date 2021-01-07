from collections import defaultdict

def tally(rows):

    cp_row = ""

    for row in rows:
        cp_row += (row + '\n')

    # print(cp_row)

    rows = cp_row

    rows = rows.replace('\n', ';')
    rows = rows.split(';')

    # print(rows)

    values_dict = defaultdict(list)

    for index in range(0, len(rows)):
        if rows[index] != "" and len(rows[index]) > 4 and rows[index] not in values_dict:
            values_dict[rows[index]] = {'matches_played': 0, 'wins' : 0, 'draws' : 0, 'losses': 0, 'points' : 0}

    # print(values_dict)
    # print(rows[:-1])

    for index in range(0, len(rows[:-1]), 3):
        values_dict[rows[index]]['matches_played'] += 1
        values_dict[rows[index + 1]]['matches_played'] += 1

        if rows[index + 2] == 'win':
            values_dict[rows[index]]['wins'] += 1
            values_dict[rows[index]]['points'] += 3
            values_dict[rows[index + 1]]['losses'] += 1
            
        elif rows[index + 2] == 'loss':
            values_dict[rows[index]]['losses'] += 1
            values_dict[rows[index + 1]]['wins'] += 1
            values_dict[rows[index + 1]]['points'] += 3

        elif rows[index + 2] == 'draw':
            values_dict[rows[index]]['draws'] += 1
            values_dict[rows[index]]['points'] += 1
            values_dict[rows[index + 1]]['draws'] += 1
            values_dict[rows[index + 1]]['points'] += 1

    # for t in sorted(sorted(values_dict.values(), key=lambda s:s['Team']), key=lambda r:r['P'], reverse=True
    print(sorted(values_dict[key]['points'] for key in values_dict.keys(), reverse= True))

    final_string = "Team                           | MP |  W |  D |  L |  P\n"

    for key, values in values_dict.items():
        for value in values.values():
            final_string += (f"{key}" + (31 - len(key)) * " " +  f"|  {values_dict[key]['matches_played']} |  {values_dict[key]['wins']} |  {values_dict[key]['draws']} |  {values_dict[key]['losses']} |  {values_dict[key]['points']}\n")
            break

    # return(final_string)[:-1]

    final_array = []

    for final_string_value in final_string.split('\n'):
        final_array.append(final_string_value)
    
    # return final_array[:-1]


    


results = [
    "Courageous Californians;Devastating Donkeys;win",
    "Allegoric Alaskans;Blithering Badgers;win",
    "Devastating Donkeys;Allegoric Alaskans;loss",
    "Courageous Californians;Blithering Badgers;win",
    "Blithering Badgers;Devastating Donkeys;draw",
    "Allegoric Alaskans;Courageous Californians;draw",
]

print(tally(results))
