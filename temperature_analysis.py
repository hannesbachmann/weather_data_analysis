class Temperature:
    def __init__(self):
        """
        Initialize from Temperature class
        """
        # store the max/min temperature for every year
        self.__hottest_temp_years = []
        self.__coldest_temp_years = []

    def get_hottest_temp_each_year(self):
        """
        getter for hottest temperatures of the year and when they occurred

        :return self.__hottest_temp_years: {array-like}, shape = [years]
            years: {array-like}, shape = [rows]
                rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                            quality_byte]
                    product_code: string
                    SDO_ID: string
                    time_stamp: string, time in 'yyyymmddhhmm'
                    temperature: string, can be converted to float value
                    quality_niveau: string
                    quality_byte: string
        """
        return self.__hottest_temp_years

    def get_coldest_temp_each_year(self):
        """
        getter for coldest temperatures of the year and when they occurred

        :return self.__coldest_temp_years: {array-like}, shape = [years]
            years: {array-like}, shape = [rows]
                rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                            quality_byte]
                    product_code: string
                    SDO_ID: string
                    time_stamp: string, time in 'yyyymmddhhmm'
                    temperature: string, can be converted to float value
                    quality_niveau: string
                    quality_byte: string
        """
        return self.__coldest_temp_years

    def find_coldest_temp_in_year(self, year_data):
        """
        finding the coldest temperature from each year
        store in self.__coldest_temp_year list

        :param year_data: {array-like}, shape = [rows]
                rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                            quality_byte], represent the years
                    product_code: string
                    SDO_ID: string
                    time_stamp: string, time in 'yyyymmddhhmm'
                    temperature: string, can be converted to float value
                    quality_niveau: string
                    quality_byte: string
        """
        coldest_temp = float(year_data[1][3])
        coldest_row = [year_data[1]]
        for row in year_data[1:]:
            if float(row[3]) < coldest_temp:
                coldest_temp = float(row[3])
                coldest_row = [row]
            elif float(row[3]) == coldest_temp:
                coldest_row.append(row)
        self.__coldest_temp_years.append(coldest_row)

    def find_hottest_temp_in_year(self, year_data):
        """
        finding the hottest temperature from each year
        store in self.__hottest_temp_year list

        :param year_data: {array-like}, shape = [rows]
                rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                            quality_byte], represent the years
                    product_code: string
                    SDO_ID: string
                    time_stamp: string, time in 'yyyymmddhhmm'
                    temperature: string, can be converted to float value
                    quality_niveau: string
                    quality_byte: string
        """
        hottest_temp = float(year_data[1][3])
        hottest_row = [year_data[1]]
        for row in year_data[1:]:
            if float(row[3]) > hottest_temp:
                hottest_temp = float(row[3])
                hottest_row = [row]
            elif float(row[3]) == hottest_temp:
                hottest_row.append(row)
        self.__hottest_temp_years.append(hottest_row)

    def find_coldest_day(self, days_data):
        """
        find the coldest day for every year

        :param days_data: {array-like}, shape = [years]
            years: {array-like}, shape = [rows]
                rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                            quality_byte], represent the days
                    product_code: string
                    SDO_ID: string
                    time_stamp: string, time in 'yyyymmddhhmm'
                    temperature: string, can be converted to float value
                    quality_niveau: string
                    quality_byte: string
        :return coldest_days: {array-like}, shape = [days]
            days: {array-like}, shape = [day]
                day: {array-like}, shape = [rows]
                    rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                                quality_byte], represent the days
                        product_code: string
                        SDO_ID: string
                        time_stamp: string, time in 'yyyymmddhhmm'
                        temperature: string, can be converted to float value
                        quality_niveau: string
                        quality_byte: string
        """
        coldest_days = [days_data[0]]
        coldest_temp_middle = self.calc_temp_sum_of_day(days_data[0]) / len(days_data[0])
        for day in days_data[1:]:
            if len(day) > 1:
                day_sum = self.calc_temp_sum_of_day(day)
                day_middle = day_sum / len(day)
                if day_middle < coldest_temp_middle:
                    coldest_temp_middle = day_middle
                    coldest_days = [day]
                elif day_middle == coldest_temp_middle:
                    coldest_days.append(day)
        return coldest_days

    def find_hottest_day(self, days_data):
        """
        find the hottest day for every year

        :param days_data: {array-like}, shape = [years]
            years: {array-like}, shape = [rows]
                rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                            quality_byte], represent the days
                    product_code: string
                    SDO_ID: string
                    time_stamp: string, time in 'yyyymmddhhmm'
                    temperature: string, can be converted to float value
                    quality_niveau: string
                    quality_byte: string
        :return hottest_days: {array-like}, shape = [days]
            days: {array-like}, shape = [day]
                day: {array-like}, shape = [rows]
                    rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                                quality_byte], represent the days
                        product_code: string
                        SDO_ID: string
                        time_stamp: string, time in 'yyyymmddhhmm'
                        temperature: string, can be converted to float value
                        quality_niveau: string
                        quality_byte: string
        """
        hottest_days = [days_data[0]]
        hottest_temp_middle = self.calc_temp_sum_of_day(days_data[0]) / len(days_data[0])
        for day in days_data[1:]:
            if len(day) > 1:
                day_sum = self.calc_temp_sum_of_day(day)
                day_middle = day_sum / len(day)
                if day_middle > hottest_temp_middle:
                    hottest_temp_middle = day_middle
                    hottest_days = [day]
                elif day_middle == hottest_temp_middle:
                    hottest_days.append(day)
        return hottest_days

    def calc_temp_sum_of_day(self, day_data):
        """
        calculating the sum of the temperatures of every day

        :param day_data: years: {array-like}, shape = [rows]
                rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                            quality_byte], represent the days
                    product_code: string
                    SDO_ID: string
                    time_stamp: string, time in 'yyyymmddhhmm'
                    temperature: string, can be converted to float value
                    quality_niveau: string
                    quality_byte: string
        :return temp_sum:
        """
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
        num_days = 0
        for row in year_data:
            if int(row[2][8:10]) == 23:
                temperatures_by_day[num_days].append(row)
                num_days += 1
                temperatures_by_day.append([])
            else:
                temperatures_by_day[num_days].append(row)
        temperatures_by_day.pop()
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
