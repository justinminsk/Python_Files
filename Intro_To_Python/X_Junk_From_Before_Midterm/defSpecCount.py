def SpecCount():
    species = input('Enter a species name: ')
    pop = input('Enter the number of organisms represented by ' + species + ': ')
    pop = int(pop)
    pop = pop + 10
    print('The population of', species, 'is:', '\n', pop)
    print('The population of', species, 'is:', "\n", "\t", pop)
    print('The population of', species, 'is:', "\t", pop)
    print('The population of', species, 'is:', pop)
