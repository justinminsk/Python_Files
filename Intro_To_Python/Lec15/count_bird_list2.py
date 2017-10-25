# count_bird_list2.py
observations_file = open('birdlist.txt')
bird_to_observations = {}
for line in observations_file:
    bird = line.strip()
    if bird in bird_to_observations:
        bird_to_observations[bird] = bird_to_observations[bird] + 1
    else:
        bird_to_observations[bird] = 1
observations_file.close()


if __name__ == '__main__':
    # Print each bird and the number of times it was seen.
    for bird, observations in bird_to_observations.items():
        print(bird, observations)
