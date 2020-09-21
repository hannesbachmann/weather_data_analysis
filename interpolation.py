from scipy.interpolate import CubicSpline
import numpy as np
import scipy.spatial
import math
import matplotlib.pyplot as plt


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


def covFunc(d):
    return 0.8 * np.exp(-np.abs(np.sin(np.pi * d)) / 0.5 - np.abs(d / 25.) ** 2 - 2.5) + \
           (0.2 - 0.01) * np.exp(-(np.abs(np.sin(np.pi * d / 4)) / 0.2)) + 0.01 * np.exp(-np.abs(d / 45.))


def covMat(x1, x2, covFunc, noise=0):
    cov = covFunc(scipy.spatial.distance_matrix(np.atleast_2d(x1).T, np.atleast_2d(x2).T))
    if noise:
        np.fill_diagonal(cov, np.diag(cov) + noise)
    return cov


def gauss_process(complete_data):
    x = np.arange(2015., 2020., 5 / 4383.)
    print(len(x))

    y = []
    full_y = []
    for i in range(len(complete_data)):
        if i % 10 == 0 and complete_data[i][2][0:4] != '2020':
            y.append(float(complete_data[i][3]) + 30)
        elif i % 10 == 0:
            full_y.append(float(complete_data[i][3]))
    print(len(y))

    x_known = x
    y_known = np.log(y)
    x_unknown = np.arange(2020, 2021, 5 / 4383.)  # range der unbekannten
    full_x = np.arange(2020, 2020.152, 5 / 4383.)
    print(len(full_x), len(full_y))

    Ckk = covMat(x_known, x_known, covFunc, noise=0.02)
    Cuu = covMat(x_unknown, x_unknown, covFunc, noise=0.00)
    CkkInv = np.linalg.inv(Ckk)
    Cuk = covMat(x_unknown, x_known, covFunc, noise=0)
    m = np.mean(y_known)
    y_unknown = m + np.dot(np.dot(Cuk, CkkInv), y_known - m)
    sigmaPrior = np.sqrt(np.mean(np.square(y_known)))
    sigma = sigmaPrior * np.sqrt(np.diag(Cuu - np.dot(np.dot(Cuk, CkkInv), Cuk.T)))

    y = [value - 30 for value in y]
    fig = plt.figure(figsize=(6, 3), dpi=100)
    plt.plot(x, y, '-')

    plt.plot(full_x, full_y)
    plt.plot(x_unknown, np.exp(y_unknown) - 30, 'r-')                # expected future data
    plt.fill_between(x_unknown, np.exp(y_unknown - sigma) - 30, np.exp(y_unknown + sigma) - 30, color='0.85')     # possible space
    plt.xlim(2015, 2021)          # axis limitation
    plt.xticks(np.arange(2015, 2021, 2))    # x axis scale
    plt.ylim(-20, 40)                # axis limitation
    plt.vlines([2020], -20, 40, '0.6', '--')      # dividing line
    plt.title('Temperature-Trend')
    plt.xlabel('time (year)')
    plt.ylabel('temperature in °C')
    plt.show()
