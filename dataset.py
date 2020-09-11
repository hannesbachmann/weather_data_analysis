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


if __name__ == '__main__':
    Data = DataSet()
    Data.open_file()
    complete_file = Data.get_data_set()

    values = [row[3] for row in complete_file]
    ylabel = values[0]
    values = values[1:]

    timesteps = [row[2] for row in complete_file]
    xlabel = timesteps[0]
    timesteps = timesteps[1:]

    minute = [step[10:12] for step in timesteps]
    hour = [step[8:10] for step in timesteps]
    day = [step[6:8] for step in timesteps]
    month = [step[4:6] for step in timesteps]
    year = [step[0:4] for step in timesteps]

    total_minute = 0
    last_min = 0
    for min in hour:
        if int(min) == 0:
            last_min = -1
        total_minute += int(min) - last_min
        last_min = int(min)
    x_minute = np.arange(0, total_minute, 1)

    x = x_minute
    y = [float(value) for value in values]

    cubic_spline = CubicSpline(x, y)
    xs = np.arange(0, total_minute, 0.25)
    spline_arr = cubic_spline(xs)

    spline_index = 0
    finer_complete_file = []
    for row in complete_file[1:]:
        tmp_year = row[2][0:4]
        tmp_month = row[2][4:6]
        tmp_day = row[2][6:8]
        tmp_hour = row[2][8:10]
        tmp_minute = row[2][10:12]
        finer_complete_file.append([row[0], row[1],
                                    str(tmp_year) + str(tmp_month) + str(tmp_day) + str(tmp_hour) + '00',
                                    spline_arr[spline_index], row[4], row[5]])
        spline_index += 1
        finer_complete_file.append([row[0], row[1],
                                    str(tmp_year) + str(tmp_month) + str(tmp_day) + str(tmp_hour) + '15',
                                    spline_arr[spline_index], row[4], row[5]])
        spline_index += 1
        finer_complete_file.append([row[0], row[1],
                                    str(tmp_year) + str(tmp_month) + str(tmp_day) + str(tmp_hour) + '30',
                                    spline_arr[spline_index], row[4], row[5]])
        spline_index += 1
        finer_complete_file.append([row[0], row[1],
                                    str(tmp_year) + str(tmp_month) + str(tmp_day) + str(tmp_hour) + '45',
                                    str(spline_arr[spline_index]), row[4], row[5]])
        spline_index += 1
    timesteps = [float(row[2]) for row in finer_complete_file]
    values = [float(row[3]) for row in finer_complete_file]
    x_spline = np.arange(0, total_minute, 0.01)

    fig, ax = plt.subplots(figsize=(6.5, 4))
    # ax.plot(xs, cubic_spline(xs), 'x', label='Spline 15 Interval')
    ax.plot(xs, values, 'o', label='data')
    ax.plot(x_spline, cubic_spline(x_spline), label='Spline')
    ax.legend(loc='lower left', ncol=1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()
