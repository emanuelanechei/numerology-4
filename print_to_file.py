import sys
import clean_numerology
import meanings


# definition of a function to create file output for results of numerology


def numerology_rpt(nick_name, first_name, nick_first_name, year, month, day, last_name, middle_name, clean_first_name, nick_last_name, nick_middle_name, clean_nick_first_name, vowel):
    # creates file to write various results of numerology calculations
    with open("report.txt", "w") as file:
        # redirecting standard output point to output file so that subsequent calls to print will write to output file
        sys.stdout = file

        # writes to file introduction with individual's name
        if nick_name == "y":
            file.write("{}, the following is your numerology report:\n".format(nick_first_name.title()))
        else:
            file.write("{}, the following is your numerology report:\n".format(first_name.title()))

        # calculates single digits master for year, month and day
        single_year_master = clean_numerology.single_digit_master(year)
        single_month_master = clean_numerology.single_digit_master(month)
        single_day_master = clean_numerology.single_digit_master(day)

        # calculates single digits for year, month and day
        single_year_uno = clean_numerology.single_digit_uno(year)
        single_month_uno = clean_numerology.single_digit_uno(month)
        single_day_uno = clean_numerology.single_digit_uno(day)

        # calculates and display meaning for life path number
        life_path = clean_numerology.life_path_calc(single_year_master, single_month_master, single_day_master)
        file.write(meanings.life_path_meaning(life_path))

        # calculates and display meaning for birth day number
        file.write(meanings.birth_day_meaning(single_day_master))

        # calculates and displays meanings for challenge numbers
        file.write(meanings.challenge_intro())

        # calculates and displays meaning for first challenge number
        first_chall = clean_numerology.first_chall_calc(single_day_uno, single_month_uno)
        file.write(meanings.first_chall_meaning(first_chall))

        # calculates and displays meaning for second challenge number
        sec_chall = clean_numerology.sec_chall_calc(single_day_uno, single_year_uno)
        file.write(meanings.sec_chall_meaning(sec_chall))

        # calculates and displays meaning for third challenge number (note that since user may not choose option 1 or 2, first and second challenge functions would have to be called here to calculate variabbles used in third challenge number)
        third_chall = clean_numerology.third_chall_calc(first_chall, sec_chall)
        file.write(meanings.third_chall_meaning(third_chall))

        # calculates and displays meaning for fourth challenge number
        fourth_chall = clean_numerology.fourth_chall_calc(single_month_uno, single_year_uno)
        file.write(meanings.fourth_chall_meaning(fourth_chall))

        # calculate and display meaning for personal year number
        personal_year = clean_numerology.pers_year_calc(single_day_uno, single_month_uno, single_year_uno, month, day)
        file.write(meanings.pers_year_meaning(personal_year))

        # concatenates full name (maybe use strip function if "0" used for blank names but it seems to not work)
        full_name = last_name + middle_name + clean_first_name

        # calculates single digits master for first, middle and last names
        single_last_master = clean_numerology.single_digit_master(clean_numerology.name_calc(last_name))
        single_middle_master = clean_numerology.single_digit_master(clean_numerology.name_calc(middle_name))
        single_first_master = clean_numerology.single_digit_master(clean_numerology.name_calc(clean_first_name))

        # separates consonants only of first, middle and last names
        cons_last_name = clean_numerology.consonants(last_name, vowel)
        cons_middle_name = clean_numerology.consonants(middle_name, vowel)
        cons_first_name = clean_numerology.consonants(clean_first_name, vowel)
        cons_full_name = clean_numerology.consonants(full_name, vowel)

        # separates vowels only of first, middle and last names
        vow_last_name = clean_numerology.vowels(last_name, vowel)
        vow_middle_name = clean_numerology.vowels(middle_name, vowel)
        vow_first_name = clean_numerology.vowels(clean_first_name, vowel)

        # calculates single digits master of first, middle and last names by consonants only
        single_cons_last_master = clean_numerology.single_digit_master(clean_numerology.name_calc(cons_last_name))
        single_cons_middle_master = clean_numerology.single_digit_master(clean_numerology.name_calc(cons_middle_name))
        single_cons_first_master = clean_numerology.single_digit_master(clean_numerology.name_calc(cons_first_name))

        # calculates single digits master of first, middle and last names by vowels only
        single_vow_last_master = clean_numerology.single_digit_master(clean_numerology.name_calc(vow_last_name))
        single_vow_middle_master = clean_numerology.single_digit_master(clean_numerology.name_calc(vow_middle_name))
        single_vow_first_master = clean_numerology.single_digit_master(clean_numerology.name_calc(vow_first_name))

        # calculates and displays meaning for expression (destiny) number
        exp_dest = clean_numerology.exp_calc(single_last_master, single_middle_master, single_first_master)
        file.write(meanings.exp_dest_meaning(exp_dest))

        # calculates and displays meaning for soul urge number
        soul_urge = clean_numerology.soul_urge_calc(single_vow_last_master, single_vow_middle_master, single_vow_first_master)
        file.write(meanings.soul_urge_meaning(soul_urge))

        # calculates and displays meaning for personality number
        personality = clean_numerology.personality_cal(single_cons_last_master, single_cons_middle_master, single_cons_first_master)
        file.write(meanings.personality_meaning(personality))

        # calculates and displays meaning for hidden passion number
        hid_pass = clean_numerology.pass_calc(full_name)
        file.write(meanings.hid_pass_meaning(hid_pass))

        # calculates and displays meaning for karmic number
        karmic = clean_numerology.karmic_calc(cons_full_name)
        file.write(meanings.karmic_meaning(karmic))

        # displays meanings for cornerstone and capstone
        file.write(meanings.corn_cap(clean_first_name))

        if nick_name == "y":
            # writes to file introduction that following section relates to the nick name
            file.write("The following section represents the various numbers as it relates to your common (nick) name. \nWhile the related numbers as it relates to your birth name represents your overall destiny, the numbers as it relates to your common (nick) name represents how you present yourself or how others perceive you.\n")

            # concatenates full name (maybe use strip function if "0" used for blank names but it seems to not work)
            nick_full_name = nick_last_name + nick_middle_name + clean_nick_first_name

            # calculates single digits master for first, middle and last names
            single_nick_last_master = clean_numerology.single_digit_master(clean_numerology.name_calc(nick_last_name))
            single_nick_middle_master = clean_numerology.single_digit_master(clean_numerology.name_calc(nick_middle_name))
            single_nick_first_master = clean_numerology.single_digit_master(clean_numerology.name_calc(clean_nick_first_name))

            # separates consonants only of first, middle and last names
            cons_nick_last_name = clean_numerology.consonants(nick_last_name, vowel)
            cons_nick_middle_name = clean_numerology.consonants(nick_middle_name, vowel)
            cons_nick_first_name = clean_numerology.consonants(clean_nick_first_name, vowel)
            cons_nick_full_name = clean_numerology.consonants(nick_full_name, vowel)

            # separates vowels only of first, middle and last names
            vow_nick_last_name = clean_numerology.vowels(nick_last_name, vowel)
            vow_nick_middle_name = clean_numerology.vowels(nick_middle_name, vowel)
            vow_nick_first_name = clean_numerology.vowels(clean_nick_first_name, vowel)

            # calculates single digits master of first, middle and last names by consonants only
            single_cons_nick_last_master = clean_numerology.single_digit_master(clean_numerology.name_calc(cons_nick_last_name))
            single_cons_nick_middle_master = clean_numerology.single_digit_master(clean_numerology.name_calc(cons_nick_middle_name))
            single_cons_nick_first_master = clean_numerology.single_digit_master(clean_numerology.name_calc(cons_nick_first_name))

            # calculates single digits master of first, middle and last names by vowels only
            single_vow_nick_last_master = clean_numerology.single_digit_master(clean_numerology.name_calc(vow_nick_last_name))
            single_vow_nick_middle_master = clean_numerology.single_digit_master(clean_numerology.name_calc(vow_nick_middle_name))
            single_vow_nick_first_master = clean_numerology.single_digit_master(clean_numerology.name_calc(vow_nick_first_name))

            # calculates and displays meaning for expression (destiny) number
            exp_dest = clean_numerology.exp_calc(single_nick_last_master, single_nick_middle_master, single_nick_first_master)
            file.write(meanings.exp_dest_meaning(exp_dest))

            # calculates and displays meaning for soul urge number
            soul_urge = clean_numerology.soul_urge_calc(single_vow_nick_last_master, single_vow_nick_middle_master, single_vow_nick_first_master)
            file.write(meanings.soul_urge_meaning(soul_urge))

            # calculates and displays meaning for personality number
            personality = clean_numerology.personality_cal(single_cons_nick_last_master, single_cons_nick_middle_master, single_cons_nick_first_master)
            file.write(meanings.personality_meaning(personality))

           # calculates and displays meaning for hidden passion number
            hid_pass = clean_numerology.pass_calc(nick_full_name)
            file.write(meanings.hid_pass_meaning(hid_pass))

            # calculates and displays meaning for karmic number
            karmic = clean_numerology.karmic_calc(cons_nick_full_name)
            file.write(meanings.karmic_meaning(karmic))

            # displays meanings for cornerstone and capstone
            file.write(meanings.corn_cap(clean_nick_first_name))

            # calculates life path number to single digit for compatibility purposes
            life_path_uno = clean_numerology.single_digit_uno(life_path)
            file.write(meanings.comp_gen(life_path_uno))
