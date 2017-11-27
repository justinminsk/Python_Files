import sqlite3
import openpyxl
wb = openpyxl.load_workbook('Pitching20.xlsx')
wbsheet = wb["Pitching"]
vals = ''
cv = ''
for i in range(2, 11): # rows - 2 is first record
    for j in range(1,31): # columns
        cv = str(wbsheet.cell(row=i, column=j).value)
        print(str(i), str(j),cv)
        if cv.strip() != 'None':
            vals = vals + '"' + str(cv) + '",'
        else: vals = vals + 'NULL,'
    # add right paren
    vals = vals + ')'
    # replace "None" with NULL
    # vals.replace('None','NULL')
    # print(vals)
    # replace last comma - but does not work!
    vals.replace(',)',')')
    print('insert into pitching values (' + vals)
    print('insert into pitching values (' + vals[0:len(vals)-2] + ')' ) # a workaround. a kludge?
    vals = ''