# bird_count_ID.py
# Invert the dictionary
# bird, count
bird_to_observations= {'canadagoose': 183, 'long-tailed jaeger': 71,
'snow goose': 63, 'northern fulmar': 1, 'snow goose': 1}
observations_to_birds_list= {}
for bird, observations in bird_to_observations.items():
    if observations in observations_to_birds_list: # count is the index
        observations_to_birds_list[observations].append(bird)
    else:
        observations_to_birds_list[observations] = [bird]
# print(observations_to_birds_list)
# Print the inverted dictionary
observations_sorted= sorted(observations_to_birds_list.keys())

if __name__ == '__main__':
    for observations in observations_sorted:
        print(observations, ':', end=" ")
        for bird in observations_to_birds_list[observations]:
            print(' ', bird, end=" ")
        print()