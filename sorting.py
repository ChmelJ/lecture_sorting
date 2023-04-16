import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file)
        keys = next(reader)
        data = [dict(zip(keys, i)) for i in reader]
    data_dictionary = {i: [c[i] for c in data] for i in keys}
    return data_dictionary


def main():
    my_data =read_data('numbers.csv')
    print(my_data)


if __name__ == '__main__':
    main()
