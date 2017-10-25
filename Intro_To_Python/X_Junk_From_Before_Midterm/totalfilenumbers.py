def sum_number_pairs(input_file, output_filename):
    """ (file open for reading, str) -> NoneType
    Read the data from input_file, which contains two floats per line
    separated by a space. Open file named output_fileand, for each line in
    input_file, write a line to the output file that contains the two floats
    from the corresponding line of input_fileplus a space and the sum of the
    two floats.

    Example:
    
    >>> sum_number_pairs('number_pairs.txt', 'number_pairs_sum.txt')
    """
    with open(output_filename, 'w') as output_file:
        with open(input_file, 'r') as input_file:
            for number_pair in input_file:
                number_pair = number_pair.strip()
                operands = number_pair.split()
                #return(str(operands))
                total = float(operands[0]) + float(operands[1])
                new_line = '{0} {1}\n'.format(number_pair, total)
                output_file.write(new_line)
#if __name__ == '__main__':
    #import doctest
    #doctest.testmod()(verbose = True)
            #the doctest refuses to work and cannot figure out the work around
