import sys
import logging
import MySQLdb as db
from .configure import config

logging.basicConfig(level=logging.INFO)


class MySqlConnector:
    """Class to connect and interact with mysql
    """

    def __init__(self):
        """Initialize database
        """

        try:
            self.mydb = db.connect(**config)
            self.cursor = self.mydb.cursor()  #create cursor
        except db.Error as err:
            logging.error("%d: %s",err.args[0], err.args[1])
            sys.exit(1)
            
    def create_table(self):
        """Create a table named  states
        """

        try:
            self.cursor.execute("create table states (Statename VARCHAR(20),state VARCHAR(20),avr VARCHAR(20))")
        except db.Error as err:
            if err.args[0] == 1050:
                self.cursor.execute("TRUNCATE states") #truncate table
            else:
                logging.error("%d: %s",err.args[0], err.args[1])
                sys.exit(1)

    def request_data(self,sql):
        """Request data from query
        
        Arguments:
            sql {query} -- [sql query to request data]
        """

        self.cursor.execute(sql)
        self.sqlout = self.cursor.fetchall()

    def drop_table(self):
        """Delete tabel
        """

        self.db.execute("drop table states")

    def insert(self,row):
        """Insert row in table
        
        Arguments:
            row {[List]} -- [insert row in states table]
        """

        try:
            self.cursor.execute("INSERT INTO states(Statename, state, avr) VALUES(%s, %s, %s)", row)
            self.mydb.commit()
        except db.Error as e:
            logging.error("%d: %s" % (e.args[0], e.args[1]))

    def close(self):
        """Close table
        """

        self.cursor.close()
