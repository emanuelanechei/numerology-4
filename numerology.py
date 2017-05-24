import meanings

import calcnprint


# definition of function to print introduction message


def greeting():
    # introduction message in numerology program
    print """\nWelcome to the nexus of numerology.\n
Numerology is the study of the numerical value of letters in words, names and birthdays.\n
It is similar to astrology, and often associated with the belief in the divine, mystical relationship between numbers (and their related vibrations) and one or more coinciding events.\n"""


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


# set list of vowels


vowel = ("a", "e", "i", "o", "u")


# definition of a function to display main menu


def main_menu_choice():
    print """\n     1 - Show numerology by birthday."""
    print """     2 - Show numerology by birth name."""
    print """     3 - Show numerology by common or nick name."""
    print """     4 - Show partner compatibility."""
    print """     5 - Create report of numerology results."""
    print """     6 - Exit the program.\n"""

    choice = raw_input("Choose from the menu options: ")

    return choice


# definition of a function to display birthday numerology menu


def birthday_menu_choice():
    print """\n     0 - Return to main menu."""
    print """     1 - Show life path number."""
    print """     2 - Show birth day number."""
    print """     3 - Show challenge number(s)."""
    print """     4 - Show personal year number.\n"""

    choice = raw_input("Choose from the menu options (return to main menu to exit): ")

    return choice


# definition of a function to display challenge numbbers menu


def challenge_menu_choice():
    print """\n     0 - Return to birthday main menu."""
    print """     1 - Show first challenge number."""
    print """     2 - Show second challenge number."""
    print """     3 - Show third challenge number."""
    print """     4 - Show fourth challenge number.\n"""

    choice = raw_input("Choose from the menu options: ")

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

    choice = raw_input("Choose from the menu options (return to main menu to exit): ")

    return choice


# definition of a function to display compatibility menu


def compatibility_menu_choice():
    print """\n     0 - Return to main menu."""
    print """     1 - Based on birthday."""
    print """     2 - Based on name.\n"""

    choice = raw_input("Choose from the menu options (return to main menu to exit): ")

    return choice


# definition of a function to execute within the challenge menu


def challenge_exec_repl(single_day_uno, single_month_uno, single_year_uno):
    # displays objective of challenge numbers
    meanings.challenge_intro()

    while True:
        # gets choice from user from challenge menu
        choice = challenge_menu_choice()

        if not choice.isdigit() or not ((int(choice) >= 0) and (int(choice) <= 4)):
            # if choice was not on menu, notes error
            print """\nPlease choose from the menu options.\n"""
        else:
            choice = int(choice)

            if choice == 0:
                # returns to birthday menu
                break
            elif choice == 1:
                # calculates and displays meaning for first challenge number
                first_chall = calcnprint.first_chall_calc(single_day_uno, single_month_uno)
                calcnprint.first_chall_meaning(first_chall)
            elif choice == 2:
                # calculates and displays meaning for second challenge number
                sec_chall = calcnprint.sec_chall_calc(single_day_uno, single_year_uno)
                calcnprint.sec_chall_meaning(sec_chall)
            elif choice == 3:
                # calculates and displays meaning for third challenge number (note that since user may not choose option 1 or 2, first and second challenge functions would have to be called here to calculate variabbles used in third challenge number)
                first_chall = calcnprint.first_chall_calc(single_day_uno, single_month_uno)
                sec_chall = calcnprint.sec_chall_calc(single_day_uno, single_year_uno)
                third_chall = calcnprint.third_chall_calc(first_chall, sec_chall)
                calcnprint.third_chall_meaning(third_chall)
            elif choice == 4:
                # calculates and displays meaning for fourth challenge number
                fourth_chall = calcnprint.fourth_chall_calc(single_month_uno, single_year_uno)
                calcnprint.fourth_chall_meaning(fourth_chall)


# definition of a function to execute within the birthday menu


def birthday_exec_repl(year, month, day):
    # calculates single digits master for year, month and day
    single_year_master = calcnprint.single_digit_master(year)
    single_month_master = calcnprint.single_digit_master(month)
    single_day_master = calcnprint.single_digit_master(day)

    # calculates single digits for year, month and day
    single_year_uno = calcnprint.single_digit_uno(year)
    single_month_uno = calcnprint.single_digit_uno(month)
    single_day_uno = calcnprint.single_digit_uno(day)

    while True:
        # gets choice from user from birthday menu
        choice = birthday_menu_choice()

        if not choice.isdigit() or not ((int(choice) >= 0) and (int(choice) <= 4)):
            # if choice was not on menu, notes error
            print """\nPlease choose from the menu options.\n"""
        else:
            choice = int(choice)

            if choice == 0:
                # returns to main menu
                break
            elif choice == 1:
                # calculates and displays meaning for life path number
                life_path = calcnprint.life_path_calc(single_year_master, single_month_master, single_day_master)
                meanings.life_path_meaning(life_path)
            elif choice == 2:
                # calculates and displays meaning for birth day number
                meanings.birth_day_meaning(single_day_master)
            elif choice == 3:
                # executes repl loop for challenge numbers, which takes it to challenge numbers menu
                challenge_exec_repl(single_day_uno, single_month_uno, single_year_uno)
            elif choice == 4:
                # calculates and displays meaning for personal year number
                personal_year = calcnprint.pers_year_calc(single_day_uno, single_month_uno, single_year_uno, month, day)
                meanings.pers_year_meaning(personal_year)


# definition of a function to execute within the name menu


def name_exec_repl(last, middle, first):
    # concatenates full name (maybe use strip function if "0" used for blank names but it seems to not work)
    full_name = last + middle + first

    # calculates single digits master for first, middle and last names
    single_last_master = calcnprint.single_digit_master(calcnprint.name_calc(last))
    single_middle_master = calcnprint.single_digit_master(calcnprint.name_calc(middle))
    single_first_master = calcnprint.single_digit_master(calcnprint.name_calc(first))

    # separates consonants only of first, middle and last names
    cons_last_name = calcnprint.consonants(last, vowel)
    cons_middle_name = calcnprint.consonants(middle, vowel)
    cons_first_name = calcnprint.consonants(first, vowel)
    cons_full_name = calcnprint.consonants(full_name, vowel)

    # separates vowels only of first, middle and last names
    vow_last_name = calcnprint.vowels(last, vowel)
    vow_middle_name = calcnprint.vowels(middle, vowel)
    vow_first_name = calcnprint.vowels(first, vowel)

    # calculates single digits master of first, middle and last names by consonants only
    single_cons_last_master = calcnprint.single_digit_master(calcnprint.name_calc(cons_last_name))
    single_cons_middle_master = calcnprint.single_digit_master(calcnprint.name_calc(cons_middle_name))
    single_cons_first_master = calcnprint.single_digit_master(calcnprint.name_calc(cons_first_name))

    # calculates single digits master of first, middle and last names by vowels only
    single_vow_last_master = calcnprint.single_digit_master(calcnprint.name_calc(vow_last_name))
    single_vow_middle_master = calcnprint.single_digit_master(calcnprint.name_calc(vow_middle_name))
    single_vow_first_master = calcnprint.single_digit_master(calcnprint.name_calc(vow_first_name))

    while True:
        # gets choice from user from name menu
        choice = name_menu_choice()

        if not choice.isdigit() or not ((int(choice) >= 0) and (int(choice) <= 6)):
            # if choice was not on menu, notes error
            print """\nPlease choose from the menu options.\n"""
        else:
            choice = int(choice)

            if choice == 0:
                # returns to main menu
                break
            elif choice == 1:
                # calculates and displays meaning for expression (destiny) number
                exp_dest = calcnprint.exp_calc(single_last_master, single_middle_master, single_first_master)
                meanings.exp_dest_meaning(exp_dest)
            elif choice == 2:
                # calculates and displays meaning for soul urge number
                soul_urge = calcnprint.soul_urge_calc(single_vow_last_master, single_vow_middle_master, single_vow_first_master)
                meanings.soul_urge_meaning(soul_urge)
            elif choice == 3:
                # calculates and displays meaning for personality number
                personality = calcnprint.personality_cal(single_cons_last_master, single_cons_middle_master, single_cons_first_master)
                meanings.personality_meaning(personality)
            elif choice == 4:
                # calculates and displays meaning for hidden passion number
                hid_pass = calcnprint.pass_calc(full_name)
                meanings.hid_pass_meaning(hid_pass)
            elif choice == 5:
                # calculates and displays meaning for karmic number
                karmic = calcnprint.karmic_calc(cons_full_name)
                meanings.karmic_meaning(karmic)
            elif choice == 6:
                calcnprint.corn_cap(first)


# definition of a function to execute within the compatibility menu


def compatibility_exec_repl(year, month, day, last, middle, first):
    # determines compatibility based on either life path number or expression number; however, since the calculations of these numbers for the individual are buried in the birthday and name menus, need to recompute those here

    # calculates single digits master for year, month and day
    single_year_master = calcnprint.single_digit_master(year)
    single_month_master = calcnprint.single_digit_master(month)
    single_day_master = calcnprint.single_digit_master(day)

    # calculates life path number
    life_path = calcnprint.life_path_calc(single_year_master, single_month_master, single_day_master)

    # calculates life path number to single digit
    life_path_uno = calcnprint.single_digit_uno(life_path)

    # calculates single digits master for first, middle and last names
    single_last_master = calcnprint.single_digit_master(calcnprint.name_calc(last))
    single_middle_master = calcnprint.single_digit_master(calcnprint.name_calc(middle))
    single_first_master = calcnprint.single_digit_master(calcnprint.name_calc(first))

    # calculates expression number
    exp_dest = calcnprint.exp_calc(single_last_master, single_middle_master, single_first_master)

    # calculates expression (destiny) number to single digit
    exp_dest_uno = calcnprint.single_digit_uno(exp_dest)

    # asks if individual has a partner in mind
    have_partner = calcnprint.ask_partner()

    if have_partner == "n":
        meanings.comp_gen(life_path_uno)
    else:
        while True:
            # gets choice from user from compatibility menu
            choice = compatibility_menu_choice()

            if not choice.isdigit() or not ((int(choice) >= 0) and (int(choice) <= 2)):
                # if choice was not on menu, notes error
                print """\nPlease choose from the menu options.\n"""
            else:
                choice = int(choice)
                
                if choice == 0:
                    # returns to main menu
                    break
                elif choice == 1:
                    partner_life_uno = calcnprint.partner_life_path(life_path)
                    life_paths = [life_path_uno, partner_life_uno]
                    life_paths.sort()
                    print meanings.lp_comp_dict[tuple(life_paths)]
                    #meanings.comp_life_meaning(life_path_uno, partner_life_uno)
                elif choice == 2:
                    partner_exp_uno = calcnprint.partner_exp_dest(exp_dest)
                    exp_dests = [exp_dest_uno, partner_exp_uno]
                    exp_dests.sort()
                    print meanings.ed_comp_dict[tuple(exp_dests)]
                    #meanings.comp_exp_meaning(exp_dest_uno, partner_exp_uno)


# definition of a function to execute the numerology program


def execute_repl():
    greeting()
    # asks user for birthday information
    year = calcnprint.ask_year("individual")
    month = calcnprint.ask_month("individual")
    day = calcnprint.ask_day(year, month, "individual")

    # asks user for birth name information
    last_name = calcnprint.clean_name(calcnprint.ask_name("birth", "last"))
    middle_name = calcnprint.clean_name(calcnprint.ask_name("birth", "middle"))
    # clean function strips name of all spaces so separating first_name variables so that it could be use for exit greeting
    first_name = calcnprint.ask_name("birth", "first")
    clean_first_name = calcnprint.clean_name(first_name)

    # asks user for common (nick) name information, if applicable
    nick_name = ask_nick_name()
    if nick_name == "y":
        nick_last_name = calcnprint.clean_name(calcnprint.ask_name("nick", "last"))
        nick_middle_name = calcnprint.clean_name(calcnprint.ask_name("nick", "middle"))
        # clean function strips name of all spaces so separating first_name variables so that it could be use for exit greeting
        nick_first_name = calcnprint.ask_name("nick", "first")
        clean_nick_first_name = calcnprint.clean_name(nick_first_name)
    else:
        nick_last_name = ""
        nick_middle_name = ""
        nick_first_name = ""
        nick_first_name = ""
        clean_nick_first_name = ""

    while True:
        # gets choice from user from main menu
        choice = main_menu_choice()

        if not choice.isdigit() or not ((int(choice) >= 1) and (int(choice) <= 6)):
            # if choice is not on menu, notes error
            print """\nPlease choose from the menu options.\n"""
        else:
            choice = int(choice)

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
            elif choice == 5:
                # creates file object to write output of results of various numerology numbers and meanings with only generic compatibility chart since details of partner is in "child" menu
                calcnprint.numerology_rpt(nick_name, first_name, nick_first_name, year, month, day, last_name, middle_name, clean_first_name, nick_last_name, nick_middle_name, clean_nick_first_name, vowel)
            else:
                if nick_name == "y":
                    print """\nHave a wonderful day with your numerical vibrations, {}. Namaste!\n""".format(nick_first_name.title())
                else:
                    print """\nHave a wonderful day with your numerical vibrations, {}. Namaste!\n""".format(first_name.title())
                break

execute_repl()
