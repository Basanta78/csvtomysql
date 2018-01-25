import MySQLdb as Db


class MySqlDao:
    """Class to connect and interact with mysql
    """
    def __init__(self, mysql_db, cursor):
        self.cursor = cursor
        self.mysql_db = mysql_db
            
    def create_table(self, table_name):
        """Create a table named  states
        """

        try:
            self.cursor.execute("create table {0} (Statename VARCHAR(20),state VARCHAR(20),avr VARCHAR(20))".format(table_name))
        except Db.OperationalError:
            self.cursor.execute("TRUNCATE {0}".format(table_name))
        except Db.DatabaseError:
            raise Exception("Connection not found")

    def request_data(self, sql):
        """Request data from query
        
        Arguments:
            sql {query} -- [sql query to request data]
        """

        self.cursor.execute(sql)
        sql_out = self.cursor.fetchall()
        return sql_out

    def drop_table(self, table_name):
        """Delete table
        """

        self.cursor.execute("drop table {0}".format(table_name))

    def insert(self, row, table_name):
        """Insert row in table
        
        Arguments:
            row {[List]} -- [insert row in states table]
        """

        try:
            self.cursor.execute("INSERT INTO {0}(Statename, state, avr) VALUES(%s, %s, %s)".format(table_name), row)
            self.mysql_db.commit()
        except Db.Error as e:
            raise Exception(e)

    def close(self):
        """Close table
        """
        self.cursor.close()