import os
import csv
import logging

logging.basicConfig(level=logging.INFO)


class CsvDao:
    """Data access object creating class for csvfile
    """

    def __init__(self, file_name):
        """Constructor
        
        Arguments:
            file_name {[string]} -- [name of file]
        """

        self.file_name = file_name

    def get_csv_data(self, csv_fname):
        """Generator for getting csv data
        
        Arguments:
            csv_fname {[string]} -- [csv filename]
        
        Raises:
            ValueError -- [Exception to read row]
        
        Yields:
            [list] -- [generate list of rows]
        """

        with open(csv_fname) as csvfile:
            try:
                for row in csv.reader(csvfile):
                    if not row:
                        raise ValueError("Read row error")
                    yield row
            except IOError:
                raise IOError

    def read_file(self):
        """Read csv file
        
        Returns:
            [list] -- [return list of rows]
        """
        if os.path.exists(self.file_name):
            iter_data = iter(self.get_csv_data(self.file_name))
            return iter_data
        else:
            raise Exception("file not found")
