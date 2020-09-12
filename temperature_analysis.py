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

    def find_coldest_day(self, year_data):
        pass

    def separate_years(self, complete_data):
        """structure:
            [[day], ..., [day]]
            day:
                [row, ..., row]
        """
        temperatures_by_day = [[]]
        total_day = 1
        num_days = 0
        for row in complete_data[1:100]:
            delta_day = int(row[2][6:8]) - total_day
            total_day = int(row[2][6:8])
            if delta_day == 1:
                temperatures_by_day.append([])
                num_days += 1
                temperatures_by_day[num_days].append(row)
            else:
                temperatures_by_day[num_days].append(row)


if __name__ == '__main__':
    D = DataSet()
    TEMP = Temperature()

    D.open_file()
    mydata = D.get_data_set()
    TEMP.find_coldest_temp_in_row(mydata)
    TEMP.separate_years(mydata)
