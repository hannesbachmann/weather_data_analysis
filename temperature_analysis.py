

class Temperature:
    def __init__(self):
        self.__hottest_temp = None
        self.__coldest_temp = None

        self.__hottest_day = None
        self.__coldest_day = None

    def find_coldest_temp_and_time(self, complete_data):
        self.__coldest_temp = float(complete_data[1][3])
