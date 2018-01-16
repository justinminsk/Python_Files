import urllib3
import sqlite3
import openpyxl


def makeSQL():
    http = urllib3.PoolManager()
    getfile = http.request('GET', 'http://math.mercyhurst.edu/~sousley/STAT_139/data/Pitching.xlsx')
    with open('Pitching.xlsx', 'wb') as output_file:
        output_file.write(bytearray(getfile.data))
    wb = openpyxl.load_workbook('Pitching20.xlsx')

    wbsheet = wb["Pitching"]
    con = sqlite3.connect("baseball.db")
    curs = con.cursor()

    vals = ''
    cv = ''
    for i in range(10001, 44140): # rows - 2 is first record
        for j in range(1,31): # columns
            cv = str(wbsheet.cell(row=i, column=j).value)
            #print(str(i), str(j),cv)
            if cv.strip() != 'None':
                vals = vals + '"' + str(cv) + '",'
            else: vals = vals + 'NULL,'
        # add right paren
        vals = vals + ')'
        print(str(i))
        # this actually does it
        # print ('insert into pitching values (' + vals[0:len(vals)-2] + ')' )
        curs.execute('insert into pitching values (' + vals[0:len(vals)-2] + ')' )
        vals = ''
    con.commit()
    curs.execute('select count(*) from pitching')
    print(curs.fetchall())


def getData():
    dataframe = sqlite3.connect('baseball.db')
    df = dataframe.cursor()
    df.execute('SELECT * FROM pitching WHERE playerID == "ruthba01"')
    for line in df.fetchall():
        print(line)


if __name__ == '__main__':
    getData()
