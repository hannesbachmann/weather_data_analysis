from scipy.interpolate import CubicSpline
import numpy as np
from dataset import Data


def perform_interpolation(complete_data):
    values = [row[3] for row in complete_data]
    ylabel = values[0]
    values = values[1:]

    timesteps = [row[2] for row in complete_data]
    xlabel = timesteps[0]
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

