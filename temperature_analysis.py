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
            if float(row[3]) < hottest_temp:
                hottest_temp = float(row[3])
                self.__hottest_row = [row]
            elif float(row[3]) == hottest_temp:
                self.__hottest_row.append(row)




if __name__ == '__main__':
    D = DataSet()
    TEMP = Temperature()

    D.open_file()
    mydata = D.get_data_set()
    TEMP.find_coldest_temp_in_row(mydata)
