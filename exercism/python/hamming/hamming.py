def distance(strand_a, strand_b):
    k = 0
    if(len(strand_a) !=  len(strand_b)):
        raise ValueError("strand_a and strand_b are not the same length")
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            k += 1
    return k