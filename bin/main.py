import os
import csv
import sys
import MySQLdb as db
from db.database import MySqlConnector
from services.csvdao import CsvDao

def main():
    mydb = MySqlConnector()
    mydb.create_table()
    csvdao = CsvDao('us_states.csv')
    readcsv = csvdao.read_file()
    for row in readcsv:
        mydb.insert(row)

   
if __name__ == '__main__':
    main()
