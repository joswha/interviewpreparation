def to_rna(dna_strand):
    final_string = ""

    for char in dna_strand:
        if char == 'G':
            final_string += 'C'
        elif char == 'C':
            final_string += 'G'
        elif char == 'T':
            final_string += 'A'
        elif char == 'A':
            final_string += 'U'
        else:
            pass    

    return final_string


# https://docs.python.org/2/library/string.html#string.translate
# Transposition maybe?

# def to_rna(strand):

#     dna_to_rna = {'G' : 'C',
#                   'C' : 'G',
#                   'T' : 'A',
#                   'A' : 'U'}

#     return ''.join([dna_to_rna[mol] for mol in strand])