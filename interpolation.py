from scipy.interpolate import CubicSpline
import numpy as np


def perform_interpolation(complete_data):
    values = [row[3] for row in complete_data]
    values = values[1:]

    timesteps = [row[2] for row in complete_data]
    timesteps = timesteps[1:]

    hour = [step[8:10] for step in timesteps]
    total_hour = 0
    last_hour = 0
    for h in hour:
        if int(h) == 0:
            last_hour = -1
        total_hour += int(h) - last_hour
        last_hour = int(h)
    x_hour = np.arange(0, total_hour, 1)
    y = [float(value) for value in values]

    cubic_spline = CubicSpline(x_hour, y)
    xs = np.arange(0, total_hour, 0.25)
    spline_arr = cubic_spline(xs)

    spline_index = 0
    finer_complete_file = []
    for row in complete_data[1:]:
        tmp_year = row[2][0:4]
        tmp_month = row[2][4:6]
        tmp_day = row[2][6:8]
        tmp_hour = row[2][8:10]
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
    return finer_complete_file

