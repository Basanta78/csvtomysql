import logging
from db.database import MySqlConnector
from services.csvdao import CsvDao
from dao.mysqldb import MySqlDao


def main():
    global my_db_cursor
    try:
        my_db = MySqlConnector()
        my_db_obj = my_db.get_db_connect_obj()
        my_db_cursor = my_db.get_db_cursor()
        sql_db = MySqlDao(my_db_obj, my_db_cursor)
        sql_db.create_table('states')
        csv_dao = CsvDao('us_states.csv')
        read_csv = csv_dao.read_file('us_states.csv')
        for row in read_csv:
            sql_db.insert(row, 'states')
        # sql_db.close()

    except Exception as e:
        logging.error(e)
    finally:
        my_db_cursor.close()


if __name__ == '__main__':
    main()
