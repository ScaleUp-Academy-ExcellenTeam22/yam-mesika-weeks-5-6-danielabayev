import random
import time
import datetime

INPUT_DATE_MESSAGE = "Please enter date in YYYY-MM-DD format: "


def print_date() -> None:
    """
    The main function - read the data and call the other functions to calculate
    the random date.
    Then check if the new date is in monday, print the date
    and if the date is monday say "i don't have vinaigrette".
    :return: don't return anything.
    """
    start_date = input(INPUT_DATE_MESSAGE)
    end_date = input(INPUT_DATE_MESSAGE)
    rand_date = random_date(start_date, end_date, '%Y-%m-%d', random.random())
    print(rand_date)
    if check_if_monday(rand_date):
        print("I don't have vinaigrette!")


def random_date(start: str, end: str, time_format: str, fraction_for_mul: float) -> datetime.date:
    """
    This function receive the start and end date and the format of the time and calculate date between
    the dates using the fraction received.
    :param start: start date.
    :param end: end date.
    :param time_format: the format the time receive.
    :param fraction_for_mul: the fraction to calculate date between the start and end date.
    :return: the function return the new date.
    """
    start_time = time.mktime(time.strptime(start, time_format))
    end_time = time.mktime(time.strptime(end, time_format))
    # create the calculation - the mul_value is always between 0-1
    random_time = start_time + fraction_for_mul * (end_time - start_time)
    # create the time in the correct format
    return datetime.date(time.localtime(random_time).tm_year,
                         time.localtime(random_time).tm_mon,
                         time.localtime(random_time).tm_mday)


def check_if_monday(date: datetime.date) -> bool:
    """
    This function receive the date and check if its monday.
    :param date: the date to check.
    :return: true if the date is monday, else false.
    """
    return date.isoweekday() == 1


if __name__ == '__main__':
    print_date()
