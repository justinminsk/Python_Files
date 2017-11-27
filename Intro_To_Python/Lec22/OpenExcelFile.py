import urllib3
import openpyxl
import sqlite3


http = urllib3.PoolManager()
getfile = http.request('GET', 'http://math.mercyhurst.edu/~sousley/STAT_139/data/Pitching20.xlsx')
with open('Pitching20.xlsx', 'wb') as output_file:
    output_file.write(bytearray(getfile.data))
wb = openpyxl.load_workbook('Pitching20.xlsx')
sheet = wb.get_active_sheet()
wbsheet = wb["Pitching"]
con = sqlite3.connect("baseball.db")
curs = con.cursor()
bbsql = "CREATE TABLE pitching(playerID TEXT, yearID INTEGER, stint INTEGER, teamID TEXT, lgID TEXT,W INTEGER," \
       " L INTEGER, G INTEGER, GS INTEGER, CG INTEGER,SHO INTEGER, SV INTEGER, IPouts INTEGER,H INTEGER, ER INTEGER," \
       " HR INTEGER, BB INTEGER, SO INTEGER, BAOpp INTEGER,ERA REAL, IBB REAL, WP INTEGER, HBP INTEGER, BK INTEGER, " \
       "BFP INTEGER, GF INTEGER, R INTEGER, SH INTEGER,SF INTEGER, GIDP INTEGER );"
curs.execute(bbsql)
curs.execute('insert into pitching values("aardsda01","2015",1,"ATL","NL",1,1,33,0,0,0,0,92,25,16,6,14,35,0.221,4.7,3,'
             '1,1,0,129,9,17,0,1,NULL)')
con.commit()


if __name__ == '__main__':
    print(wb.get_sheet_names())
    print(wbsheet['A1'].value)
    for i in range(1, 31):
        print(i, wbsheet.cell(row=1, column=i).value)
    curs.execute('select * from pitching')
