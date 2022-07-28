import connector
import pandas as pd
import lev_dist as levd
import csv

# grab downloaded copy of excel app/dbs - convert to g-sheet connection if reuse is needed
pii = pd.read_excel(r'C:\Users\kmcgilli\Downloads\Inmar Data Classification and Marking Policy.xlsx', sheet_name=None)
sheet_tbls = []
for key, value in pii.items():
    sheet_tbls.append(key)

xlapps = pii['Data Sources by Application']
xldbs = pii['Data Sources by Database']


# grab ED db version of app + dbs
appquery='select appid, applicationname from applications'

dbquery='select a.applicationname, s.servername, d.databaseid, d.databasename, d.istracked \
from applications a \
join databases d on a.appid=d.appid \
join servers s on s.serverid=d.serverid'

mycon = connector.Postgres() 
mycon.dbengine(servername='1.1.1.1',databasename='xx',username='uid',passwrd='pass')
dbdbs = mycon.dbdataframe(dbquery)
dbapps = mycon.dbdataframe(appquery)
mycon.disposengine()

# dbapps['applicationname']
# xlapps['Application']




# app_guess = {}
# for dbapp in dbapps['applicationname']:
#     app_guess[dbapp] = {xlap: levd.lev_dist(dbapp,xlap) for xlap in xlapps['Application']}
#     app_guess[dbapp] = sorted(app_guess[dbapp].items(), key=lambda kv: kv[1])

app_guess = {}
for app in xlapps['Application']:
    app_guess[app] = {xlap: levd.lev_dist(app,xlap) for xlap in dbapps['applicationname']}
    app_guess[app] = sorted(app_guess[app].items(), key=lambda kv: kv[1])

app_guess['YOU Technology'][0][0]

dbappguess = [(app,app_guess[app][0][0]) for app in dbapps['applicationname']]
type(dbappguess)

for x in dbappguess:
    print(x)

with open(r'C:\Users\kmcgilli\Downloads\pii_app_guesses.csv','w', newline='\n') as guesslist:
    o = csv.writer(guesslist, quoting = csv.QUOTE_MINIMAL)
    o.writerow(['DB appname']+['Spreadsheet appname'])
    # for app in dbappguess:
    #     o.writerow(str(app[0]))
    o.writerows(dbappguess)

# joinapps = pd.merge(dbapps,xlapps,
# how='inner',
# left_on='applicationname',
# right_on='Application',
# suffixes=('_db','_xl'))

# joinapps = pd.merge(dbapps,xlapps,
# how='inner',
# left_on='applicationname',
# right_on='Application',
# suffixes=('_db','_xl'))
