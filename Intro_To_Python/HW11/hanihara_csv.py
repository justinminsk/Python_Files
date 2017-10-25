def process_file(file, output_file):
    with open(file, 'r') as r_file:  # read our file
        with open(output_file, 'w') as w_file:  # write over the new file
            line = r_file.readline().strip()  # get the first line we formated
            write_line = '{0}'.format(line)  # make sure it stays formated
            w_file.write(write_line)  # write the line into the csv
            for line in r_file:  # read each line
                line = line.strip()  # strip each line
                if 'Specimen' not in line:  # if it does not contains Specimen
                    line = line.replace(' ', ',')  # add a comma instead of a space
                    write_line = '{0},'.format(line)  # format it to end in a comma
                    w_file.write(write_line)  # write the line
                else:
                    write_line = '\n{0},'.format(line)  # if it contains Specimen it creates a new line then adds a
                    # comma at the end
                    w_file.write(write_line)  # writes to the csv


if __name__ == '__main__':
    process_file('hanihara.txt', 'hanihara.csv')
