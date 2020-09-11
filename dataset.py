import csv
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np


class DataSet:
    def __init__(self):
        self.__REL_PATH = 'data_TT_TU_MN009'
        self.__file_type = 'csv'

        self.__data = []  # array for the rows of the data table

    def open_file(self):
        self.__data = []
        with open(self.__REL_PATH + '.' + self.__file_type) as data_csv:  # open the file
            csv_reader_obj = csv.reader(data_csv, delimiter=',')  # create the csv reader object
            for row in csv_reader_obj:
                self.__data.append(row)

    def get_data_set(self):
        return self.__data

    def get_row(self, row_num):
        if row_num != 0:
            return self.__data[row_num]
        else:
            return None

    def get_legend(self):
        return self.__data[0]
