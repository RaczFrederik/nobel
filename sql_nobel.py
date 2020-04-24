# év;    típus;    keresztnév;    vezetéknév
# 0        1           2              3
# 2017    fizikai     Rainer         Weiss
import sqlite3, pprint
con = sqlite3.connect('nobel.db')
c   = con.cursor()

c.execute("DROP TABLE IF EXISTS tabla")
c.execute('''
        CREATE TABLE IF NOT EXISTS tabla
        (év INTEGER,
        típus TEXT,
        keresztnév TEXT,
        vezetéknév TEXT)
        ''')
con.commit()

with open ('nobel.csv','r', encoding='UTF-8-sig') as f:
    fejlec = f.readline()
#    matrix = [sor.strip().split(';') for sor in f]
    for sor in f:
        év, típus, keresztnév, vezetéknév = sor.strip().split(';')
        c.execute("INSERT INTO tabla VALUES(?,?,?,?)",(év,típus,keresztnév,vezetéknév))
con.commit()

#3.fel. Arthur B mcdonald milyen díjat kapott?
c.execute("SELECT típus FROM tabla WHERE keresztnév LIKE 'Arthur B.' AND vezetéknév LIKE 'McDonald'")   # LIKE olyan az sql ben mint az == és stringeknél használjuk.
típus = c.fetchall()[0][0]
#    if sor[2] == 'Arthur B.' and sor[3] == 'McDonald':
print(f'3.feladat: {típus}')

#4.fel.
c.execute("SELECT keresztnév,vezetéknév FROM tabla WHERE év == 2017 AND típus LIKE 'irodalmi'")   # LIKE olyan az sql ben mint az == és stringeknél használjuk.
keresztnév,vezetéknév = c.fetchall()[0]
print(f'4 feladat: {keresztnév} {vezetéknév}')

#5.fel mely szervezeteek kaptak béke nobeldijat 1990 től.
c.execute("SELECT év,keresztnév FROM tabla WHERE év > 1989 AND típus LIKE 'béke' AND vezetéknév LIKE''")   # LIKE olyan az sql ben mint az == és stringeknél használjuk.
adat = c.fetchall()
for év,szervezet in adat:
    print(f' {év} {szervezet}')


#6. feladat
print(    f'6. feladat:')
c.execute("SELECT év,keresztnév,vezetéknév,típus FROM tabla WHERE vezetéknév LIKE '%Curie%'")   # LIKE olyan az sql ben mint az == és stringeknél használjuk.
adat = c.fetchall()
for év,keresztnév,vezetéknév,típus in adat:
    print(    f'        {év} {keresztnév} {vezetéknév} {típus}')

#7.fel
c.execute("SELECT típus,COUNT(típus) FROM tabla GROUP BY típus")   # LIKE olyan az sql ben mint az == és stringeknél használjuk.
adat = c.fetchall()
for típus,darab in adat:
    print(  f'       {típus:22} {darab:3} db ')
#8 fel.
print(        f'8. feladat: orvosi.txt')
c.execute("SELECT év,keresztnév,vezetéknév FROM tabla WHERE típus LIKE 'orvosi' ORDER BY év ASC")   # LIKE olyan az sql ben mint az == és stringeknél használjuk.
adat = c.fetchall()
with open ('orvosi.txt','w', encoding='UTF-8') as f:
    for év,keresztnév,vezetéknév in adat:
        print(f'{év}:{keresztnév} {vezetéknév}',file=f)

con.commit()
con.close