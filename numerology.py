while True:
    welcome = raw_input("Welcome to the world of numerology. Do you want to learn more about your core numbers? (Y/N) ")
    if welcome.lower() == "n":
        print "You're missing out on the path to enlightenment. Have a great day!"
    elif welcome.lower() != "y":
        print "Input Y or N"
    else:
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
                            elif (month == 2) and ((day < 1) or (day > 29)):
                                print "That may be a day on Venus, but not on Earth!"
                            elif (month in [4, 6, 9, 11]) and ((day < 1) or (day > 30)):
                                print "That may be a day on Saturn, but not on Earth!"
                            else:
                                while True:
                                    year = raw_input("Input your year of birth: ")
                                    if not year.isdigit():
                                        print "Please input the year based on the Gregorian calendar."
                                    else:
                                        year = int(year)
                                    break
                        break
            break
    break
