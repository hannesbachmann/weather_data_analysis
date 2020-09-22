from interpolation import perform_interpolation, gauss_process
from dataset import DataSet, TempData
from temperature_analysis import Temperature
from display import plot_hottest_and_coldest_days, plot_trend_prediction, show


def run():
    """
    complete assembled workflow
    - > open and store data set
    - > perform interpolation on data set
    - > find coldest/hottest temperatures of each year
    - > find coldest/hottest days of each year
    - > store the coldest/hottest temperatures of each year
    - > plot coldest/hottest days
    - > perform gauss process future prediction
    - > plot future prediction
    """
    Dataset = DataSet()
    Temp = Temperature()
    Tempdata = TempData()

    Dataset.open_file()
    complete_file = Dataset.get_data_set()
    finer_file = perform_interpolation(complete_data=complete_file)

    years = Temp.separate_into_years(finer_file)
    hottest_days = []
    coldest_days = []
    for year in years:
        Temp.find_coldest_temp_in_year(year)
        Temp.find_hottest_temp_in_year(year)
        days = Temp.separate_into_days(year)
        hottest_days.append(Temp.find_hottest_day(days))
        coldest_days.append(Temp.find_coldest_day(days))
    hottest_temp_year = Temp.get_hottest_temp_each_year()
    coldest_temp_year = Temp.get_coldest_temp_each_year()
    legend = Dataset.get_legend()
    Tempdata.store_extrema(legend, hottest_temp_year, coldest_temp_year)
    plot_hottest_and_coldest_days(hottest_days, coldest_days)

    x, y, x_unknown, y_unknown, sigma = gauss_process(complete_file[1:])
    plot_trend_prediction(x, y, x_unknown, y_unknown, sigma)
    show()


if __name__ == '__main__':
    run()
