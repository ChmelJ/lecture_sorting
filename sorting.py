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


def selection_sorting(list_of_numbers, direction='ascend'):
    sorted_list_of_numbers = list_of_numbers.copy()
    for i in range(len(sorted_list_of_numbers)):
        smallest = float('inf')
        ind_min = i
        for ind, number in enumerate(sorted_list_of_numbers[i:]):
            if number < smallest:
                smallest = number
                ind_min = ind + i
        sorted_list_of_numbers[i], sorted_list_of_numbers[ind_min] =\
            sorted_list_of_numbers[ind_min], sorted_list_of_numbers[i]
    if direction != 'ascend':
        sorted_list_of_numbers.reverse()
    return sorted_list_of_numbers


def bubble_sort(list_of_numbers):
    sorted_list_of_numbers = list_of_numbers.copy()
    for i in range(len(sorted_list_of_numbers) - 1):
        for ind in range(len(sorted_list_of_numbers) - i - 1):
            if sorted_list_of_numbers[ind] > sorted_list_of_numbers[ind + 1]:
                sorted_list_of_numbers[ind], sorted_list_of_numbers[ind + 1] = \
                    sorted_list_of_numbers[ind + 1], sorted_list_of_numbers[ind]
    return sorted_list_of_numbers


def insertion_sort(list_of_numbers):
    sorted_list_of_numbers = list_of_numbers.copy()
    for i in range(1, len(sorted_list_of_numbers)):
        number = sorted_list_of_numbers[i]
        k = i - 1
        while k >= 0 and sorted_list_of_numbers[k] > number:
            sorted_list_of_numbers[k + 1], sorted_list_of_numbers[k] = \
                sorted_list_of_numbers[k], sorted_list_of_numbers[k + 1]
            k = k - 1
    return sorted_list_of_numbers


def main():
    my_data = read_data('numbers.csv')
    selection_sorted_numbers = selection_sorting(my_data['series_1'], direction='ascend')
    bubble_sorted_numbers = bubble_sort(my_data['series_1'])
    insertion_sorted_numbers = insertion_sort(my_data['series_1'])
    print(my_data['series_1'])
    print(selection_sorted_numbers)
    print(bubble_sorted_numbers)
    print(insertion_sorted_numbers)


if __name__ == '__main__':
    main()
