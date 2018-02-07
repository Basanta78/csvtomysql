import os
import csv
import logging

logging.basicConfig(level=logging.INFO)


class CsvDao:
    """Data access object creating class for csvfile
    """
    @staticmethod
    def get_csv_data(csv_file_path):

        with open(csv_file_path) as csv_file:
            try:
                for row in csv.reader(csv_file):
                    if not row:
                        raise ValueError("Read row error")
                    yield row
            except IOError:
                raise IOError

    @classmethod
    def read_file(cls, file_path):
        if os.path.exists(file_path):
            iter_data = iter(cls.get_csv_data(file_path))
            return iter_data
        else:
            raise Exception("file not found")
