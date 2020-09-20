import matplotlib.pyplot as plt


def plot_hottest_and_coldest_days(hottest_days, coldest_days):
    fig, ax1 = plt.subplots(figsize=(6.5, 4))
    for day in hottest_days:
        day_temp = [float(col[3]) for col in day[0]]
        day_time = [0.25 * i for i in range(93)]
        ax1.plot(day_time, day_temp)
    plt.xlabel('time over one day')
    plt.ylabel('temperature')

    fig, ax2 = plt.subplots(figsize=(6.5, 4))
    for day in coldest_days:
        day_temp = [float(col[3]) for col in day[0]]
        day_time = [0.25 * i for i in range(len(day[0]))]
        ax2.plot(day_time, day_temp)
    plt.xlabel('time over one day')
    plt.ylabel('temperature')
    plt.show()