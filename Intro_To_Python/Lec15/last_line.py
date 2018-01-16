def last_line(filename):
	with open(filename, 'r') as example_file:
		lines = example_file.readlines()
		last_line = lines[-1]
	return last_line


if __name__ == '__main__':
    print(last_line('birdlist.txt'))