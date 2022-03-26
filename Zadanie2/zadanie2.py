"""
Write a program to validate the PESEL number according to the official
format specification. Prepare unit tests that check several data
incorrect data and at least one correct pesel number.
"""
from calendar import monthrange
import sys

def check_pesel_month(month: list) -> bool:
    """
    Returns False if given month is not possible to obtain in pesel number range, else returns True

    param: month - List with two digits that indicates what is the month of birth.
    """
    month_number = ''.join([m for m in month])
    month_number = int(month_number)
    if  month_number not in range(0, 13) and  month_number not in range(21,33) and month_number not in range(81, 92):
        return False
    return True
 
def check_pesel_day(year:list, month:list, day:list) -> bool:
    """
    Returns False if given day is not possible to obtain in pesel number range, else returns True
    e.g. day = 32 in every month or day = 30 in February is not possible.

    param: year - List with two digits that indicates what is the year of birth.
    param: month - List with two digits that indicates what is the month of birth.
    param: day - List with two digits that indicates what is the day of birth.
    """
    month_number = ''.join(month)
    month_number = int(month_number)
    day_number = ''.join(day)
    day_number = int(day_number)
    if month_number in range(0, 13):
        year_number = int('19'.join(year))
    elif month_number in range(21, 33):
        year_number = int('20'.join(year))
        month_number -= 20
    elif month_number in range(81, 93):
        year_number = int('18'.join(year))
        month_number -= 80
    else:
        return False

    if day_number > number_of_days_in_month(year_number, month_number):
        return False
    
    return True

def number_of_days_in_month(year: int, month: int) -> int:
    """
    Returns amount of days in given month of given year.
    """
    return monthrange(year, month)[1]

def check_sum_number(pesel: list, weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3], temp_result = 0, final_result = 0) -> bool:
    """
    Returns False if given control number is not possible to obtain in pesel number range, else returns True
    e.g. 
    Multiply each digit from your PESEL number by the appropriate weight: 1-3-7-9-1-3-7-9-1-3.
    0 * 1 = 0
    2 * 3 = 6 
    0 * 7 = 0
    7 * 9 = 63
    0 * 1 = 0
    8 * 3 = 24 
    0 * 7 = 0
    3 * 9 = 27
    6 * 1 = 6
    2 * 3 = 6
    Add together the results obtained. Note, if you get a two-digit number when multiplying, add only the last digit (for example, add 3 instead of 63).
    0 + 6 + 0 + 3 + 0 + 4 + 0 + 7 +6 + 6 = 32
    Subtract the result from 10. Note: if you get a two-digit number when adding, subtract only the last digit (for example, instead of 32 subtract 2). The digit you get is the check digit. 10 - 2 = 8

    param: pesel - given pesel in List format
    """
    for i in range (len(pesel) - 1):
        temp_result = int(pesel[i]) * weight[i]
        if temp_result >= 10:
            temp_result %= 10
        final_result += temp_result

    if final_result >= 10:
        final_result = 10 - final_result % 10 
    else:
        final_result = 10 - final_result
    
    return final_result == int(pesel[10])

def validate_pesel(pesel: str) -> str:
    pesel = [str(x) for x in str(pesel) if x.isdigit()]
    if len(pesel) == 11:
        if check_pesel_month(pesel[2:4]):
            if check_pesel_day(pesel[0:2], pesel[2:4], pesel[4:6]):
                if check_sum_number(pesel):
                    return "Pesel number correct!"
                else:
                    return "Incorrect control number!"
            else:
                return "Incorrect day of birth!"
        else:
            return "Incorrect month of birth!"
    else:
        return "Pesel number must be 11 char long and it must contain only digits"


def main(argv):
    if len(argv) == 1:
        print(validate_pesel(f'{argv[0]}'))
    else:
        print('Enter Pesel number as parameter')

if __name__ == "__main__":
    main(sys.argv[1:])