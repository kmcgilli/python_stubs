import connector
import pandas as pd

servers_query = "select serverid, servername from servers as s join platform as p on p.platformid = s.platformid where platformabbr = 'BQ'"
mycon = connector.Postgres() 

mycon.dbconnect(servername='1.2.3.4',databasename='db',username='uid',passwrd='pw')
mycur = mycon.dbdictcursor(servers_query) 
servers = mycur.fetchall()
servers[0:10]
mycon.closedbconn()

mycon.dbengine(servername='10.190.28.11',databasename='enterprise_datums',username='svc_dg',passwrd='DrozifA+imoVas3pHlsp')
dfservers = mycon.dbdataframe(servers_query)
dfservers.head()
mycon.disposengine()
