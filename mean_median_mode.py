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


def main():
    """Runs the main process."""

    data_set_one = [6, 9, 1, 2, 6, 3, 7]
    # data_set_two = [6, 9, 1, 2, 6, 3, 7, 4]
    # data_set_three = [6, 9, 1, 2, 6, 3, 7, 4, 1]

    mean = calc_mean(data_set_one)
    print(mean)
    median = calc_median(data_set_one)
    print(median)


if __name__ == "__main__":
    main()
