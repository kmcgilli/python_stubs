from abc import ABC, abstractmethod
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

class DbConnection (ABC):

    # def __init__(self, config:dict):
    #     self.dbconfig = config

    @abstractmethod
    def dbconnect(self):
        pass

    def dbdictcursor(self):
        return self.cur
        
    

class Postgres(DbConnection):
    import psycopg2
    import psycopg2.extras
    from psycopg2 import OperationalError, errorcodes, errors
    
    def dbconnect(self,servername, databasename, username, passwrd):
        try:
            db_conn = self.psycopg2.connect(host=servername, database=databasename, user=username, password=passwrd)
            self.db_conn = db_conn
            return(db_conn)
        except self.OperationalError as err:
            msg = "Error {} connecting to database {}:{}.{}".format(err,username,servername,databasename)
            return(msg)

    def dbdictcursor(self,query):
        try:
            cur = self.db_conn.cursor(cursor_factory=self.psycopg2.extras.DictCursor)
            cur.execute(query)
            return(cur)
        except Exception as err:
            return(err)

    def dbengine(self,servername, databasename, username, passwrd):
        try:
            engine = create_engine("postgresql://"+str(username)+":"+str(passwrd)+"@"+str(servername)+"/"+str(databasename))
            self.engine = engine
            eng_conn = engine.connect()
            self.eng_conn = eng_conn
        except Exception as err:
            return(err)

    def dbdataframe(self, query):
        try:
            dfresult = pd.read_sql_query(query, con = self.eng_conn)
            return(dfresult)
        except Exception as err:
            return(err)

    def closedbconn(self):
        try:
            self.db_conn.close()
        except Exception as err:
            return(err)

    def disposengine(self):
        try:
            self.engine.dispose()
        except Exception as err:
            return(err)
