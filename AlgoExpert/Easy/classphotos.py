def classPhotos(redShirtHeights, blueShirtHeights):
    
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    # start from the back(since then you would know the tallest from both -> only possible arrangement if any)
    
    n = len(blueShirtHeights) - 1
    
    for i in range(len(redShirtHeights)):
        if redShirtHeights[n] > blueShirtHeights[n]:
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False
    
    return True
