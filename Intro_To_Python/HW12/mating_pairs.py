def mating_pairs(males, females):
    pairs = set()  # create a empty set named pairs
    while males.difference(females) != set():  # while either list is not empty
        hold = males.pop()  # save males pop
        hold2 = females.pop()  # save female pop
        pairs.add((hold, hold2),)  # add then into pairs as a set
    print(pairs)  # print pairs
    return pairs  # return pairs


if __name__ == '__main__':
    mating_males = {'male1', 'male2', 'male3'}
    mating_females = {'female1', 'female2', 'female3'}
    mating_pairs(mating_males, mating_females)
    mating_males = {1, 2, 3}
    mating_females = {11, 22, 33}
    mating_pairs(mating_males, mating_females)