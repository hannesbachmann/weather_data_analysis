import display
from interpolation import perform_interpolation
from dataset import DataSet, TempData
from temperature_analysis import Temperature


def run():
    Dataset = DataSet()
    Temp = Temperature()
    Tempdata = TempData()

    Dataset.open_file()
    complete_file = Dataset.get_data_set()
    finer_file = perform_interpolation(complete_file)

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
    print(hottest_temp_year)


if __name__ == '__main__':
    run()