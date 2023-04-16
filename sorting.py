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
    data_dictionary = {i: [int(c[i]) for c in data] for i in keys}
    return data_dictionary


def selection_sorting(list_of_numbers):
    for i in range(len(list_of_numbers)):
        smallest = float('inf')
        ind_min = i
        for ind, number in enumerate(list_of_numbers[i:]):
            if number < smallest:
                smallest = number
                ind_min = ind+i
        list_of_numbers[i], list_of_numbers[ind_min] = list_of_numbers[ind_min], list_of_numbers[i]
    return list_of_numbers


def main():
    my_data = read_data('numbers.csv')
    selection_sorted_numbers = selection_sorting(my_data['series_3'])
    print(my_data['series_3'])
    print(selection_sorted_numbers)


if __name__ == '__main__':
    main()
