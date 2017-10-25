import time_series_read
def smallest_value(reader):
    """ (file open for reading) -> NoneType
    Read and process reader and return the smallest value after the
    time_seriesheader.
    """
    line = time_series_read.skip_header(reader).strip()
    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = int(line) # first value always expected to be a number
    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line.strip())
            # If we find a smaller value, remember it.
            if value < smallest:
                smallest = value
    return smallest
if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))