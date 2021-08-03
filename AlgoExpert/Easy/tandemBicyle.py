def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    _sum = 0
    n = len(redShirtSpeeds)
    for i in range(n):
        if fastest:
            _sum += max(redShirtSpeeds[n - i - 1], blueShirtSpeeds[i])
        else:
            _sum += min(redShirtSpeeds[n - i - 1],blueShirtSpeeds[i])
    return _sum