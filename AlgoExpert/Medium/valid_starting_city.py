def validStartingCity(distances, fuel, mpg):
    n = len(distances)
    remaining_miles = 0

    start_index = 0
    start_miles = 0

    for index in range(1, n):
        prev_distance = distances[index - 1]
        prev_fuel = fuel[index - 1]
        remaining_miles += (prev_fuel * mpg - prev_distance)

        if remaining_miles < start_miles:
            start_miles = remaining_miles
            start_index = index
    
    return start_index
