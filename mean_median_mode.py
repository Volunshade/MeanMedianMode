"""Module for calulating mean, median, mode of data sets."""


def calc_mean(nums):
    """Calculates the mean of a list of numbers."""

    mean = round(sum(nums) / len(nums), 3)
    return mean


def calc_median(nums):
    """Calculates the median of a list of numbers."""

    sorted_data = sorted(nums)
    length = len(sorted_data)
    if not length % 2:
        # even
        upper_midpoint = length // 2
        lower_midpoint = upper_midpoint - 1
        upper_value = sorted_data[upper_midpoint]
        lower_value = sorted_data[lower_midpoint]
        median = (upper_value + lower_value) / 2
    else:
        # odd
        midpoint = length // 2
        median = sorted_data[midpoint]
        
    return round(float(median), 2)


def calc_mode(nums):
    """Calculates the mode of a list of numbers"""

    frequencies = {}
    for unique_number in set(nums):
        frequency = nums.count(unique_number)
        frequencies[unique_number] = frequency

    highest = -1
    for value in frequencies.values():
        if value > highest:
            highest = value

    modes = []
    for key, value in frequencies.items():
        if value == highest:
            modes.append(key)

    return modes


def solve_dataset(dataset):
    """Calculates the mean, median, and mode of a dataset"""

    mean = calc_mean(dataset)
    median = calc_median(dataset)
    mode = calc_mode(dataset)

    return mean, median, mode


def main():
    """Runs the main process."""

    data_set_one = [6, 9, 1, 2, 6, 3, 7]
    data_set_two = [6, 9, 1, 2, 6, 3, 7, 4]
    data_set_three = [6, 9, 1, 2, 6, 3, 7, 4, 1]

    datasets = (data_set_one, data_set_two, data_set_three)
    for dataset in datasets:
        mean, median, mode = solve_dataset(dataset)
        print(f'{mean=}, {median=}, {mode=}')


if __name__ == "__main__":
    main()
