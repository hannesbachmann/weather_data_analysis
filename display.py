import matplotlib.pyplot as plt
import numpy as np


def plot_hottest_and_coldest_days(hottest_days, coldest_days):
    fig, ax = plt.subplots(2, 1)
    fig.suptitle('hottest and coldest days of each year')
    for day in hottest_days:
        day_temp = [float(col[3]) for col in day[0]]
        day_time = [0.25 * i for i in range(93)]
        ax[0].plot(day_time, day_temp, label=day[0][0][2][0:4])
    ax[0].set_xlabel('time in h')
    ax[0].set_ylabel('temperature in °C')
    ax[0].legend()

    for day in coldest_days:
        day_temp = [float(col[3]) for col in day[0]]
        day_time = [0.25 * i for i in range(len(day[0]))]
        ax[1].plot(day_time, day_temp, label=day[0][0][2][0:4])
    ax[1].set_xlabel('time in h')
    ax[1].set_ylabel('temperature in °C')
    ax[1].legend()
    fig.tight_layout()
    plt.show()


def plot_trend_prediction(x, y, x_unknown, y_unknown, sigma):
    fig = plt.figure(figsize=(6, 3), dpi=100)
    plt.plot(x, y, '-', label='true data')
    plt.plot(x_unknown, np.exp(y_unknown) - 30, 'r-', label='prediction')  # expected future data
    plt.fill_between(x_unknown, np.exp(y_unknown - sigma) - 30, np.exp(y_unknown + sigma) - 30,
                     color='0.85')  # possible space
    plt.xlim(2015, 2021)  # axis limitation
    plt.xticks(np.arange(2015, 2021, 1))  # x axis scale
    plt.ylim(-20, 40)  # axis limitation
    plt.vlines([2020], -20, 40, '0.6', '--')  # dividing line
    plt.title('Temperature-Trend')
    plt.xlabel('time (year)')
    plt.ylabel('temperature in °C')
    fig.tight_layout()
    plt.show()
