def alph_order(filename):
    with open(filename, 'r') as example_file:
        lines = example_file.readlines()
        alph_lines = sorted(lines)
    return alph_lines


if __name__ == '__main__':
	for planet in alph_order('planets.txt'):
            print(planet.strip())
