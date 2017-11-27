from sqlite3 import *


def make_database():
    dataframe = connect('census.db')
    return dataframe


def make_db_table():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('CREATE TABLE Density(Province TEXT, Population INTEGER, Area REAL)')
    dataframe.commit()
    return df


def add_entries():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('CREATE TABLE Density(Province TEXT, Population INTEGER, Area REAL)')
    dataframe.commit()
    table = [
        ('Newfoundland and Labrador', 512930, 370501.69),
        ('Prince Edward Island', 135294, 5684.39),
        ('Nova Scotia', 908007, 52917.43),
        ('New Brunswick', 729498, 71355.67),
        ('Quebec', 7237479, 1357743.08),
        ('Ontario', 11410046, 907655.59),
        ('Manitoba', 1119583, 551937.87),
        ('Saskatchewan', 978933, 586561.35),
        ('Alberta', 2974807, 639987.12),
        ('British Columbia', 3907738, 926492.48),
        ('Yukon Territory', 28674, 474706.97),
        ('Northwest Territories', 37360, 1141108.37),
        ('Nunavut', 26745, 1925460.18),
    ]
    for line in table:
        df.execute('INSERT INTO Density VALUES (?, ?, ?)', line)
    dataframe.commit()



def get_content():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('CREATE TABLE Density(Province TEXT, Population INTEGER, Area REAL)')
    dataframe.commit()
    table = [
        ('Newfoundland and Labrador', 512930, 370501.69),
        ('Prince Edward Island', 135294, 5684.39),
        ('Nova Scotia', 908007, 52917.43),
        ('New Brunswick', 729498, 71355.67),
        ('Quebec', 7237479, 1357743.08),
        ('Ontario', 11410046, 907655.59),
        ('Manitoba', 1119583, 551937.87),
        ('Saskatchewan', 978933, 586561.35),
        ('Alberta', 2974807, 639987.12),
        ('British Columbia', 3907738, 926492.48),
        ('Yukon Territory', 28674, 474706.97),
        ('Northwest Territories', 37360, 1141108.37),
        ('Nunavut', 26745, 1925460.18),
    ]
    for line in table:
        df.execute('INSERT INTO Density VALUES (?, ?, ?)', line)
    dataframe.commit()
    df.execute('SELECT * FROM Density')
    for line in df.fetchall():
        print(line)


def get_pop():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('SELECT Population FROM Density')
    for line in df.fetchall():
        print(line)


def get_prov_lt10mill():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('SELECT Province FROM Density WHERE Population < 1000000')
    for line in df.fetchall():
        print(line)


def get_prov_lt10mill_gt5mill():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('SELECT Province FROM Density WHERE (Population < 1000000 or Population > 5000000)')
    for line in df.fetchall():
        print(line)


def get_prov_nlt10mill_ngt5mill():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('SELECT Province FROM Density WHERE NOT(Population < 1000000 or Population > 5000000)')
    for line in df.fetchall():
        print(line)


def get_prov_landgt200th():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('SELECT Province FROM Density WHERE Area > 200000')
    for line in df.fetchall():
        print(line)


def get_popden():
    dataframe = connect('census.db')
    df = dataframe.cursor()
    df.execute('SELECT Province, Population / Area FROM Density')
    for line in df.fetchall():
        print(line)


if __name__ == '__main__':
    get_popden()
