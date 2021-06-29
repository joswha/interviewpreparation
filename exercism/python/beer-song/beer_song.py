def recite(start, take=1): 
    total = start
    final = []
    for i in range(start, 1, -1):
        final.append(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.")
        final.append("")
        final.append("nTake one down and pass it around, " + str(i - 1) + " bottles of beer on the wall.")

    final.append((str(1) + " bottle of beer on the wall, " + str(1) + " bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.")
    
    print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, " + str(total) + " bottles of beer on the wall.")


recite(11, 1)
