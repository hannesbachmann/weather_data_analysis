import csv


class DataSet:
    def __init__(self):
        """
        Initializes for the DataSet class
        """
        self.__REL_PATH = 'data_TT_TU_MN009'
        self.__file_type = 'csv'

        self.__data = []  # array for the rows and cols of the data table

    def open_file(self):
        """
        open and store the data from the .csv file
        store in self.__data list
        """
        self.__data = []
        with open(self.__REL_PATH + '.' + self.__file_type) as data_csv:  # open the file
            csv_reader_obj = csv.reader(data_csv, delimiter=',')  # create the csv reader object
            for row in csv_reader_obj:
                self.__data.append(row)

    def get_data_set(self):
        """
        getter for the full data set

        :return self.__data: {array-like}, shape = [rows]
            rows: {array-like}, shape = [product_code, SDO_ID, time_stamp, temperature, quality_niveau,
                                        quality_byte]
                product_code: string
                SDO_ID: string
                time_stamp: string, time in 'yyyymmddhhmm'
                temperature: string, can be converted to float value
                quality_niveau: string
                quality_byte: string
        """
        return self.__data

    def get_legend(self):
        """
        getter for the top legend of the .csv file

        :return self.__data[0]: {array-like}, shape = [ "Produkt_Code",
                                                        "SDO_ID","Zeitstempel",
                                                        "Wert",
                                                        "Qualitaet_Niveau",
                                                        "Qualitaet_Byte" ]
        """
        return self.__data[0]


class TempData:
    def __init__(self):
        """
        Initializes for the TempData class
        """
        self.__rel_path = 'hottest_coldest'
        self.__file_type = 'csv'

    def store_extrema(self, legend, hottest, coldest):
        with open(self.__rel_path + '.' + self.__file_type, 'w', newline='') as csv_hottest:
            csv_writer = csv.writer(csv_hottest, delimiter=',')
            csv_writer.writerow(legend)
            for hot_row in hottest:
                csv_writer.writerow(hot_row)
            for cold_row in coldest:
                csv_writer.writerow(cold_row)
