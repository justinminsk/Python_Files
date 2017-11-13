# How to run the code

To run the code you should use anaconda3 or jupyter notebook with python 3. You will also need numpy, pandas, matplotlib, seaborn, and pylab libraries for python.

# A Look at Pokemon by Generation

Pokemon became a sensation in the 1990's and continues to be a popular franchise to this date.
Pokemon the video game has evolved (pun intended) over the decades into a complex game that takes
a lot of statistics and analyze to create teams that can win the meta at tournaments. The point
of this kernal is to look at the Pokemon by generation and see if we can find any insight into
the numbers behind the design.

# An Example of a Pokemon

This is Pickachu the franchises mascot.

![alt text](https://cdn.bulbagarden.net/upload/2/28/Spr_6o_025_C.png)

This is Pickachu in our data.


    pokemon.iloc[30]


#25

Name           Pikachu

Type 1        Electric

Type 2             NaN

Total              320

HP                  35

Attack              55

Defense             40

Sp. Atk             50

Sp. Def             50

Speed               90

Generation           1

Legendary        False

Name: 30, dtype: object


# A Look at Every Generation

Looking at all the generations at once we can create a control that we can compare to the
other datasets. Here we make a Pearson correlation chart to see the correlations and create
a histogram for each variable to see distribution and other useful information.

To start looking at the data first you need to upload libraries.


    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    #import libraries


Then import the data.


    pokemon = pd.read_csv('Pokemon.csv')
    #import data


Now we can graph the data.


    #Looking at the breakdown of type 1
    type_count = pd.value_counts(pokemon['Type 1'], sort = True).sort_index()
    labels = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fariy', 'Fighting', 'Fire',
            'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
            'Rock', 'Steel', 'Water']
    sizes = type_count

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of Pokemon by type 1')
    #plt.savefig('pie1.png', bbox_inches='tight')
    plt.show()



    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data', y = 1.05, size = 15)
    sns.heatmap(pokemon.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    sns.plt.show()
    #color map looking at Pearson correlations


As we can see sp. def and defense as well as sp. attack and sp. def have some of
the strongest correlations.


    pokemon.hist()
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.show()
    #histograms of the different stats to show if they have normal distribution


Attack, Defense, HP, Sp. Atk, Sp. Def, and Speed have decent distributions.

# Generation 1


    df1 = pokemon[pokemon.Generation == 1]
    #look at just first generation pokemon

    #Looking at the breakdown of type 1
    type_count = pd.value_counts(df1['Type 1'], sort = True).sort_index()
    #print(type_count)
    labels = ['Bug', 'Dragon', 'Electric', 'Fariy', 'Fighting', 'Fire',
            'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
            'Rock',  'Water']
    sizes = type_count

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of Pokemon by type 1')
    #plt.savefig('pie2.png', bbox_inches='tight')
    plt.show()


    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data', y = 1.05, size = 15)
    sns.heatmap(df1.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    plt.savefig('heat2.png', bbox_inches='tight')
    sns.plt.show()
    #color map looking at Pearson correlations


Here we can see that sp. attack and sp. def have the highest correlation, even higher then our control. This means in gen one sp. attack and sp. def tended to go hand in hand.


    df1.hist()
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.savefig('hist2.png', bbox_inches='tight')
    plt.show()
    #histograms of the different stats to show if they have normal distribution


Attack, Defense, HP, Sp. Atk, and Speed have decent distributions.

# Generation 2

    df1 = pokemon[pokemon.Generation == 2]
    #look at gen 2 pokemon

    #Looking at the breakdown of type 1
    type_count = pd.value_counts(df1['Type 1'], sort = True).sort_index()
    #print(type_count)
    labels = ['Bug', 'Dark', 'Electric', 'Fariy', 'Fighting', 'Fire',
             'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
            'Rock', 'Steel', 'Water']
    sizes = type_count

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of Pokemon by type 1')
    #plt.savefig('pie3.png', bbox_inches='tight')
    plt.show()
 

    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data', y = 1.05, size = 15)
    sns.heatmap(df1.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    plt.savefig('heat3.png', bbox_inches='tight')
    sns.plt.show()
    #color map looking at Pearson correlations



In gen two it seems that the two def stats (sp. def and defense) correlate best, but we see that sp. def and sp. attack correlation almost completely drops off compared to our control and gen one.
The other new trend is between attack and defense which have a strong correlation compared to the rest of the stats.

    df1.hist()
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.savefig('hist3.png', bbox_inches='tight')
    plt.show()
    #histograms of the different stats to show if they have normal distribution


This generation does not have normal distributions.

# Generation 3


    df1 = pokemon[pokemon.Generation == 3]
    #look at gen 3 pokemon

    #Looking at the breakdown of type 1
    type_count = pd.value_counts(df1['Type 1'], sort = True).sort_index()
    #print(type_count)
    labels = ['Bug', 'Dark',  'Electric', 'Fariy', 'Fighting', 'Fire',
            'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
            'Rock', 'Steel', 'Water']
    sizes = type_count

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of Pokemon by type 1')
    #plt.savefig('pie4.png', bbox_inches='tight')
    plt.show()

    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data', y = 1.05, size = 15)
    sns.heatmap(df1.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    plt.savefig('heat4.png', bbox_inches='tight')
    sns.plt.show()
    #color map looking at Pearson correlations


This gen (gen three) has a crazy high correlation between sp. atk and attack. Speed and sp atk also have high correlation which is a new correlation. This could be a generation that you would leave out for trying to predict type off of stats. The trend with the defenses (sp. def and defense) contiue also.


    df1.hist()
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.savefig('hist4.png', bbox_inches='tight')
    plt.show()
    #histograms of the different stats to show if they have normal distribution


# Generation 4

    df1 = pokemon[pokemon.Generation == 4]
    #look at gen 4 pokemon


    #Looking at the breakdown of type 1
    type_count = pd.value_counts(df1['Type 1'], sort = True).sort_index()
    #print(type_count)
    labels = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fariy', 'Fighting', 'Fire',
            'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
            'Rock', 'Steel', 'Water']
    sizes = type_count

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of Pokemon by type 1')
    #plt.savefig('pie5.png', bbox_inches='tight')
    plt.show()



    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data', y = 1.05, size = 15)
    sns.heatmap(df1.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    plt.savefig('heat5.png', bbox_inches='tight')
    sns.plt.show()
    #color map looking at Pearson correlations



Here we have the correlation out of all the gens. At a 71% correlation defense and sp. def in this generation should be the same or close to the same number. Here we also see a correlation between hp and attack which is a different trend compared to other gens.


    df1.hist()
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.savefig('hist5.png', bbox_inches='tight')
    plt.show()
    #histograms of the different stats to show if they have normal distribution


Attack has decent distribution.

# Generation 5

    df1 = pokemon[pokemon.Generation == 5]
    #look at gen 5 pokemon

    #Looking at the breakdown of type 1
    type_count = pd.value_counts(df1['Type 1'], sort = True).sort_index()
    #print(type_count)
    labels = ['Bug', 'Dark', 'Dragon', 'Electric',  'Fighting', 'Fire',
            'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
            'Rock', 'Steel', 'Water']
    sizes = type_count

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of Pokemon by type 1')
    #plt.savefig('pie6.png', bbox_inches='tight')
    plt.show()

    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data', y = 1.05, size = 15)
    sns.heatmap(df1.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    plt.savefig('heat6.png', bbox_inches='tight')
    sns.plt.show()
    #color map looking at Pearson correlations


This generation we see a come back of sp. atk and sp. def correlation, we also still have an unsually high correlation of sp. def and defense. The trend form last gen (gen 4) of attack and hp contiues as well.


    df1.hist()
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.savefig('hist6.png', bbox_inches='tight')
    plt.show()
    #histograms of the different stats to show if they have normal distribution


Attack and HP have decent distributions.

# Generation 6

    df1 = pokemon[pokemon.Generation == 6]
    #look at gen 6 pokemon


    #Looking at the breakdown of type 1
    type_count = pd.value_counts(df1['Type 1'], sort = True).sort_index()
    #print(type_count)
    labels = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fariy', 'Fighting', 'Fire',
            'Flying', 'Ghost', 'Grass',  'Ice', 'Normal', 'Poison', 'Psychic',
            'Rock', 'Steel', 'Water']
    sizes = type_count

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of Pokemon by type 1')
    #plt.savefig('pie7.png', bbox_inches='tight')
    plt.show()



    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data', y = 1.05, size = 15)
    sns.heatmap(df1.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    plt.savefig('heat7.png', bbox_inches='tight')
    sns.plt.show()
    #color map looking at Pearson correlations




The trends in gen 6 are speed and sp atk, sp. def, and sp. atk, attack and sp atk, and attack and hp.


    df1.hist()
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.savefig('hist7.png', bbox_inches='tight')
    plt.show()
    #histograms of the different stats to show if they have normal distribution


Attack, Defense, and HP have decent distributions.

# Conclusion

Each gen has its' own unique correlations and trends. This means that if you want to find a strong tank Pokemon (high hp, sp. def, defence) you might look at gen 4 with a 71% correlation between sp. def and defence. The next varible to look at would be legendary which might skew the data.

# Looking at Pokemon without Legendaries

    df1 = pokemon['Legendary'].map(lambda x: x == 0)
    df1 = pokemon[df1]
    #get the data without legendaries

    #Looking at the breakdown of type 1
    type_count = pd.value_counts(df1['Type 1'], sort = True).sort_index()
    labels = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fariy', 'Fighting', 'Fire',
            'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
            'Rock', 'Steel', 'Water']
    sizes = type_count

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of Pokemon by type 1')
    #plt.savefig('pie8.png', bbox_inches='tight')
    plt.show()


    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data without legendaries', y = 1.05, size = 15)
    sns.heatmap(df1.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    plt.savefig('heat8.png', bbox_inches='tight')
    sns.plt.show()
    #color map looking at Pearson correlations
    colormap = plt.cm.plasma
    plt.figure(figsize=(16,12))
    plt.title('Pearson correlation of data with legendaries', y = 1.05, size = 15)
    sns.heatmap(pokemon.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='black', annot=True)
    sns.plt.show()
    #color map looking at Pearson correlations



## Histograms of data without legendaries

    df1.hist()
    fig=plt.gcf()
    fig.set_size_inches(20,15)
    plt.savefig('hist8.png', bbox_inches='tight')
    plt.show()
    #histograms of the different stats to show if they have normal distribution


# Final Observation

Removing Legendries lowers a lot of our correlations and makes our distribution less normal. I think leaving legendries in will improve your chances of being able to predict type by stats.

### Author

Justin Minsk - justin.minsk@gmail.com
