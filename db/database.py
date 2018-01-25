import logging
import MySQLdb as Db
from .configure import config

logging.basicConfig(level=logging.INFO)


class MySqlConnector:
    """Class to connect and interact with mysql
    """

    def __init__(self):
        """Initialize database
        """

        try:
            self.my_db = Db.connect(**config)
            self.cursor = self.my_db.cursor()
        except Db.Error as err:
            raise Exception(err)

    def get_db_cursor(self):
        return self.cursor

    def get_db_connect_obj(self):
        return self.my_db

            

