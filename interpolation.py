from scipy.interpolate import CubicSpline
import numpy as np
import scipy.spatial


def perform_interpolation(complete_data):
    """
    perform interpolation calculation on the complete data
    convert the time steps into 15 minutes interval

    :param complete_data: {array-like}, shape = [rows]
            rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                        quality_byte]
                product_code: string
                SDO_ID: string
                time_stamp: string, time in 'yyyymmddhhmm'
                temperature: string, can be converted to float value
                quality_niveau: string
                quality_byte: string
    :return finer_complete_file: {array-like}, shape = [rows]
            rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                        quality_byte]
                product_code: string
                SDO_ID: string
                time_stamp: string, time in 'yyyymmddhhmm'
                temperature: string, can be converted to float value
                quality_niveau: string
                quality_byte: string
    """
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


def cov_func(d):
    """
    calculating covFunc needed for gauss process

    :param d:
    :return calculation_result:
    """
    return 0.8 * np.exp(-np.abs(np.sin(np.pi * d)) / 0.5 - np.abs(d / 25.) ** 2 - 2.5) + \
           (0.2 - 0.01) * np.exp(-(np.abs(np.sin(np.pi * d / 4)) / 0.2)) + 0.01 * np.exp(-np.abs(d / 45.))


def cov_mat(x1, x2, cov_func, noise=0.0):
    """
    calculating covMat needed for gauss process

    :param x1: x_known/x_unknown, list for data set
    :param x2: x_known/x_unknown, list for data set
    :param cov_func: function, calculating covFunc needed for gauss process
    :param noise: float, default=0
    :return cov: list, calculated result cov_func with diagonal noise
    """
    cov = cov_func(scipy.spatial.distance_matrix(np.atleast_2d(x1).T, np.atleast_2d(x2).T))
    if noise:
        np.fill_diagonal(cov, np.diag(cov) + noise)
    return cov


def gauss_process(complete_data):
    """
    perform the gauss process trend calculation to predict the future

    :param complete_data: {array-like}, shape = [rows]
            rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                        quality_byte]
                product_code: string
                SDO_ID: string
                time_stamp: string, time in 'yyyymmddhhmm'
                temperature: string, can be converted to float value
                quality_niveau: string
                quality_byte: string
    :return [x, y, x_unknown, y_unknown, sigma]: {array-like}
        x: {array-like}, shape = [time_stamps]
            time_stamps: float, represents time
        y: {array-like}, shape = [temperature_values]
            temperature_values: float, represents temperature in °C
        x_unknown: {array-like}, shape = [time_stamps]
            time_stamps: float, represents time after known time
        y_unknown: {array-like}, shape = [temperature_values]
            temperature_values: float, represents temperature in °C
        sigma: {array-like}, shape = [values]
            values: float, variable for possible inaccuracy in the future trend
    """
    x = np.arange(2015., 2020., 5 / 4383.)

    y = []
    for i in range(len(complete_data)):
        if i % 10 == 0 and complete_data[i][2][0:4] != '2020':
            y.append(float(complete_data[i][3]) + 30)

    x_known = x
    y_known = np.log(y)
    x_unknown = np.arange(2020, 2021, 5 / 4383.)  # range der unbekannten

    Ckk = cov_mat(x_known, x_known, cov_func, noise=0.02)
    Cuu = cov_mat(x_unknown, x_unknown, cov_func, noise=0.00)
    CkkInv = np.linalg.inv(Ckk)
    Cuk = cov_mat(x_unknown, x_known, cov_func, noise=0)
    m = np.mean(y_known)
    y_unknown = m + np.dot(np.dot(Cuk, CkkInv), y_known - m)
    sigmaPrior = np.sqrt(np.mean(np.square(y_known)))
    sigma = sigmaPrior * np.sqrt(np.diag(Cuu - np.dot(np.dot(Cuk, CkkInv), Cuk.T)))
    y = [value - 30 for value in y]

    return [x, y, x_unknown, y_unknown, sigma]



