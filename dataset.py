import csv
import matplotlib.pyplot as plt


class DataSet:
    def __init__(self):
        self.__REL_PATH = 'data_TT_TU_MN009'
        self.__file_type = 'csv'

        self.__data = []        # array for the rows of the data table

    def open_file(self):
        self.__data = []
        with open(self.__REL_PATH + '.' + self.__file_type) as data_csv:                             # open the file
            csv_reader_obj = csv.reader(data_csv, delimiter=',')     # create the csv reader object
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


if __name__ == '__main__':
    Data = DataSet()
    Data.open_file()
    complete_file = Data.get_data_set()
    print(complete_file)
    values = [row[3] for row in complete_file]
    ylabel = values[0]
    values = values[1:]

    timesteps = [row[2] for row in complete_file]
    xlabel = timesteps[0]
    timesteps = timesteps[1:]

    start_time = timesteps[0]
    timesteps = [str(int(step) - int(start_time)) for step in timesteps]
    print(timesteps)
    print(values)

    x = [int(step) for step in timesteps]
    y = [float(value) for value in values]

    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()

