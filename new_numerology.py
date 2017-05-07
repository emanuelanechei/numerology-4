# definition of function to print introduction message


def greeting():
    print """\nWelcome to the nexus of numerology.\n
Numerology is the study of the numerical value of letters in words, names and birthdays.\n
It is similar to astrology, and often associated with the belief in the divine, mystical relationship between numbers and one or more coinciding events.\n"""

#greeting()


# definition of function for birth year


def ask_year():
    while True:
        year = raw_input("Input your year of birth: ")
        if not year.isdigit():
            print "Please input the year based on the Gregorian calendar."
        else:
            year = int(year)

        return year

#year = ask_year()


# definition of function for birth month


def ask_month():
    while True:
        month = raw_input("Input your month (1-12) of birth: ")
        if not month.isdigit():
            print "Please input the numerical value of the month."
        elif (int(month) < 1) or (int(month) > 12):
            print "That may be a month on Mars, but not on Earth!"
        else:
            month = int(month)

        return month

#month = ask_month()


# definition of function for birth day


def ask_day(year, month):
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
                # for leap year, if divisile by 100 but not 400, then not leap year. otherwise, divisible by 4.
                print "You took a flying leap off of Pluto!"
            elif (month == 2) and ((year % 4 != 0) or ((year % 4 == 0) and (year % 100 == 0))) and ((day < 1) or (day > 28)):
                print "That may be a day on Venus, but not on Earth!"

        return day

#day = ask_day(year, month)


# definition of function to calculate various items to single digit or master number


def single_digit_master(single_digit):
    while True:
        if (single_digit < 10) or (single_digit == 11) or (single_digit == 22):
            single_digit_master = single_digit
            break
        else:
            partial_sum = 0
            for number in str(single_digit):
                partial_sum += int(number)
            single_digit = partial_sum

    return single_digit_master

#single_year_master = single_digit_master(year)
#single_month_master = single_digit_master(month)
#single_day_master = single_digit_master(day)

#print single_year_master, single_month_master, single_day_master


# definition of function to calculate various items to single digit


def single_digit_uno(single_digit):
    while True:
        if (single_digit < 10):
            single_digit_uno = single_digit
            break
        else:
            partial_sum = 0
            for number in str(single_digit):
                partial_sum += int(number)
            single_digit = partial_sum

    return single_digit_uno

#single_year_uno = single_digit_uno(year)
#single_month_uno = single_digit_uno(month)
#single_day_uno = single_digit_uno(day)

#print single_year_uno, single_month_uno, single_day_uno


# definition of function to calculate life path number


def life_path_calc(single_year_master, single_month_master, single_day_master):
    life_path_raw = single_year_master + single_month_master + single_day_master
    life_path = single_digit_master(life_path_raw)

    return life_path

#life_path = life_path_calc(single_year_master, single_month_master, single_day_master)


# definition of a function to display life path meaning


def life_path_meaning(life_path):
    print """\nYour life path number is {}. Life path number defines limitations or possibilities in life and gives insights to the direction you'll take and the decisions that will affect the life you lead.\n""".format(life_path)

    if life_path == 1:
        print """\nYou are all about power! Strong and determined individuals carry this life path number. They are often leaders in business and have great personal ambition.\n
They are motivated by personal success and competition. Highly independent by nature - the person with the 1 life path is often very innovative and creative in their thinking. Highly analytical and very sharp, they are natural problem solvers.\n
Number 1s who stray from their paths often end up in clingy co-dependent relationships.\n"""
    elif life_path == 2:
        print """\nYou are all about love. People with life path 2 love to find and maintain balance. They are natural peacemakers and tend to be drawn towards service to others.\n
Often they are too self-sacrificing and struggle to find balance in life when it comes to valuing themselves as much as others. People with this life path numer tend to be somewhat reserved and quiet. They have excellent listening skills and tend to be very drwan to music.\n
It is very important for them to get out and socialize. A number 2 who is isolated courts pessimism, lethargy and depression.\n"""
    elif life_path == 3:
        print """\nYou are all about performance! This is the life path numer of creative people who are very expressive and unique. They are skilled communicators, naturally charming and attractive to others. They know how to convey ideas.\n
3 people tend to be very optimistic and hopeful people who encourage and nourish that quality in others. They tend to be very energetic and busy - to the point they may wear themselves out.\n
Number 3s stray off their life path by giving up their dreams and talents. Many escape into drug abuse or promiscuity to avoid hearing the nagging voice of their true calling to express their talents.\n"""
    elif life_path == 4:
        print """\nYou are all about stability! This is the life path number of the pragmatic organizer - the one who builds, constructs, works hard and who is very diligent and persistent in his efforts.\n
People with this life path are considered "practical" and down to earth. Many workaholic types have the 4 as a life path numer. People with this life path tend to prefer to follow established rules and believe in order. They don't tend to like surprises and are rather meticulous.\n
However, self-sacrificing number 4s often demand too much, both of themselves and others, and develop reputations as martyrs or tyrants. Their willpower and stubbornness can also be interpreted as greed and selfishness.\n"""
    elif life_path == 5:
        print """\nYou are all about freedom! Those with a 5 life path are gregarious, fun-loving people who love to be surrounded by others. The 5 life path is a bit free-spirited and enjoys adventure, travel, and diversity.\n
People with this life path often thrive in careers that involve travel or working aorad. They do not do well in office settings or any place that liits their freedom and creative expression.\n
However, 5s tend to be very self-absorbed and unaware of the effect of their actions on other people. As other people often feel tricked or fooled by number 5s, experiencing a series of broken relationships is also often a part of their path. People with this life path sometimes have difficulty with discipline or finishing what they started.\n"""
    elif life_path == 6:
        print """\nYou are all about nurturing. Those with this life path of 6 are hard workers, tend to have a variety of skills and interests and are very "direct" in their approach. Sometimes prone to being too hard on themselves, they will push themselves to their limits.\n
6 people are typically very organized and efficient and dislike waste - whether it be wasted time or resources. Those with this life path are sometimes seen as strict or sharp, but in actuality, they do have the best interest s of others at heart and love to see people reach their potentical. People with this life path make good personal trainers, drill instructors, etc. ecause they can push others to their personal limits in ways that are both compassionate and motivating.\n
6s that find themselves enslaved to an addicted or mentally ill partner might not be following their true path, as this is a sign that they have become enablers, rather than healers of the diseases.\n"""
    elif life_path == 7:
        print """\nYou are all about knowledge! 7 is the life path numer of the Seeker. People with this life path numer are drawn to the igger mysteries in life and are always looking for a larger purpose behind their circumstances.\n
7s are often psychic or extremely intuitive by nature with an innate aility to see to the heart and soul of others and situations. 7 people tend to love people, but are also very independent, requiring a great deal of solitary time to recharge their batteries. 7 people can be prone to being slow movers and procrastinators and need to work to keep their motivation levels up.\n
A sign that a number 7 has strayed completely off his or her life path is a complete withdrawal from society. In this case, the troubled 7 should try to recognize his or her original ambitions to improve the world through the application of wisdom.\n"""
    elif life_path == 8:
        print """\nYou are all about wealth. 8 is the life path of the natural born leader. These are people who are often very good at business and attracting wealth and favors. 8 people are often visionaries and capable of great things because they can also do the hard work required to make thier visions a reality.\n
8 people are very capable and inspiring leadrs, and people are compelled to follow their lead or be left behind. 8s do etter when they don't let their amitions get the better of their compassionate side - doing so can lead to greed and accumulation of wealth for less noble reasons.\n
Sometimes the pursuit of riches becomes more important than personal relationships and cost them their personal relationships, morality and popularity.\n"""
    elif life_path == 9:
        print """\nYou are all about spirituality. Life path 9 is the life path of the humanitarian. A natural orn leader by nature, you are compelled to lead and to serve. Your high ideals give you a strong desire to improve the lives of others.\n
You are innovative, visionary, and good at implementing new concepts and ideas. People with this life path sometimes struggle with disappointment when they can't live up to their high ideals. There is a need to learn to accept themselves more because when they do, they are capale of great things.\n
These sophisticated individuals are very selfless souls and are often patient, trustworthy, and honorable from the very beginning to the end of their lives. Sometimes a 9s lofty ideals are presented in a manner that others find absurd. Part of a 9s life path is to express spiritual principles through actions, rather than through preaching or proselytizing.\n"""
    elif life_path == 11:
        print """\nYou are about enlightenment. Those with this life path numer are extremely intuitive and feel a strong connection with others, sometimes to the point that it overwhelms their emotions.\n
11 people are very visionary and tend to be great thinkers. Solutions to prolems seem to come to them with very little effort and sometimes they don't understand how gifted they are at seeing what is "hidden" or elusive to others.\n
Many of them are "wounded healers" who at some point in their life suffer a devastating experience that propels them on the search for spirituality. However, along with these situations, usually comes a lot of toxic emotional baggage and harsh inner critic. It takes many 11s their entire life to rid themselves of the 'chip on their shoulder' and achieve enlightenment.\n"""
    else:
        print """\nYou are a master builder. The strongest of the life path numers, the 22 carries great potential, ut also great weight and responsibility. This card represents those who can e master uilders and visionaries, who can rally around a cause and bring people together for the common good.\n
Those with this life path often face weighty decisions at several points in their life where they must emrace the crossroads with confidence and make a choice. Those who are not fully in tune with this higher viration may find they struggle with choice in life and must work to take the path that challenges them over the path of least resistence. Sometimes they display what looks like insensitivity but actually they are just very focused on their goals. This is part of a spiritual directive to be detached from objects and the outcomes of events.\n
22 life path people who push themselves and embrace change can live truly astounding, creative lives.\n"""

#life_path_meaning(life_path)


# definition of function to display birth day number


def birth_day_meaning(single_day_master):
    print """\nYour birth day number is {}. Birth day number defines your very special talent or strength that greatly facilitates the fulfillment of your destiny.\n""".format(single_day_master)

    if single_day_master == 1:
        print """\nYour birth day number is 1. This birth day signifies natural born leaders, those with a lot of drive and initiative.\n
One people are ambitious, hard working, and often very career focused. One people have a keen intelligence and are quick learners who are able to do things on a grand scale.\n"""
    elif single_day_master == 2:
        print """\nTwo people are very balanced and tend to be natural peace keepers and diplomats. Natural negotiators, two people dislike conflict and will work hard to make compromises that benefit everyone.\n
Two people love to do important things behind the scenes and tend to have a good blend of both creative and analytical skills.\n"""
    elif single_day_master == 3:
        print """\nThree people are natural artists and love to express themselves creatively in a variety of forms. Three people are inspiring and display greath enthusiasm.\n
Three people have great imagination and vision and are also sharp and able to pick up on subtle details.\n"""
    elif single_day_master == 4:
        print """\nFour people are very hard-working and diligent. They are those who build a strong foundation and like structure and stability.\n
Loyal and genuinely honest, four people find others trust and rely upon their quiet strength and strong common sense approach to life.\n"""
    elif single_day_master == 5:
        print """\nFive people are your movers and shakers who long for adventure and new experience. Five people love and embrace diversity and require a lot of changes to keep them motivated and inspired.\n
Five people can be prone to carelessness at times, but their deep love of adventure and naturally keep social skills make them a joy to know - 'never a dull moment' as the saying goes.\n"""
    elif single_day_master == 6:
        print """\nSix people work hard to walk the 'middle ground' in life and feel the need for balance weighing on them quite often. Naturally artistic and expressive, but highly sensitive, six people tend to be very vulnerable to criticism and require a lot of positive reinforcement in life to keep them motivated.\n
They are naturally good at working for compromise, but have a strong sense of duty and don't tolerate excuses or 'victim' mentality in others. 'If they can do it, you can too' is their motto, but they are always eager to extend themselves to encourage and help others find their own inner strength.\n"""
    elif single_day_master == 7:
        print """\nSeven people are your natural born seekers and philosophers, those who seek truth and higher wisdom in all experiences Seven people tend to have a naturally strong intuition, but often struggle with their emotions which can sometimes cloud their judgment unless they learn to work through their emotional sensitivities with honesty.\n
Seven people are often highly intellectual as well and need to learn to balance that with their deep emotions so that they don't become cynical or detached from others.\n"""
    elif single_day_master == 8:
        print """\nEight people are daring and bold, usually naturally good in business, and they have a knack for making or acquiring money. Eight people are very motivated by success and are quite competitive.\n
They are also prone to being very self-confident, practical and efficient which lends to others trusting them with their business. Eight people are often seen as 'lucky' or having lucky breaks in life - but this is typically due to a natural drive and persistence that helps them attract what they want/need for success.\n"""
    elif single_day_master == 9:
        print """\nNine people are compassionate, dreamy and idealistic in nature. They are highly creative and often devote themselves to life-long learning. Many people with multiple degrees will have this number; they are never 'finished' or 'masters' as they embrace continued growth and personal expansion.\n
Nine people are visionaries who do best when they learn to assert themselves and master their insecurities. Worldly, creative and ever expansive, nine people often appear larger than life.\n"""
    elif single_day_master == 11:
        print """\nPeople with master number 11 are exceptionally intuitive and are often naturally drawn to the healing arts. 11 people are compelled with a strong drive towards service to others.\n
Highly sensitive, a dreamer, 11 people have to work hard to stay motivated and take action on their loftier goals.\n"""
    else:
        print """\nPeople with master number 22 are great builders and organizers. This number means you are gifted with the natural ability to not only visualize a plan but to see hte actual result ahead of time.\n
You are both a 'seer and a doer' and when you properly apply yourself, can see through from start to finish with relative ease. Your perception is keep and you have the right blend of idealism and practicalithy that can take you far.\n"""

#birth_day_meaning(single_day_master)


# definition of function to display challenge number meaning


def chall_meaning(challenge):
    if challenge == 0:
        print """\nThe zero challenge number tends to indicate no one specific area or challenge being greater than others. It can also mean a sort of mixed bag when it comes to minor challenges, but these are all designed to help you find your strength.\n
Zero challenges are more about developing one's strengths and having confidence in your abilities - becoming more well-rounded.\n"""
    elif challenge == 1:
        print """\nThe challenge with one is learning to exert your independence and speak out authentically. One people tend ot struggle with the need for approval from others from which they base their own sense of self-worth.\n
The challenge is to value oneself enough to be unique.\n"""
    elif challenge == 2:
        print """\nPeople with this challenge struggle with balance emotionally. They take criticism very personally and struggle to assert themselves.\n
People with this challenge often shirk responsibility because they don't want the pressure of others depending on them or because they are convinced that they can't handle it. People with this challenge in full force tend to shrink back a lot.\n"""
    elif challenge == 3:
        print """\nPeople with a 3 challenge number tend to have difficulty finishing what they start. They tend to multi-task in ways that are not effective and have many unfinished projects and goals that they struggle to reach.\n
Three people also tend to go on the defensive easily or 'react' to situations rather than think them through. They have difficulty expressing themselves at times in ways that are healthy and productive.\n"""
    elif challenge == 4:
        print """\nThis challenge has a lot to do with procrastination and not working hard enough to reach one's goals. Often this challenge can speak of going for the path of least resistance rather than really pushing your limits.\n
When the 4 is your challenge number, you are being pushed to be more assertive and efficient in your work habits.\n"""
    elif challenge == 5:
        print """\nThe 5 as a challenge indicates a high degree of impulsiveness and reckless behavior. The 5 is the number for freedom and adventure, but as a challenge, it can indicate a need to tone it down a bit and to attain some discipline and foresight.\n"""
    elif challenge == 6:
        print """\nPeople with a 6 challenge struggle with perfectionism. They demand too much of themselves and often those around them. As a result, they can come off as cynical, too authoritarian, and too critical.\n
People with this challenge need to learn to lighten up a bit, and unconditional love and acceptance of both self and others are their lessons.\n"""
    elif challenge == 7:
        print """\nUnexpressed emotions, difficulty accpeing concepts that defy 'norms,' and being too overly analytical can be themes of the 7 challenge number.\n
People with this challenge tend to be overly anayltical, dismissing anything that does not coincide with their own sense of logic. As a result, people with a 7 challenge are not as open-minded or open to new experiences as they could or should be.\n"""
    else:
        print """\nMaterialism above all else tends to be the theme of the 8 challenge number. People with this challenge give too much importance to material affairs and may rely upon social status and money to provide their sense of self-worth or value.\n
It can be tempting for people with this challenge to resort to less than scrupulous tactics in their business ventures, and they need to work to better balance the material world with their spiritual side.\n"""


# definition of function to introduce challenge numbers


def challenge_intro():
    print """\nChallenge numbers define four life cycles and the related challenges that one has to work to grow through, tendencies and obstacles that will pop up during those cycles. When faced with honesty, these numbers can lend great insight into areas for self improvement and personal growth.\n
Four numbers represent: 1) from birth to approximately age 35; 2) from 35 to approximately 60; 3) primary challenge that one faces throughout life; and 4) from 60 to end of life.\n"""

#challenge_intro()


# definition of function to calculate first challenge number


def first_chall_calc(single_day_uno, single_month_uno):
    first_chall = abs(single_day_uno - single_month_uno)

    return first_chall

#first_chall = first_chall_calc(single_day_uno, single_month_uno)


# definition of function to display first challenge meaning


def first_chall_meaning(first_chall):
    print """\nYour first challenge number is {}, which is from birth to approximately age 35.\n""".format(first_chall)
    chall_meaning(first_chall)

#first_chall_meaning(first_chall)


# definition of function to calculate second challenge number


def sec_chall_calc(single_day_uno, single_year_uno):
    sec_chall = abs(single_year_uno - single_day_uno)

    return sec_chall

#sec_chall = sec_chall_calc(single_day_uno, single_year_uno)


# definition of function to display second challenge meaning


def sec_chall_meaning(sec_chall):
    print """\nYour second challenge number is {}, which is from approximately age 35 to approximately age 60.\n""".format(sec_chall)
    chall_meaning(sec_chall)

#sec_chall_meaning(sec_chall)


# definition of function to calculate third challenge number


def third_chall_calc(first_chall, sec_chall):
    third_chall = abs(sec_chall - first_chall)

    return third_chall

#third_chall = third_chall_calc(first_chall, sec_chall)


# definition of function to display third challenge meaning


def third_chall_meaning(third_chall):
    print """\nYour third challenge number is {}, which represents the primary challenge that one faces throughout life.\n""".format(third_chall)
    chall_meaning(third_chall)

#third_chall_meaning(third_chall)


# definition of function to calculate fourth challenge number


def fourth_chall_calc(single_month_uno, single_year_uno):
    fourth_chall = abs(single_year_uno - single_month_uno)

    return fourth_chall

#fourth_chall = fourth_chall_calc(single_month_uno, single_year_uno)


# definition of function to display fourth challenge meaning


def fourth_chall_meaning(fourth_chall):
    print """\nYour fourth (and final) challenge number is {}, which from approximately age 60 to end of life.\n""".format(fourth_chall)
    chall_meaning(fourth_chall)

#fourth_chall_meaning(fourth_chall)


# definition of function to calculate personal year number


from datetime import date


def pers_year_calc(single_day_uno, single_month_uno, single_year_uno, month, day):
    single_current_uno = single_digit_uno(date.today().year)
    personal_year_raw = single_current_uno + single_month_uno + single_day_uno
    personal_year = single_digit_uno(personal_year_raw)
    today = date.today()
    birth_raw = date(today.year, month, day)

    if today < birth_raw:
        personal_year = personal_year - 1
    else:
        personal_year

    return personal_year

#personal_year = pers_year_calc(single_day_uno, single_month_uno, single_year_uno, month, day)


# definition of function to display personal year meaning


def pers_year_meaning(personal_year):
    print """\nYour personal year number is {}. Personal year number gives insight into what surrounds you for this year cycle and represents various themes and events that will likely occur for you during the year (from your birthday until your next birthday).\n""".format(personal_year)

    if personal_year == 1:
        print """\nThe first of the 9 year cycle, a personal year 1 means a year of major changes and a need to make some decisions and work to embrace the opportunities coming rather than resisting change. A good time to focus on personal growth and making positive changes on that front as well.\n
Avoid procrastination this year as it will have more detrimental effects than usual. Conversely, determination truly pays long-term for efforts made during this cycle.\n"""
    elif personal_year == 2:
        print """\nA personal year 2 indicates slow but steady growth, with patience and persistence required. you may find yourself in competition with others at this time or that you have to work harder to resolve conflicts or find creative solutions to challenges.\n
This can also indicate feeling at a bit of crossroads or some uncertainty. It's important not to let it undermine your goals.\n"""
    elif personal_year == 3:
        print """\nExpansion and continued unfoldment that lead to success are the themes of a personal year 3. This is a good time to embrace partnerships and cooperation with others for common goals and the benefit of the whole.\n
More breathing room and a feeling of a burden eing lifted often accompany a personal year 3.\n"""
    elif personal_year == 4:
        print """\nA personal year 4 means a lot of responsibility, hard work, and diligent effots will be required. 4 speakds of "hands on" effort and making every effort count.\n
This is a year of uilding solid foundations and likely a year where you may feel you are not accomplishing as much as you actually are. The personal year 4 speaks of ground work and solidifying.\n"""
    elif personal_year == 5:
        print """\nA personal year 5 speaks of a strong desire for change, adventure and trying new things. This is a year where you will e more inclined to travel, move, or even change career paths.\n
This cycle brings out the pioneering spirit and the desire for new experience and expression. This is a personal year cycle where it can be easy to become distracted, and self-discipline is more difficult.\n"""
    elif personal_year == 6:
        print """\nThis personal year cycle tends to focus more on personal relationships. It is an excellent cycle for meeting new people, deepening or finding love with a special someone and otherwise, forming or strengthening lasting bonds with others.\n
You may find that you make new friends or mend fences at this time. A personal year 6 also indicates a phase where you may e called to face yourself with more honesty and work on cultivating more love/respect within.\n"""
    elif personal_year == 7:
        print """\nThe personal year 7 cycle typically rings a period of introspection and more solitude. A time for focusing on personal goals, growth, and expansion.\n
A 7 cycle can mean withdrawing a it socially to focus on personal issues. A great time for pursuing growth through education, enlightenment, etc.\n"""
    elif personal_year == 8:
        print """\nPersonal year 8 tends to indicate a good cycle for investments, monetary issues, and growth on a more material/career level. The 8 personal year cycle is a great time to focus on increasing business or even starting a new business.\n
It is during this phase that many people find themselves growing financially, getting promotions, and finding and building further success. A cycle of prosperity.\n"""
    else:
        print """\nThe personal year cycle 9 says as one thing ends another egins. There is a certain feeling of restlessness and anticipation that can make a 9 personal year a it uncomfortable for some, particularly for those who have difficulties accepting change.\n
This cycle rings the strong desire to make changes, to clear away areas that are no longer serving your growth and to remove limitations from your life as you prepare to start fresh on a new 1 cycle.\n"""

#pers_year_meaning(personal_year)


# to be deleted after menu is coded

#birth_or_nick = "birth"

# definition of function for last name


def ask_last_name(birth_or_nick):
    while True:
        if birth_or_nick == "birth":
            last_name = raw_input("Input your family (last) name at birth: ")
        else:
            last_name = raw_input("Input your family (last) name: ")

        if last_name.isdigit():
            print "Your parents named you a number?"
        else:
            last_name = last_name.lower()
            last_name = last_name.replace(" ", "")

        return last_name

#last_name = ask_last_name(birth_or_nick)


# definition of function for middle name


def ask_middle_name(birth_or_nick):
    while True:
        if birth_or_nick == "birth":
            middle_name = raw_input("Input your middle name at birth: ")
        else:
            middle_name = raw_input("Input your middle name: ")

        if middle_name.isdigit():
            print "Your parents named you a number?"
        else:
            middle_name = middle_name.lower()
            middle_name = middle_name.replace(" ", "")

        return middle_name

#middle_name = ask_middle_name(birth_or_nick)


# definition of function for first name


def ask_first_name(birth_or_nick):
    while True:
        if birth_or_nick == "birth":
            first_name = raw_input("Input your first (given) name at birth: ")
        else:
            first_name = raw_input("Input your first (nick) name: ")

        if first_name.isdigit():
            print "Your parents named you a number?"
        else:
            first_name = first_name.lower()
            first_name = first_name.replace(" ", "")

        return first_name

#first_name = ask_first_name(birth_or_nick)


# definition of function to assign numerical value to letters


def name_calc(name):
    partial_sum = 0
    for letter in range(len(name)):
        partial_name = ((ord(name[letter]) - ord("a")) % 9) + 1
        partial_sum += partial_name
    name_value = partial_sum

    return name_value


#single_last_master = single_digit_master(name_calc(last_name))
#single_middle_master = single_digit_master(name_calc(middle_name))
#single_first_master = single_digit_master(name_calc(first_name))

#print single_last_master, single_middle_master, single_first_master


# definition of a function to calculate expression/destiny number


def exp_calc(single_last_master, single_middle_master, single_first_master):
    exp_raw = single_last_master + single_middle_master + single_first_master
    exp_dest = single_digit_master(exp_raw)

    return exp_dest

#exp_dest = exp_calc(single_last_master, single_middle_master, single_first_master)


# definition of a function to display expression/destiny meaning


def exp_dest_meaning(exp_dest):
    print """\nYour expression (destiny) number is {}. Expression number describes your inherent traits and natural talents. It defines your highest potential and how to make the most of your experience in this life.\n""".format(exp_dest)

    if exp_dest == 1:
        print """\nThis expression numer represents the pioneering spirit, the risk taker and someone who is willing to put him/herself "out there" and try new things. Extroverted (typically) and very self-confident, sometimes even a it too self-centered.\n
This number speaks of someone with the desire to win, who will work harder than most to reach his/her goals. Independent and competitive - always growing and striving.\n"""
    elif exp_dest == 2:
        print """\nThe natural diplomat is represented with this destiny number. 2 people are well-balanced, able to bring people together and reach compromise.\n
They are quite intuitive and can sense the feelings of others which leads to this innate aility for teamwork. 2s emody fairness and balance. They also tend to develop strong musical talents as well due to their natural sense of rhythm and harmony.\n"""
    elif exp_dest == 3:
        print """\nThe 3 expression number speaks of someone who is very theatrical by nature - very expressive, outgoing, and a natural charmer. People with this number are often drawn towards writing, acting, or the arts - anywhere they can express themselves and share their views with others.\n
3s are capable of abstract thought and can paint pictures easily with words and communication. They have an innate ability to explain complex concepts in a way that is easy for everyone to grasp.\n"""
    elif exp_dest == 4:
        print """People with a 4 expression numer are considered down to earth, practical and orderly. 4 people thrive in environments that are well-organized, and they love structure and staility.\n
They are often seen as "the rock" or pillar strength in their families and businesses because of their strong sense of duty and discipline.\n"""
    elif exp_dest == 5:
        print """\nThe person with the 5 expression numer is a natural adventurer - someone who thrives on new experiences and who is a life long seeker and learner through hands on methods. These people are often "jack of all trades" types who are self-taught in many areas and are always wanting to tray something new.\n
The 5 expression number is destined to travel, have a variety of experiences and reak free of the societal mold that tells us to "do one thing" career wise, etc. 5s change their minds often and when they give themselves the freedom to explore, they lead very rich and interesting lives.\n"""
    elif exp_dest == 6:
        print """\n6 people are driven by a strong sense of duty and often put others ahead of themselves. They are called often to careers that allow them to help others - counselors, health care fields, teaching, etc.\n
People with a 6 expression numer tend to measure their own sense of self-worth ased on what they do for others. They need to be careful to not be too overprotective and to allow others the freedom to make their own choices in life.\n"""
    elif exp_dest == 7:
        print """\nPeople with 7 expression numer are very intuitive, intelligent - the seekers of truth and understanding. 7 people tend to be rather introverted and require a great deal of "personal space" in order to thrive.\n
7 people are motivated in life y a need for greater understanding and are often drawn to philosophical, spiritual, and/or metaphysical pursuits in their quest for deeper meaning.\n"""
    elif exp_dest == 8:
        print """\nPeople with an 8 expression number are incredily competitive, ambitious and hard working. Often destined for great successes in life, particularly in their career field.\n
8 people are excellent managers and builders who are very efficient and effective. They are able to balance strong ambitions with care and concern for others which allows them to create strong enterprises that serve their communities well.\n"""
    elif exp_dest == 9:
        print """\nPeople with a 9 destiny/expression number are the lofty idealists that inspire us to aim higher. Humanitarian by their very nature, 9 people are typically called to lives of activism and social issues.\n
They are driven by a need to be accpeted and loved by others and often become very well known or famous for their efforts. People with a 9 expression number are typically highly artisitc and creative and use those talents to promote a cause.\n"""
    elif exp_dest == 11:
        print """\nPeople with the master numer 11 as their expression number are naturally psychic and very intelligent. They have a great lend of logic and creativity and when they can balance these aspects and channel their vast energy in productive ways, nothing can stop them.\n
11s have to work hard to keep their higher virational energy levels up. 11s can become too cuaght up in fantasy over reality as an escape when their emotions overwhelm them. It is very important for people with this expression numer and life path to work hard to keep their energy fields in balance.\n"""
    else:
        print """\nPeople with this master numer 22 as their destiny number are great at bringing the sacred to the mundane - they can and do embrace all life and experience as a spiritual adventure and put this reverence into everything they build and create.\n
Natural builders, those with a 22 expression number are blessed as visionaries with strong leadership abilities. They can see a project through from start to finish - build what they envision with ease and grace.\n"""

#exp_dest_meaning(exp_dest)


# definition of a function to display cornerstone/capstone meaning


def cc_meaning(letter):
    if letter == "a":
        print """\nYou display originality and a strong sense of leadership and individualism with the letter A as your cornerstone. People with this cornerstone are very active and assertive towards reaching their goals. Confidence.\n"""
    elif letter == "b":
        print """\nYou are highly adaptive and cooperative, making a great team member who is reliable and trustworthy. You strive for balance and harmony.\n"""
    elif letter == "c":
        print """\nYou are creative, highly expressive, and love attention. C people are compelled to reach out to others and interact in meaningful ways.\n"""
    elif letter == "d":
        print """\nYou are a good planner, practical, down to earth and prefer structure over chaos. You are persistent and diligent in your efforts which ultimately leads to some degree of success.\n"""
    elif letter == "e":
        print """\nYou are open to life and very flexible, embracing the wisdom in all experience. Deeply emotional with excellent communication skills.\n"""
    elif letter == "f":
        print """\nYou are balanced, organized, and strive for harmony in all things. You are a great friend and good listener who makes others feel valued.\n"""
    elif letter == "g":
        print """\nYou are an independent person with a strong work ethic. You have strong focus, determination, and are very self-reliant.\n"""
    elif letter == "h":
        print """\nYou are tenacious, hard working and competitive. Your love of winning and competition give you a natural edge in business.\n"""
    elif letter == "i":
        print """\nYou have a strong idealism and strong sense of self. You know exactly what you hope to accomplish and don't adapt well to changes in plans.\n"""
    elif letter == "j":
        print """\nYou are motivated and self-confident. You prefer to take action over sitting back and show great initiative. Sometimes there is a tendencey towards impulsive behavior.\n"""
    elif letter == "k":
        print """\nYou are strong-willed and emotional. You are also able to pick up on subtle insights that others often miss and are very perceptive.\n"""
    elif letter == "l":
        print """\nYou have strong social skills and are naturally attractive to others. Easy going and appreciative of the simple things in life.\n"""
    elif letter == "m":
        print """\nYou are considered practical and hard working - a prolem solver who doesn't shy away from a challenge. M people are quite independent, but can still work well with others when necessary.\n"""
    elif letter == "n":
        print """\nYou are very social and well-liked by others. N people are popular and enjoy adventure and change in life. You may find you bore easily and need variety to stay motivated.\n"""
    elif letter == "o":
        print """\nYou are disciplined and motivated. You love to learn and are very knowledgable about a variety of subjects. You are someone who learns easily and may find that you are "self-taught" in many areas.\n"""
    elif letter == "p":
        print """\nYour focus is on self-knowledge and seeking wisdom. You are focused on spiritual and personal growth and are likely drawn to philosophy, self-help subjects, and the metaphysical.\n"""
    elif letter == "q":
        print """\nYou have a keen intuition and innate ability to sense the strengths and weaknesses in others which makes you very strong in business and sales.\n"""
    elif letter == "r":
        print """\nYou have a wide range of interests, are confident, and independent with a strong desire to be successful in life.\n"""
    elif letter == "s":
        print """\nYou are a charming and charismatic person with a strong business sense. You are deeply passionate and are sometimes prone to acting on impulse.\n"""
    elif letter == "t":
        print """\nYou are highly sensitive and emotional which gives your life complexity and depth, but it can also result in your sometimes being hurt too easily.\n"""
    elif letter == "u":
        print """\nYou are smart, creative, and naturally attractive to others. You have the propensity for epic success and failure and may find you experience a variety of extremes in your life.\n"""
    elif letter == "v":
        print """\nYour vivid imagination leads you to great plans and discoveries. You are a rugged individualist who expresses yourself uniquely. Sometimes you are prone to flights of fancy and may lack needed objectivity.\n"""
    elif letter == "w":
        print """\nYou are a charismatic, people person who thrives on variety in life and in your career. You are very expressive and have a strong sense of higher purpose.\n"""
    elif letter == "x":
        print """\nYou are creative and passionate in all you do and have a tendency towards strong desires that can make moderating ehaviors more challenging for you. Truly unique and deeply in tune to your emotions, you experience richness in all life's experiences.\n"""
    elif letter == "y":
        print """\nYou are a freedom loving person who does not accpet limitations or allow anything to hold you back. You are amitious and independent with a keen intuition.\n"""
    else:
        print """\nYou are an optimist who has great vision, but are ale to balance that with rational thought and ojectivity. Your compassion and kindness are like a magnet to others.\n"""


# definition of a function to display cornerstone and capstone


def corn_cap(first_name):
    cornerstone = first_name[0]
    capstone = first_name[-1]

    print """\nCornerstone gives insight into how you approach challenges in life and how you master situations. Capstone gives insight into how you make transitions in your life, how you finish projects or move from one thing into another.\n"""

    print """Your cornerstone: """
    cc_meaning(cornerstone)

    print """Your capstone: """
    cc_meaning(capstone)

    return cornerstone, capstone

#corn_cap(first_name)


# definition of a function to calculate hidden passion number


def pass_calc(last_name, middle_name, first_name):
    full_name = last_name + middle_name + first_name
    for letter in range(len(full_name)):
        partial_name = ((ord(full_name[letter]) - ord("a")) % 9) + 1

    partial_name = str(partial_name)
    hid_pass = int(max(partial_name, key=partial_name.count))

    return hid_pass

#hid_pass = pass_calc(last_name, middle_name, first_name)


# definition of a function to display hidden passion meaning


def hid_pass_meaning(hid_pass):
    print """\nYour hidden passion number is {}. Hidden passion number defines your greatest natural talents, strengths and motivations. They are strengths that are readily available to you, that you can easily develop and use throughout your life.\n""".format(hid_pass)

    if hid_pass == 1:
        print """\nThis person is driven y a strong individualism and need to stand out in the crowd and get noticed. Ambitious and motivated, those with this hidden passion number are natural leaders.\n"""
    elif hid_pass == 2:
        print """\n2 people are natural peacemakers and negotiators who strive to create harmony in the family, workplace, and wherever they may go. People naturally gravitate to you because they feel a strong innate sense of trust.\n
You are patient and persistent. 2 people are naturally inclined towards music and the arts.\n"""
    elif hid_pass == 3:
        print """\nThe 3 person is a natural born entertainer who is very social. You have a natural charm which is alluring to others. 3 people are naturally gifted creatively and are often multi-talented in various forms of art, music, writing, etc.\n"""
    elif hid_pass == 4:
        print """\n4 people are extremely diligent, determined hard-workers, and for this reason, they are capable of uilding great successes from the ground up. Practical, disciplined, and seen as a great provider or support sytem to others.\n
You are "the rock" of your family/group. 4 people are very organized and efficient and need a sense of order in their lives.\n"""
    elif hid_pass == 5:
        print """5 is the number of those who love adventure and new experiences. People with this number love to indulge the senses and are natural communicators. Many are drawn to writing and other forms of communication.\n
People with this number can be prone to being a it too impulsive at times and need to work to cultivate self-discipline. 5 people thrive on change in life and often struggle when they feel they have to "choose" one path.\n"""
    elif hid_pass == 6:
        print """\n6 people have a natural call to service and are often healers, counselors, teachers, etc. Responsile and self-sacrificing 6 people have an inner need to be recognized and valued by others in order to feel a strong sense of self-worth.\n"""
    elif hid_pass == 7:
        print """\n7 people are naturally intuitive and highly intelligent. They are the thinkers who seek the deeper meanings behind experience and are often drawn to philosophy, metaphysics, psychology and any area that explores the subconscious or hidden truths. 7 people are often sought out for their insight and keen understanding.\n"""
    elif hid_pass == 8:
        print """\n8people are natural salesmen and business people. They have an innate dirve that pushes them to accomplish great things. The right blend of vision and amition, people with an 8 passion are driven by material success and the need to compete with themselves and others. No other number is as energetic and motivated by winning/reaching goals.\n"""
    else:
        print """\n9 people are visionaries with a deep sense of humanitarianism. They have lofty ideals and strive to make their communities and even the world a better place.\n
Highly emotional and idealistic, it can be difficult for 9s to bring their ideas down to earh in a more practical way. 9s see the future and have great vision and need to surround themselves with those who can help them actually manifest these goals/dreams.\n"""

#hid_pass_meaning(hid_pass)


# definition of a function to display main menu


def main_menu_choice():
    print """\n     1 - Show numerology by birthday."""
    print """     2 - Show numerology by birth name."""
    print """     3 - Show numerology by common or nick name."""
    print """     4 - Exit the program.\n"""

    choice = int(raw_input("Choose from the menu options: "))

    return choice


# definition of a function to display birthday menu


def birthday_menu_choice():
    print """\n     0 - Return to main menu."""
    print """     1 - Show life path number."""
    print """     2 - Show birth day number."""
    print """     3 - Show challenge number(s)."""
    print """     4 - Show personal year number.\n"""

    choice = int(raw_input("Choose from the menu options (return to main menu to exit): "))

    return choice


# definition of a function to display challenge menu


def challenge_menu_choice():
    print """\n     0 - Return to birthday main menu."""
    print """     1 - Show first challenge number."""
    print """     2 - Show second challenge number."""
    print """     3 - Show third challenge number."""
    print """     4 - Show fourth challenge number.\n"""

    choice = int(raw_input("Choose from the menu options: "))

    return choice


# definition of a function to display name menu


def name_menu_choice():
    print """\n     0 - Return to main menu."""
    print """     1 - Show expression (destiny) number."""
    print """     2 - Show soul urge number."""
    print """     3 - Show personality number."""
    print """     4 - Show hidden passion number."""
    print """     5 - Show karmic number."""
    print """     6 - Show cornerstone and capstone numbers.\n"""

    choice = int(raw_input("Choose from the menu options (return to main menue to exit): "))

    return choice


# definition of a function to execute within the challenge menu


def challenge_exec_repl(single_day_uno, single_month_uno, single_year_uno):
    challenge_intro()

    while True:
        # get choice from user from challenge menu
        choice = challenge_menu_choice()

        if (choice < 0) or (choice > 4):
            # if choice was not on menu, note error
            print """\nPlease choose from the menu options.\n"""
        else:
            if choice == 0:
                # return to birthday menu
                break
            elif choice == 1:
                # calculate and display meaning for first challenge number
                first_chall = first_chall_calc(single_day_uno, single_month_uno)
                first_chall_meaning(first_chall)
            elif choice == 2:
                # calculate and display meaning for second challenge number
                sec_chall = sec_chall_calc(single_day_uno, single_year_uno)
                sec_chall_meaning(sec_chall)
            elif choice == 3:
                # calculate and display meaning for third challenge number (note that since user may not choose option 1 and 2, first and second challenges would have to be called here)
                first_chall = first_chall_calc(single_day_uno, single_month_uno)
                sec_chall = sec_chall_calc(single_day_uno, single_year_uno)
                third_chall = third_chall_calc(first_chall, sec_chall)
                third_chall_meaning(third_chall)
            elif choice == 4:
                # calculate and display meaning for fourth challenge number
                fourth_chall = fourth_chall_calc(single_month_uno, single_year_uno)
                fourth_chall_meaning(fourth_chall)


# definition of a function to execute within the birthday menu


def birthday_exec_repl():
    # ask user for birthday information
    year = ask_year()
    month = ask_month()
    day = ask_day(year, month)
    single_year_master = single_digit_master(year)
    single_month_master = single_digit_master(month)
    single_day_master = single_digit_master(day)
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


def name_exec_repl(birth_or_nick):
    # ask user for name information
    last_name = ask_last_name(birth_or_nick)
    middle_name = ask_middle_name(birth_or_nick)
    first_name = ask_first_name(birth_or_nick)
    single_last_master = single_digit_master(name_calc(last_name))
    single_middle_master = single_digit_master(name_calc(middle_name))
    single_first_master = single_digit_master(name_calc(first_name))

    while True:
        # get choice from user from name menu
        choice = name_menu_choice()

        if (choice < 0) or (choice > 6):
            # if choice was not on menu, note error
            print """\nPlease choose from the menu options.\n"""
        else:
            if choice == 0:
                # return to main menu
                break
            elif choice == 1:
                # calculate and display meaning for expression (destiny) number
                exp_dest = exp_calc(single_last_master, single_middle_master, single_first_master)
                exp_dest_meaning(exp_dest)
            elif choice == 2:
                # calculate and display meaning for soul urge number - STILL NEED TO CODE
                continue
            elif choice == 3:
                # calculate and display meaning for personality number - STILL NEED TO CODE
                continue
            elif choice == 4:
                # calculate and display meaning for hidden passion number
                hid_pass = pass_calc(last_name, middle_name, first_name)
                hid_pass_meaning(hid_pass)
            elif choice == 5:
                # calculate and display meaning for karmic number = STILL NEED TO CODE
                continue
            elif choice == 6:
                corn_cap(first_name)


# definition of a function to execute the numerology program


def execute_repl():
    greeting()

    while True:
        # get choice from user from main menu
        choice = main_menu_choice()

        if (choice < 1) or (choice > 4):
            print """\nPlease choose from the menu options.\n"""

        if choice == 1:
            # get choice from user from birthday menu and repl within that menu
            birthday_exec_repl()
        elif choice == 2:
            # get choice from user from name menu and repl within that menu based on birth name
            birth_or_nick = "birth"
            name_exec_repl(birth_or_nick)
        elif choice == 3:
            # get choice from user from name menu and repl within that menu based on nick name
            birth_or_nick = "nick"
            name_exec_repl(birth_or_nick)
        else:
            print """\nHave a wonderful day with your numerical vibrations. Namaste!\n"""
            break

execute_repl()
