def greeting():
    #prints introduction message
    print """\nWelcome to the nexus of numerology.\n
Numerology is the study of the numerical value of letters in words, names and birthdays.\n
It is often associated with the paranormal, similar to astrology, and the belief in the divine, mystical relationship between numbers and one or more coinciding events.\n"""

greeting()


# definition of function to input birthdate


def birthdate():
    while True:
        year = raw_input("Input your year of birth: ")
        if not year.isdigit():
            print "Please input the year based on the Gregorian calendar."
        else:
            year = int(year)
            while True:
                month = raw_input("Input your month (1-12) of birth: ")
                if not month.isdigit():
                    print "Please input the numerical value of the month."
                else:
                    month = int(month)
                    if (month < 1) or (month > 12):
                        print "That may be a month on Mars, but not on Earth!"
                    else:
                        while True:
                            day = raw_input("Input your day of birth: ")
                            if not day.isdigit():
                                print "Please input the numerical value of the day."
                            else:
                                day = int(day)
                                if (month in [1, 3, 5, 7, 8, 10, 12]) and ((day < 1) or (day > 31)):
                                    print "That may be a day on Jupiter, but not on Earth!"
                                elif (month in [4, 6, 9, 11]) and ((day < 1) or (day > 30)):
                                    print "That may be a day on Saturn, but not on Earth!"
                                elif (month == 2) and (((year % 100 == 0) and (year % 400 == 0)) or ((year % 4 == 0) and (year % 100 != 0))) and ((day < 1) or (day > 29)):
                                    # for leap year, if divisible by 100 but not 400, then not leap year. otherwise, divisible by 4.
                                    print "You took a flying leap off of Pluto!"
                                elif (month == 2) and ((year % 4 != 0) or ((year % 4 == 0) and (year % 100 == 0))) and ((day < 1) or (day > 28)):
                                    print "That may be a day on Venus, but not on Earth!"
                                else:
                                    break
                break
        break

birthdate()

from datetime import date


# definition of function to calculate various items to single digit or master number


def single_digit_master(single_digit):
    while True:
        if (single_digit < 10) or (single_digit == 11) or single_digit == 22:
            single_digit_master = single_digit
            break
        elif single_digit > 99:
            single_digit_str = str(single_digit)
            single_digit_total = int(single_digit_str[0]) + int(single_digit_str[1]) + int(single_digit_str[2]) + int(single_digit_str[3])
            single_digit = single_digit_total
        else:
            single_digit_str = str(single_digit)
            single_digit_total = int(single_digit_str[0]) + int(single_digit_str[1])
            single_digit = single_digit_total
    return single_digit_master

#single_year_master = single_digit_master(year)
#single_month_master = single_digit_master(month)
#single_day_master = single_digit_master(day)


# definition of function to calculate various items to single digit


def single_digit_uno(single_digit):
    while True:
        if (single_digit < 10) or (single_digit == 11) or single_digit == 22:
            single_digit_uno = single_digit
            break
        elif single_digit > 99:
            single_digit_str = str(single_digit)
            single_digit_total = int(single_digit_str[0]) + int(single_digit_str[1]) + int(single_digit_str[2]) + int(single_digit_str[3])
            single_digit = single_digit_total
        else:
            single_digit_str = str(single_digit)
            single_digit_total = int(single_digit_str[0]) + int(single_digit_str[1])
            single_digit = single_digit_total
    return single_digit_uno

#single_year_uno = single_digit_uno(year)
#single_month_uno = single_digit_uno(month)
#single_day_uno = single_digit_uno(day)
