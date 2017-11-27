import sqlite3
import openpyxl
wb = openpyxl.load_workbook('Pitching20.xlsx')
wbsheet = wb["Pitching"]
con = sqlite3.connect("baseball.db")
curs = con.cursor()
vals = vals = ''
cv = ''
for i in range(2, 15): # rows - 2 is first record
    for j in range(1,31): # columns
        cv = str(wbsheet.cell(row=i, column=j).value)
        print(str(i), str(j),cv)
        # replace "None" with NULL
        if cv.strip() != 'None':
            vals = vals + '"' + str(cv) + '",'
        else: vals = vals + 'NULL,'
    # add right paren
    vals = vals + ')'
    print ('insert into pitching values (' + vals[0:len(vals)-2] + ')' )
    curs.execute('insert into pitching values (' + vals[0:len(vals)-2] + ')' )
    vals = ''
con.commit()