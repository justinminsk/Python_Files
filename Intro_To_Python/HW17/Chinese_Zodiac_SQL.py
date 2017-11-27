from sqlite3 import *


def Chinese_Zodiac_SQL():
    dataframe = connect('zodiac.db')
    df = dataframe.cursor()
    '''df.execute('CREATE TABLE Zodiac(Cycle INTERGER, Animal TEXT, Characteristics TEXT)')
    dataframe.commit()
    table = [
        (0, 'Rat', 'Forthright , industrious, sensitive, intellectual, sociable'),
        (1, 'Ox', 'Dependable , methodical , modest , born leader, patient'),
        (2, 'Tiger', 'Unpredictable , rebellious, passionate, daring, impulsive'),
        (3, 'Rabbit', 'Good friend, kind, soft-spoken , cautious , artistic'),
        (4, 'Dragon', 'Strong, self-assured, proud, decisive, loyal'),
        (5, 'Snake', 'Deep thinker, creative, responsible, calm, purposeful'),
        (6, 'Horse', 'Cheerful, quick-witted, perceptive, talkative, open-minded'),
        (7, 'Goat', 'Sincere, sympathetic, shy, generous, mothering'),
        (8, 'Monkey', 'Motivator, inquisitive, flexible, innovative, problem solver'),
        (9, 'Rooster', 'Organized, self-assured, decisive, perfectionist, zealous'),
        (10, 'Dog', 'Honest , unpretentious, idealistic, moralistic, easy going'),
        (11, 'Pig', 'Peace-loving, hard-working , trusting, understanding, thoughtful'),
    ]
    for line in table:
        df.execute('INSERT INTO Zodiac VALUES (?, ?, ?)', line)
    dataframe.commit()'''

    terminate = False

    # program greeting
    print('This program will display your Chinese zodiac sign and associated')
    print('personal characteristics . \n')

    # get current year from module datetime
    current_yr = datetime.date.today().year

    while not terminate:
        # get year of birth
        birth_year = int(input('Enter your year of birth (yyyy) :'))

        # trap birth year errors - notice I can comment to the far left but it hurts the readability
        while birth_year < 1900 or birth_year > current_yr:
            print('Invalid year . Please re- enter\n')
            birth_year = int(input('Enter your year of birth (yyyy) :'))

        # get index of animal based on birth year
        cycle_num = (birth_year - 1900) % 12
        cycle = (cycle_num,)
        # output results
        df.execute('SELECT Animal FROM Zodiac WHERE Cycle =?', cycle)
        data = df.fetchone()
        print('Your Chinese zodiac sign is the', data[0], '\n')
        print('Your personal characteristics ...')
        df.execute('SELECT Characteristics FROM Zodiac WHERE Cycle =?', cycle)
        data = df.fetchone()
        print(data[0])

        # continue? / classify another birth year?
        response = input('\nWould you like to enter another year? (y/n) :')
        while response != 'y' and response != 'n':
            response = input("Please enter'y'or'n': ")
        if response == 'n':
            terminate = True


if __name__ == '__main__':
    Chinese_Zodiac_SQL()
