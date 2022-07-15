"""Module for calulating mean, median, mode of data sets."""


def calc_mean(nums):
    """Calculates the mean of a list of numbers."""

    mean = round(sum(nums) / len(nums), 3)
    return mean


def main():
    """Runs the main process."""

    data_set_one = [6, 9, 1, 2, 6, 3, 7]
    # data_set_two = [6, 9, 1, 2, 6, 3, 7, 4]
    # data_set_three = [6, 9, 1, 2, 6, 3, 7, 4, 1]

    mean = calc_mean(data_set_one)
    print(mean)


if __name__ == "__main__":
    main()
