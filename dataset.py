import csv


class DataSet:
    def __init__(self):
        self.__REL_PATH = 'data_TT_TU_MN009.csv'
        self.__file_type = 'csv'

        self.__csv_reader_obj = None        # represents the data inside the csv

    def open_file(self):
        with open(self.__REL_PATH) as data_csv:                             # open the file
            self.__csv_reader_obj = csv.reader(data_csv, delimiter=',')     # create the csv reader object

    def get_data_set(self):
        pass

