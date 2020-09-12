

class Temperature:
    def __init__(self):
        self.__hottest_temp = None
        self.__coldest_temp = None

        self.__hottest_day = None
        self.__coldest_day = None

    def find_coldest_temp_and_time(self, complete_data):
        self.__coldest_temp = float(complete_data[1][3])
        coldest_times = [complete_data[1][2]]
        for row in complete_data[1:]:
            if float(row[3]) < self.__coldest_temp:
                self.__coldest_temp = float(row[3])
                coldest_times = [row[2]]
            elif float(row[3]) == self.__coldest_temp:
                coldest_times.append(row[2])
        print(f"coldest temp: {self.__coldest_temp}, times: {coldest_times}")


