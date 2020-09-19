import csv


class DataSet:
    def __init__(self):
        self.__REL_PATH = 'data_TT_TU_MN009'
        self.__file_type = 'csv'

        self.__data = []  # array for the rows and cols of the data table

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


class TempData:
    def __init__(self):
        self.__rel_path = 'hottest_coldest'
        self.__file_type = 'csv'

    def store_extrema(self, legend, hottest, coldest):
        with open(self.__rel_path + self.__file_type, 'w', newline='') as csv_hottest:
            csv_writer = csv.writer(csv_hottest, delimiter=',')
            csv_writer.writerow(legend)
            for hot_row in hottest:
                csv_writer.writerow(hot_row)
            for cold_row in coldest:
                csv_writer.writerow(cold_row)
