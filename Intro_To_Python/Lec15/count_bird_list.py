# count_bird_list.py

observations_file = open('birdlist.txt')
bird_counts = []
for line in observations_file:
    bird = line.strip()
    found = False
# Find bird in the list of bird counts.
    for entry in bird_counts:
        if entry[0] == bird:
            entry[1] = entry[1] + 1
            found = True
    if not found:
        bird_counts.append([bird, 1])  # first time


if __name__ == '__main__':
    observations_file.close()
    for entry in bird_counts:
        print(entry[0], entry[1])
