import matplotlib.pyplot as plt


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
