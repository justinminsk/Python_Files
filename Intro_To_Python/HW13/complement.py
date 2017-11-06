#  1. change the letter to its pair then search for that new string
#  Make a statement that reads each letter then saves it's complement into a new string.
def complement(dna):
    comp = ''
    for letter in dna:
        if letter == 'A' or letter == 'a':
            comp += 'T'
        if letter == 'T' or letter == 't':
            comp += 'A'
        if letter == 'G' or letter == 'g':
            comp += 'C'
        if letter == 'C' or letter == 'c':
            comp += 'G'
    print(comp)
    return comp


if __name__ == '__main__':
    complement('ACTCGCTTCGCTATAAGCTAGGCAT')
