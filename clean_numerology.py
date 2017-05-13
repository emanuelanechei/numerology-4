# definition of function to print introduction message


def greeting():
    # introduction message in numerology program
    print """\nWelcome to the nexus of numerology.\n
Numerology is the study of the numerical value of letters in words, names and birthdays.\n
It is similar to astrology, and often associated with the belief in the divine, mystical relationship between numbers (and their related vibrations) and one or more coinciding events.\n"""


# definition of function for birth year


def ask_year(who):
    # asks individual for birth year, with error message for any response that are not integers
    if who == "partner":
        while True:
            year = raw_input("\nInput your partner's year of birth: ")
            if not year.isdigit():
                print "Please input the year based on the Gregorian calendar."
            else:
                year = int(year)
                return year
    else:
        while True:
            year = raw_input("\nInput your year of birth: ")
            if not year.isdigit():
                print "Please input the year based on the Gregorian calendar."
            else:
                year = int(year)
                return year


# definition of function for birth month


def ask_month(who):
    # asks individual for birth month, with error message for any response that is not within month numbers of 1 to 12
    if who == "partner":
        while True:
            month = raw_input("Input your partner's month (1-12) of birth: ")
            if not month.isdigit():
                print "Please input the numerical value of the month."
            elif (int(month) < 1) or (int(month) > 12):
                print "That may be a month on Mars, but not on Earth!"
            else:
                month = int(month)
                return month
    else:
        while True:
            month = raw_input("Input your month (1-12) of birth: ")
            if not month.isdigit():
                print "Please input the numerical value of the month."
            elif (int(month) < 1) or (int(month) > 12):
                print "That may be a month on Mars, but not on Earth!"
            else:
                month = int(month)
                return month


# definition of function for birth day


def ask_day(year, month, who):
    # asks individual for birth day, with various error messages for days that do not match the respective month, as well as adjusting February for leap years
    if who == "partner":
        while True:
            day = raw_input("Input your partner's day of birth: ")
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
                    return day
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
                    return day


# definition of function to calculate various items to single digit or master numbers of 11 or 22


def single_digit_master(single_digit):
    # if digits are not 1-9, 11 or 22, continue to add individual digits together until total equals one of those options
    while True:
        #if ((single_digit >= 1) and (single_digit <= 9)) or (single_digit == 11) or (single_digit == 22):
        if (single_digit <= 9) or (single_digit == 11) or (single_digit == 22):
            single_digit_master = single_digit
            break
        else:
            partial_sum = 0
            for number in str(single_digit):
                partial_sum += int(number)
            single_digit = partial_sum

    return single_digit_master


# definition of function to calculate various items to single digit


def single_digit_uno(single_digit):
    # if digits are not 1-9, continue to add individual digits together until total equals one of those options
    while True:
        #if (single_digit >= 1) and (single_digit <= 9):
        if single_digit <= 9:
            single_digit_uno = single_digit
            break
        else:
            partial_sum = 0
            for number in str(single_digit):
                partial_sum += int(number)
            single_digit = partial_sum

    return single_digit_uno


# definition of function to calculate life path number


def life_path_calc(single_year_master, single_month_master, single_day_master):
    # takes each category of year, month and day after it has been sum to 1-9, 11 or 22 and then adds the three variables together
    life_path_raw = single_year_master + single_month_master + single_day_master
    # the individual digits of the result are then added together until it equals 1-9, 11 or 22
    life_path = single_digit_master(life_path_raw)

    return life_path


from meanings import *


# definition of function to calculate first challenge number


def first_chall_calc(single_day_uno, single_month_uno):
    # difference between digits of birth month and birth day, individually summed down to 1-9
    first_chall = abs(single_day_uno - single_month_uno)

    return first_chall


# definition of function to display first challenge meaning


def first_chall_meaning(first_chall):
    # displays meaning based on first challenge number calculation
    print """\nYour first challenge number is {}, which is from birth to approximately age 35.\n""".format(first_chall)
    chall_meaning(first_chall)


# definition of function to calculate second challenge number


def sec_chall_calc(single_day_uno, single_year_uno):
    # difference between digits of birth year and birth day, individually summed down to 1-9
    sec_chall = abs(single_year_uno - single_day_uno)

    return sec_chall


# definition of function to display second challenge meaning


def sec_chall_meaning(sec_chall):
    # displays meaning based on second challenge number calculation
    print """\nYour second challenge number is {}, which is from approximately age 35 to approximately age 60.\n""".format(sec_chall)
    chall_meaning(sec_chall)


# definition of function to calculate third challenge number


def third_chall_calc(first_chall, sec_chall):
    # difference betwen first and second challenge numbers
    third_chall = abs(sec_chall - first_chall)

    return third_chall


# definition of function to display third challenge meaning


def third_chall_meaning(third_chall):
    # displays meaning based on third challenge number calculation
    print """\nYour third challenge number is {}, which represents the primary challenge that one faces throughout life.\n""".format(third_chall)
    chall_meaning(third_chall)


# definition of function to calculate fourth challenge number


def fourth_chall_calc(single_month_uno, single_year_uno):
    # difference between digits of birth year and birth month, individually summed down to 1-9
    fourth_chall = abs(single_year_uno - single_month_uno)

    return fourth_chall


# definition of function to display fourth challenge meaning


def fourth_chall_meaning(fourth_chall):
    # displays meaning based on fourth challenge number calculation
    print """\nYour fourth (and final) challenge number is {}, which from approximately age 60 to end of life.\n""".format(fourth_chall)
    chall_meaning(fourth_chall)


# definition of function to calculate personal year number


from datetime import date


def pers_year_calc(single_day_uno, single_month_uno, single_year_uno, month, day):
    # calculates current year digits down to single digit 1-9
    single_current_uno = single_digit_uno(date.today().year)
    # takes each category of current year, month and day of birth after it has been sum to 1-9 and then adds the three variables together
    personal_year_raw = single_current_uno + single_month_uno + single_day_uno
    # the individual digits of the result are then added together until it equals 1-9
    personal_year = single_digit_uno(personal_year_raw)
    # pulls today's date and birth day in current year
    birth_raw = date(date.today().year, month, day)

    # if birthday has not occurred yet, then personal year is adjusted to prior personal year number since personal year number is effective from birthday to birthday
    if date.today() < birth_raw:
        personal_year = personal_year - 1
    else:
        personal_year

    return personal_year


# definition of function for last name


def ask_last_name(birth_or_nick):
    # asks individual for last name, with error for integers
    # gives option for individual to provide birth name vs. common (nick) name, includes option for partner input
    if birth_or_nick == "birth":
        while True:
            last_name = raw_input("\nInput your family (last) name at birth: ")
            if last_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return last_name
    elif birth_or_nick == "partner":
        while True:
            last_name = raw_input("\nInput your partner's family (last) name: ")
            if last_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return last_name
    else:
        while True:
            last_name = raw_input("\nInput your family (last) name: ")
            if last_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return last_name


# definition of function for middle name


def ask_middle_name(birth_or_nick):
    # asks individual for middle name, with error for integers
    # gives option for individual to provide birth name vs. common (nick) name, includes option for partner input
    if birth_or_nick == "birth":
        while True:
            middle_name = raw_input("Input your middle name at birth: ")
            if middle_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return middle_name
    elif birth_or_nick == "partner":
        while True:
            middle_name = raw_input("Input your partner's middle name: ")
            if middle_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return middle_name
    else:
        while True:
            middle_name = raw_input("Input your middle name: ")
            if middle_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return middle_name


# definition of function for first name


def ask_first_name(birth_or_nick):
    # asks individual for first name, with error for integers
    # gives option for individual to provide birth name vs. common (nick) name, includes option for partner input
    if birth_or_nick == "birth":
        while True:
            first_name = raw_input("Input your first (given) name at birth: ")
            if first_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return first_name
    elif birth_or_nick == "partner":
        while True:
            first_name = raw_input("Input your partner's first name: ")
            if first_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return first_name
    else:
        while True:
            first_name = raw_input("Input your first (nick) name: ")
            if first_name.isdigit():
                print "Your parents are so hipster that they named you a number."
            else:
                return first_name


# definition of function to clean name for miscellaneous characters that are not part of alphabet and case sensitivities


def clean_name(name):
    # cleans input for case sensitivities as well as for spaces, hyphenated names or abbreviations (e.g., Jr.)
    name = name.lower()
    name = name.replace("-", "")
    name = name.replace(".", "")
    name = name.replace(" ", "")
    return name


# definition of function for common (nick) name

def ask_nick_name():
    # asks individual if he/she has common (nick) name
    while True:
        # asks individual if he/she goes by another name
        nick_raw = raw_input("\nDo you go by another name (e.g., nickname)? (Y/N): ")
        nick_raw = nick_raw.lower()

        if not ((nick_raw == "y") or (nick_raw == "n")):
            print "Please input Y or N."
        else:
            return nick_raw


# definition of function to assign numerical value to letters


def name_calc(name):
    # assigns each letter a numerical value from 1-9 and calculates the total value of the word
    partial_sum = 0
    for letter in range(len(name)):
        partial_name = ((ord(name[letter]) - ord("a")) % 9) + 1
        partial_sum += partial_name
    name_value = partial_sum

    return name_value


# definition of a function to calculate expression/destiny number


def exp_calc(single_last_master, single_middle_master, single_first_master):
    # takes each category of last, middle and first names after it has been sum to 1-9, 11 or 22 and then adds the three variables together
    exp_raw = single_last_master + single_middle_master + single_first_master
    # the individual digits of the result are then added together until it equals 1-9, 11 or 22
    exp_dest = single_digit_master(exp_raw)

    return exp_dest


# set list of vowels

vowel = ("a", "e", "i", "o", "u")


# definition of a function to calculate only consonants


def consonants(name, vowel):
    # strips word of all vowels
    cons_name = name
    for letter in name:
        if letter in vowel:
            cons_name = cons_name.replace(letter, "")

    return cons_name


# definition of a function to calculate only vowels


def vowels(name, vowel):
    # strips word of all consonants
    vow_name = name
    for letter in name:
        if letter not in vowel:
            vow_name = vow_name.replace(letter, "")

    return vow_name


# definition of a function to calculate soul urge number


def soul_urge_calc(single_vow_last_master, single_vow_middle_master, single_vow_first_master):
    # takes each category of last, middle and first names after it has been sum to 1-9, 11 or 22 based on vowels only and then adds the three variables together
    soul_urge_raw = single_vow_last_master + single_vow_middle_master + single_vow_first_master
    # the individual digits of the result are then added together until it equals 1-9, 11 or 22
    soul_urge = single_digit_master(soul_urge_raw)

    return soul_urge


# definition of a function to calculate personality number


def personality_cal(single_cons_last_master, single_cons_middle_master, single_cons_first_master):
    # takes each category of last, middle and first names after it has been sum to 1-9, 11 or 22 based on consonants only and then adds the three variables together
    personality_raw = single_cons_last_master + single_cons_middle_master + single_cons_first_master
    # the individual digits of the result are then added together until it equals 1-9, 11 or 22
    personality = single_digit_master(personality_raw)

    return personality


# definition of a function to calculate hidden passion number


def pass_calc(name):
    # assigns each letter a numerical value from 1-9 and determines the number that is the most repetitive
    for letter in range(len(name)):
        partial_name = ((ord(name[letter]) - ord("a")) % 9) + 1

    partial_name = str(partial_name)
    hid_pass = int(max(partial_name, key=partial_name.count))

    return hid_pass


# definition of a function to calculate karmic number


def karmic_calc(cons_full_name):
    # strips full name of consonants only, converts into numerical value based on sum of each individual letter (assigned a numerical value from 1-9), and sum digits down to 1-9
    karmic = single_digit_uno(name_calc(cons_full_name))

    return karmic


# definition of a function to display cornerstone and capstone


def corn_cap(first_name):
    # pulls first letter of first name for cornerstone and last letter of first name for capstone
    cornerstone = first_name[0]
    capstone = first_name[-1]

    print """\nCornerstone gives insight into how you approach challenges in life and how you master situations. Capstone gives insight into how you make transitions in your life, how you finish projects or move from one thing into another.\n"""

    print """Your cornerstone ({}): """.format(cornerstone.upper())
    cc_meaning(cornerstone)

    print """Your capstone ({}): """.format(capstone.upper())
    cc_meaning(capstone)

    return cornerstone, capstone


# definition of a function to ask whether there is or is not a specific partner


def ask_partner():
    # asks individual if he/she has a partner in mind
    while True:
        # asks individual if he/she has a specific partner
        partner_raw = raw_input("\nDo you currently have a specific partner that you would like to assess? (Y/N): ")
        partner_raw = partner_raw.lower()

        if not ((partner_raw == "y") or (partner_raw == "n")):
            print "Please input Y or N."
        else:
            return partner_raw


# definition of a function to obtain partner's birthday information and calculate life path number

def partner_life_path(ind_life_path):
    # asks for partner's birthday
    year = ask_year("partner")
    month = ask_month("partner")
    day = ask_day(year, month, "partner")

    # calculates single digits master for year, month and day
    single_year_master = single_digit_master(year)
    single_month_master = single_digit_master(month)
    single_day_master = single_digit_master(day)

    # calculates life path number
    life_path = life_path_calc(single_year_master, single_month_master, single_day_master)

    # displays partner's life path number
    print """\nYour and your partner's life path numbers are {} and {}, respectively.\n""".format(ind_life_path, life_path)

    # calculates life path number to single digit
    partner_life_path = single_digit_uno(life_path)

    return partner_life_path


# definition of a function to obtain partner's name information and calculate expression number

def partner_exp_dest(ind_exp_dest):
    # asks for partner's birthday
    last_name = clean_name(ask_last_name("partner"))
    middle_name = clean_name(ask_middle_name("partner"))
    first_name = clean_name(ask_first_name("partner"))

    # calculate single digits master for first, middle and last names
    single_last_master = single_digit_master(name_calc(last_name))
    single_middle_master = single_digit_master(name_calc(middle_name))
    single_first_master = single_digit_master(name_calc(first_name))

    # calculates expression (destiny) number
    exp_dest = exp_calc(single_last_master, single_middle_master, single_first_master)

    # displays partner's expression (destiny) number
    print """\nYour and your partner's expression (destiny) numbers are {} and {}, respectively.\n""".format(ind_exp_dest, exp_dest)

    # calculates expression (destiny) number to single digit
    partner_exp_dest = single_digit_uno(exp_dest)

    return partner_exp_dest


# definition of a function to display main menu


def main_menu_choice():
    print """\n     1 - Show numerology by birthday."""
    print """     2 - Show numerology by birth name."""
    print """     3 - Show numerology by common or nick name."""
    print """     4 - Show partner compatibility."""
    print """     5 - Exit the program.\n"""

    choice = int(raw_input("Choose from the menu options: "))

    return choice


# definition of a function to display birthday numerology menu


def birthday_menu_choice():
    print """\n     0 - Return to main menu."""
    print """     1 - Show life path number."""
    print """     2 - Show birth day number."""
    print """     3 - Show challenge number(s)."""
    print """     4 - Show personal year number.\n"""

    choice = int(raw_input("Choose from the menu options (return to main menu to exit): "))

    return choice


# definition of a function to display challenge numbbers menu


def challenge_menu_choice():
    print """\n     0 - Return to birthday main menu."""
    print """     1 - Show first challenge number."""
    print """     2 - Show second challenge number."""
    print """     3 - Show third challenge number."""
    print """     4 - Show fourth challenge number.\n"""

    choice = int(raw_input("Choose from the menu options: "))

    return choice


# definition of a function to display name numerology menu


def name_menu_choice():
    print """\n     0 - Return to main menu."""
    print """     1 - Show expression (destiny) number."""
    print """     2 - Show soul urge number."""
    print """     3 - Show personality number."""
    print """     4 - Show hidden passion number."""
    print """     5 - Show karmic number."""
    print """     6 - Show cornerstone and capstone.\n"""

    choice = int(raw_input("Choose from the menu options (return to main menu to exit): "))

    return choice


# definition of a function to display compatibility menu


def compatibility_menu_choice():
    print """\n     0 - Return to main menu."""
    print """     1 - Based on birthday."""
    print """     2 - Based on name.\n"""

    choice = int(raw_input("Choose from the menu options (return to main menu to exit): "))

    return choice


# definition of a function to execute within the challenge menu


def challenge_exec_repl(single_day_uno, single_month_uno, single_year_uno):
    # displays objective of challenge numbers
    challenge_intro()

    while True:
        # gets choice from user from challenge menu
        choice = challenge_menu_choice()

        if (choice < 0) or (choice > 4):
            # if choice was not on menu, note error
            print """\nPlease choose from the menu options.\n"""
        else:
            if choice == 0:
                # returns to birthday menu
                break
            elif choice == 1:
                # calculates and displays meaning for first challenge number
                first_chall = first_chall_calc(single_day_uno, single_month_uno)
                first_chall_meaning(first_chall)
            elif choice == 2:
                # calculates and displays meaning for second challenge number
                sec_chall = sec_chall_calc(single_day_uno, single_year_uno)
                sec_chall_meaning(sec_chall)
            elif choice == 3:
                # calculates and displays meaning for third challenge number (note that since user may not choose option 1 or 2, first and second challenge functions would have to be called here to calculate variabbles used in third challenge number)
                first_chall = first_chall_calc(single_day_uno, single_month_uno)
                sec_chall = sec_chall_calc(single_day_uno, single_year_uno)
                third_chall = third_chall_calc(first_chall, sec_chall)
                third_chall_meaning(third_chall)
            elif choice == 4:
                # calculates and displays meaning for fourth challenge number
                fourth_chall = fourth_chall_calc(single_month_uno, single_year_uno)
                fourth_chall_meaning(fourth_chall)


# definition of a function to execute within the birthday menu


def birthday_exec_repl(year, month, day):
    # calculate single digits master for year, month and day
    single_year_master = single_digit_master(year)
    single_month_master = single_digit_master(month)
    single_day_master = single_digit_master(day)

    # calculate single digits for year, month and day
    single_year_uno = single_digit_uno(year)
    single_month_uno = single_digit_uno(month)
    single_day_uno = single_digit_uno(day)

    while True:
        # get choice from user from birthday menu
        choice = birthday_menu_choice()

        if (choice < 0) or (choice > 4):
            # if choice was not on menu, note error
            print """\nPlease choose from the menu options.\n"""
        else:
            if choice == 0:
                # return to main menu
                break
            elif choice == 1:
                # calculate and display meaning for life path number
                life_path = life_path_calc(single_year_master, single_month_master, single_day_master)
                life_path_meaning(life_path)
            elif choice == 2:
                # calculate and display meaning for birth day number
                birth_day_meaning(single_day_master)
            elif choice == 3:
                # execute repl loop for challenge numbers, which takes it to challenge numbers menu
                challenge_exec_repl(single_day_uno, single_month_uno, single_year_uno)
            elif choice == 4:
                # calculate and display meaning for personal year number
                personal_year = pers_year_calc(single_day_uno, single_month_uno, single_year_uno, month, day)
                pers_year_meaning(personal_year)


# definition of a function to execute within the name menu


def name_exec_repl(last, middle, first):
    # concatenate full name (maybe use strip function if "0" used for blank names but it seems to not work)
    full_name = last + middle + first

    # calculate single digits master for first, middle and last names
    single_last_master = single_digit_master(name_calc(last))
    single_middle_master = single_digit_master(name_calc(middle))
    single_first_master = single_digit_master(name_calc(first))

    # separate consonants only of first, middle and last names
    cons_last_name = consonants(last, vowel)
    cons_middle_name = consonants(middle, vowel)
    cons_first_name = consonants(first, vowel)
    cons_full_name = consonants(full_name, vowel)

    # separate vowels only of first, middle and last names
    vow_last_name = vowels(last, vowel)
    vow_middle_name = vowels(middle, vowel)
    vow_first_name = vowels(first, vowel)

    # calculate single digits master of first, middle and last names by consonants only
    single_cons_last_master = single_digit_master(name_calc(cons_last_name))
    single_cons_middle_master = single_digit_master(name_calc(cons_middle_name))
    single_cons_first_master = single_digit_master(name_calc(cons_first_name))

    # calculate single digits master of first, middle and last names by vowels only
    single_vow_last_master = single_digit_master(name_calc(vow_last_name))
    single_vow_middle_master = single_digit_master(name_calc(vow_middle_name))
    single_vow_first_master = single_digit_master(name_calc(vow_first_name))

    while True:
        # gets choice from user from name menu
        choice = name_menu_choice()

        if (choice < 0) or (choice > 6):
            # if choice was not on menu, note error
            print """\nPlease choose from the menu options.\n"""
        else:
            if choice == 0:
                # returns to main menu
                break
            elif choice == 1:
                # calculates and display meaning for expression (destiny) number
                exp_dest = exp_calc(single_last_master, single_middle_master, single_first_master)
                exp_dest_meaning(exp_dest)
            elif choice == 2:
                # calculates and display meaning for soul urge number
                soul_urge = soul_urge_calc(single_vow_last_master, single_vow_middle_master, single_vow_first_master)
                soul_urge_meaning(soul_urge)
            elif choice == 3:
                # calculates and display meaning for personality number
                personality = personality_cal(single_cons_last_master, single_cons_middle_master, single_cons_first_master)
                personality_meaning(personality)
            elif choice == 4:
                # calculates and display meaning for hidden passion number
                hid_pass = pass_calc(full_name)
                hid_pass_meaning(hid_pass)
            elif choice == 5:
                # calculates and display meaning for karmic number
                karmic = karmic_calc(cons_full_name)
                karmic_meaning(karmic)
            elif choice == 6:
                corn_cap(first)


# definition of a function to execute within the compatibility menu


def compatibility_exec_repl(year, month, day, last, middle, first):
    # determines compatibility based on either life path number or expression number; however, since the calculations of these numbers for the individual are buried in the birthday and name menus, need to recompute those here

    # calculates single digits master for year, month and day
    single_year_master = single_digit_master(year)
    single_month_master = single_digit_master(month)
    single_day_master = single_digit_master(day)

    # calculates life path number
    life_path = life_path_calc(single_year_master, single_month_master, single_day_master)

    # calculates life path number to single digit
    life_path_uno = single_digit_uno(life_path)

    # calculates single digits master for first, middle and last names
    single_last_master = single_digit_master(name_calc(last))
    single_middle_master = single_digit_master(name_calc(middle))
    single_first_master = single_digit_master(name_calc(first))

    # calculates expression number
    exp_dest = exp_calc(single_last_master, single_middle_master, single_first_master)

    # calculates expression (destiny) number to single digit
    exp_dest_uno = single_digit_uno(exp_dest)

    # asks if individual has a partner in mind
    have_partner = ask_partner()

    if have_partner == "n":
        comp_gen(life_path_uno)
    else:
        while True:
            # get choice from user from compatibility menu
            choice = compatibility_menu_choice()

            if (choice < 0) or (choice > 2):
                # if choice was not on menu, note error
                print """\nPlease choose from the menu options.\n"""
            else:
                if choice == 0:
                    # return to main menu
                    break
                elif choice == 1:
                    partner_life_uno = partner_life_path(life_path)
                    comp_life_meaning(life_path_uno, partner_life_uno)
                elif choice == 2:
                    partner_exp_uno = partner_exp_dest(exp_dest)
                    comp_exp_meaning(exp_dest_uno, partner_exp_uno)


# definition of a function to execute the numerology program


def execute_repl():
    greeting()
    # ask user for birthday information
    year = ask_year("individual")
    month = ask_month("individual")
    day = ask_day(year, month, "individual")

    # ask user for birth name information
    last_name = clean_name(ask_last_name("birth"))
    middle_name = clean_name(ask_middle_name("birth"))
    # clean function strips name of all spaces so separating first_name variables so that it could be use for exit greeting
    first_name = ask_first_name("birth")
    clean_first_name = clean_name(first_name)

    #error occurs if middle name is blank so temporary fix
    # if middle_name == "":
    #     middle_name = "0"
    # else:
    #     middle_name

    # ask user for common (nick) name information, if applicable
    nick_name = ask_nick_name()
    if nick_name == "y":
        nick_last_name = clean_name(ask_last_name("nick"))
        nick_middle_name = clean_name(ask_middle_name("nick"))
        # clean function strips name of all spaces so separating first_name variables so that it could be use for exit greeting
        nick_first_name = ask_first_name("nick")
        clean_nick_first_name = clean_name(nick_first_name)
        # error occurs if middle name is blank so temporary fix
        # if nick_middle_name == "":
        #     nick_middle_name = "0"
        # else:
        #     nick_middle_name

    while True:
        # gets choice from user from main menu
        choice = main_menu_choice()

        if (choice < 1) and (choice > 5):
            print """\nPlease choose from the menu options.\n"""

        if choice == 1:
            # gets choice from user from birthday menu and repl within that menu
            birthday_exec_repl(year, month, day)
        elif choice == 2:
            # gets choice from user from name menu and repl within that menu based on birth name
            name_exec_repl(last_name, middle_name, clean_first_name)
        elif choice == 3:
            # gets choice from user from name menu and repl within that menu based on nick name
            name_exec_repl(nick_last_name, nick_middle_name, clean_nick_first_name)
        elif choice == 4:
            # gets choice from user from compatibility menu and repl within that menu
            compatibility_exec_repl(year, month, day, last_name, middle_name, clean_first_name)
        else:
            if nick_name == "y":
                print """\nHave a wonderful day with your numerical vibrations, {}. Namaste!\n""".format(nick_first_name.title())
            else:
                print """\nHave a wonderful day with your numerical vibrations, {}. Namaste!\n""".format(first_name.title())
            break

execute_repl()
