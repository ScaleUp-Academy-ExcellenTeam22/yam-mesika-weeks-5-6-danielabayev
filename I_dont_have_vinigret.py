import random
import time
import datetime

INPUT_DATE_MESSAGE = "Please enter date in YYYY-MM-DD format: "
MONDAY_MESSAGE = "I don't have vinaigrette!"


# the main function - read the data and call the other functions to calculate
# the random date and check if the new date is in monday
def print_date():
    start_date = input(INPUT_DATE_MESSAGE)
    end_date = input(INPUT_DATE_MESSAGE)
    rand_date = random_date(start_date, end_date, '%Y-%m-%d', random.random())
    print(rand_date)
    if check_if_monday(rand_date):
        print(MONDAY_MESSAGE)


# function to create the new date
def random_date(start, end, time_format, mul_value):
    start_time = time.mktime(time.strptime(start, time_format))
    end_time = time.mktime(time.strptime(end, time_format))
    # create the calculation - the mul_value is always between 0-1
    random_time = start_time + mul_value * (end_time - start_time)

    # create the time in the correct format
    return datetime.date(time.localtime(random_time).tm_year,
                         time.localtime(random_time).tm_mon,
                         time.localtime(random_time).tm_mday)


def check_if_monday(date):
    return date.isoweekday() == 1


if __name__ == '__main__':
    print_date()
