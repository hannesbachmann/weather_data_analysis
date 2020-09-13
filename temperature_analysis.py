from dataset import DataSet


class Temperature:
    def __init__(self):
        self.__coldest_row = None
        self.__hottest_row = None

        self.__hottest_day = None
        self.__coldest_day = None

    def get_hottest_row(self):
        return self.__hottest_row

    def get_coldest_row(self):
        return self.__coldest_row

    def get_hottest_day(self):
        return self.__hottest_day

    def get_coldest_day(self):
        return self.__coldest_day

    def find_coldest_temp_in_row(self, complete_data):
        coldest_temp = float(complete_data[1][3])
        self.__coldest_row = [complete_data[1]]
        for row in complete_data[1:]:
            if float(row[3]) < coldest_temp:
                coldest_temp = float(row[3])
                self.__coldest_row = [row]
            elif float(row[3]) == coldest_temp:
                self.__coldest_row.append(row)
        print(f"coldest temp: {coldest_temp}, times: {self.__coldest_row}")

    def find_hottest_temp_in_row(self, complete_data):
        hottest_temp = float(complete_data[1][3])
        self.__hottest_row = [complete_data[1]]
        for row in complete_data[1:]:
            if float(row[3]) > hottest_temp:
                hottest_temp = float(row[3])
                self.__hottest_row = [row]
            elif float(row[3]) == hottest_temp:
                self.__hottest_row.append(row)

    def find_coldest_day(self, days_data):
        coldest_days = [days_data[0]]
        coldest_temp_middle = self.calc_temp_sum_of_day(days_data[0]) / len(days_data[0])
        for day in days_data[1:]:
            day_sum = self.calc_temp_sum_of_day(day)
            day_middle = day_sum / len(day)
            if day_middle < coldest_temp_middle:
                coldest_temp_middle = day_middle
                coldest_days = [day]
            elif day_middle == coldest_temp_middle:
                coldest_days.append(day)
        return coldest_days

    def calc_temp_sum_of_day(self, day_data):
        temp_sum = 0
        for row in day_data:
            temp_sum += float(row[3])
        return temp_sum

    def separate_into_days(self, year_data):
        """structure:
            [[day], ..., [day]]
            day:
                [row, ..., row]
        """
        temperatures_by_day = [[]]
        total_day = 1
        num_days = 0
        for row in year_data[1:]:

            delta_day = int(row[2][6:8]) - total_day
            print(delta_day, int(row[2][6:8]), total_day)
            total_day = int(row[2][6:8])
            if delta_day == 1:
                temperatures_by_day.append([])
                num_days += 1
                temperatures_by_day[num_days].append(row)
            else:
                temperatures_by_day[num_days].append(row)
        return temperatures_by_day
        # store information of each day of the year

    def separate_into_years(self, complete_data):
        temperatures_by_year = [[]]
        total_year = int(complete_data[1][2][0:4])
        num_years = 0
        for row in complete_data[1:]:
            delta_year = int(row[2][0:4]) - total_year
            total_year = int(row[2][0:4])
            if delta_year == 1:
                temperatures_by_year.append([])
                num_years += 1
                temperatures_by_year[num_years].append(row)
            else:
                temperatures_by_year[num_years].append(row)
        return temperatures_by_year


if __name__ == '__main__':
    D = DataSet()
    TEMP = Temperature()

    D.open_file()
    mydata = D.get_data_set()
    TEMP.find_coldest_temp_in_row(mydata)
    ys = TEMP.separate_into_years(mydata)

    total = []
    for y in ys:
        total.append(TEMP.separate_into_days(y))
        days = TEMP.separate_into_days(y)
        TEMP.find_coldest_day(days)
        # print(TEMP.calc_temp_sum_of_day(TEMP.separate_into_days(y)[0]) / len(TEMP.separate_into_days(y)[0]))
