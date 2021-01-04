def convert(number):
    result = ""
    if number % 7 == 0:
        result += 'Plong'
    if number % 5 == 0:
        result += 'Plang'
    if number % 3 == 0:
        result += 'Pling'
    if len(result) == 0:
        result = str(number)
    return result
