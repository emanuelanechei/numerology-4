# definition of function to print introduction message

def greeting():
    print """\nWelcome to the nexus of numerology.\n 
    Numerology is the study of the numerical value of letters in words, names and birthdays.\n 
    It is similar to astrology, and often associated with the belief in the divine, mystical relationship between numbers and one or more coinciding events.\n"""

greeting()


# definition of function for birth year


def ask_year():
    while True:
        year = raw_input("Input your year of birth: ")
        if not year.isdigit():
            print "Please input the year based on the Gregorian calendar."
        else:
            year = int(year)
            return year

year = ask_year()


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

month = ask_month()


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
            else:
                return day

day = ask_day(year, month)


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

single_year_master = single_digit_master(year)
single_month_master = single_digit_master(month)
single_day_master = single_digit_master(day)

print single_year_master, single_month_master, single_day_master


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

single_year_uno = single_digit_uno(year)
single_month_uno = single_digit_uno(month)
single_day_uno = single_digit_uno(day)

print single_year_uno, single_month_uno, single_day_uno


# definition of function to calculate life path number


def life_path_calc(single_year_master, single_month_master, single_day_master):
    life_path_raw = single_year_master + single_month_master + single_day_master
    life_path = single_digit_master(life_path_raw)
    print """\nYour life path number is {}. Life path number defines limitations or possibilities in life and gives insights to the direction you'll take and the decisions that will affect the life you lead.\n""".format(life_path)

    if life_path == 1:
        print """You are all about power! Strong and determined individuals carry this life path number. They are often leaders in business and have great personal ambition.\n
        They are motivated by personal success and competition. Highly independent by nature - the person with the 1 life path is often very innovative and creative in their thinking. Highly analytical and very sharp, they are natural problem solvers.\n
        Number 1s who stray from their paths often end up in clingy co-dependent relationships.\n"""
    elif life_path == 2:
        print """You are all about love. People with life path 2 love to find and maintain balance. They are natural peacemakers and tend to be drawn towards service to others.\n
        Often they are too self-sacrificing and struggle to find balance in life when it comes to valuing themselves as much as others. People with this life path numer tend to be somewhat reserved and quiet. They have excellent listening skills and tend to be very drwan to music.\n
        It is very important for them to get out and socialize. A number 2 who is isolated courts pessimism, lethargy and depression.\n"""
    elif life_path == 3:
        print """You are all about performance! This is the life path numer of creative people who are very expressive and unique. They are skilled communicators, naturally charming and attractive to others. They know how to convey ideas.\n
        3 people tend to be very optimistic and hopeful people who encourage and nourish that quality in others. They tend to be very energetic and busy - to the point they may wear themselves out.\n
        Number 3s stray off their life path by giving up their dreams and talents. Many escape into drug abuse or promiscuity to avoid hearing the nagging voice of their true calling to express their talents.\n"""
    elif life_path == 4:
        print """You are all about stability! This is the life path number of the pragmatic organizer - the one who builds, constructs, works hard and who is very diligent and persistent in his efforts.\n
        People with this life path are considered "practical" and down to earth. Many workaholic types have the 4 as a life path numer. People with this life path tend to prefer to follow established rules and believe in order. They don't tend to like surprises and are rather meticulous.\n
        However, self-sacrificing number 4s often demand too much, both of themselves and others, and develop reputations as martyrs or tyrants. Their willpower and stubbornness can also be interpreted as greed and selfishness.\n"""
    elif life_path == 5:
        print """You are all about freedom! Those with a 5 life path are gregarious, fun-loving people who love to be surrounded by others. The 5 life path is a bit free-spirited and enjoys adventure, travel, and diversity.\n
        People with this life path often thrive in careers that involve travel or working aorad. They do not do well in office settings or any place that liits their freedom and creative expression.\n
        However, 5s tend to be very self-absorbed and unaware of the effect of their actions on other people. As other people often feel tricked or fooled by number 5s, experiencing a series of broken relationships is also often a part of their path. People with this life path sometimes have difficulty with discipline or finishing what they started.\n"""
    elif life_path == 6:
        print """You are all about nurturing. Those with this life path of 6 are hard workers, tend to have a variety of skills and interests and are very "direct" in their approach. Sometimes prone to being too hard on themselves, they will push themselves to their limits.\n
        6 people are typically very organized and efficient and dislike waste - whether it be wasted time or resources. Those with this life path are sometimes seen as strict or sharp, but in actuality, they do have the best interest s of others at heart and love to see people reach their potentical. People with this life path make good personal trainers, drill instructors, etc. ecause they can push others to their personal limits in ways that are both compassionate and motivating.\n
        6s that find themselves enslaved to an addicted or mentally ill partner might not be following their true path, as this is a sign that they have become enablers, rather than healers of the diseases.\n"""
    elif life_path == 7:
        print """You are all about knowledge! 7 is the life path numer of the Seeker. People with this life path numer are drawn to the igger mysteries in life and are always looking for a larger purpose behind their circumstances.\n
        7s are often psychic or extremely intuitive by nature with an innate aility to see to the heart and soul of others and situations. 7 people tend to love people, but are also very independent, requiring a great deal of solitary time to recharge their batteries. 7 people can be prone to being slow movers and procrastinators and need to work to keep their motivation levels up.\n
        A sign that a number 7 has strayed completely off his or her life path is a complete withdrawal from society. In this case, the troubled 7 should try to recognize his or her original ambitions to improve the world through the application of wisdom.\n"""
    elif life_path == 8:
        print """You are all about wealth. 8 is the life path of the natural born leader. These are people who are often very good at business and attracting wealth and favors. 8 people are often visionaries and capable of great things because they can also do the hard work required to make thier visions a reality.\n
        8 people are very capable and inspiring leadrs, and people are compelled to follow their lead or be left behind. 8s do etter when they don't let their amitions get the better of their compassionate side - doing so can lead to greed and accumulation of wealth for less noble reasons.\n
        Sometimes the pursuit of riches becomes more important than personal relationships and cost them their personal relationships, morality and popularity.\n"""
    elif life_path == 9:
        print """You are all about spirituality. Life path 9 is the life path of the humanitarian. A natural orn leader by nature, you are compelled to lead and to serve. Your high ideals give you a strong desire to improve the lives of others.\n
        You are innovative, visionary, and good at implementing new concepts and ideas. People with this life path sometimes struggle with disappointment when they can't live up to their high ideals. There is a need to learn to accept themselves more because when they do, they are capale of great things.\n
        These sophisticated individuals are very selfless souls and are often patient, trustworthy, and honorable from the very beginning to the end of their lives. Sometimes a 9s lofty ideals are presented in a manner that others find absurd. Part of a 9s life path is to express spiritual principles through actions, rather than through preaching or proselytizing.\n"""
    elif life_path == 11:
        print """You are about enlightenment. Those with this life path numer are extremely intuitive and feel a strong connection with others, sometimes to the point that it overwhelms their emotions.\n
        11 people are very visionary and tend to be great thinkers. Solutions to prolems seem to come to them with very little effort and sometimes they don't understand how gifted they are at seeing what is "hidden" or elusive to others.\n
        Many of them are "wounded healers" who at some point in their life suffer a devastating experience that propels them on the search for spirituality. However, along with these situations, usually comes a lot of toxic emotional baggage and harsh inner critic. It takes many 11s their entire life to rid themselves of the 'chip on their shoulder' and achieve enlightenment.\n"""
    else:
        print """You are a master builder. The strongest of the life path numers, the 22 carries great potential, ut also great weight and responsibility. This card represents those who can e master uilders and visionaries, who can rally around a cause and bring people together for the common good.\n
        Those with this life path often face weighty decisions at several points in their life where they must emrace the crossroads with confidence and make a choice. Those who are not fully in tune with this higher viration may find they struggle with choice in life and must work to take the path that challenges them over the path of least resistence. Sometimes they display what looks like insensitivity but actually they are just very focused on their goals. This is part of a spiritual directive to be detached from objects and the outcomes of events.\n
        22 life path people who push themselves and embrace change can live truly astounding, creative lives."""

    return life_path


# definition of function to calculate birth day number


def birth_day_calc(single_day_master):
    print """\nYour birth day number is {}. Birth day number defines your very special talent or strength that greatly facilitates the fulfillment of your destiny.\n""".format(single_day_master)

    if single_day_master == 1:
        print """Your birth day number is 1. This birth day signifies natural born leaders, those with a lot of drive and initiative.\n
        One people are ambitious, hard working, and often very career focused. One people have a keen intelligence and are quick learners who are able to do things on a grand scale.\n"""
    elif single_day_master == 2:
        print """Two people are very balanced and tend to be natural peace keepers and diplomats. Natural negotiators, two people dislike conflict and will work hard to make compromises that benefit everyone.\n
        Two people love to do important things behind the scenes and tend to have a good blend of both creative and analytical skills.\n"""
    elif single_day_master == 3:
        print """Three people are natural artists and love to express themselves creatively in a variety of forms. Three people are inspiring and display greath enthusiasm.\n
        Three people have great imagination and vision and are also sharp and able to pick up on subtle details.\n"""
    elif single_day_master == 4:
        print """Four people are very hard-working and diligent. They are those who build a strong foundation and like structure and stability.\n
        Loyal and genuinely honest, four people find others trust and rely upon their quiet strength and strong common sense approach to life.\n"""
    elif single_day_master == 5:
        print """Five people are your movers and shakers who long for adventure and new experience. Five people love and embrace diversity and require a lot of changes to keep them motivated and inspired.\n
        Five people can be prone to carelessness at times, but their deep love of adventure and naturally keep social skills make them a joy to know - 'never a dull moment' as the saying goes.\n"""
    elif single_day_master == 6:
        print """Six people work hard to walk the 'middle ground' in life and feel the need for balance weighing on them quite often. Naturally artistic and expressive, but highly sensitive, six people tend to be very vulnerable to criticism and require a lot of positive reinforcement in life to keep them motivated.\n
        They are naturally good at working for compromise, but have a strong sense of duty and don't tolerate excuses or 'victim' mentality in others. 'If they can do it, you can too' is their motto, but they are always eager to extend themselves to encourage and help others find their own inner strength.\n"""
    elif single_day_master == 7:
        print """Seven people are your natural born seekers and philosophers, those who seek truth and higher wisdom in all experiences Seven people tend to have a naturally strong intuition, but often struggle with their emotions which can sometimes cloud their judgment unless they learn to work through their emotional sensitivities with honesty.\n
        Seven people are often highly intellectual as well and need to learn to balance that with their deep emotions so that they don't become cynical or detached from others.\n"""
    elif single_day_master == 8:
        print """Eight people are daring and bold, usually naturally good in business, and they have a knack for making or acquiring money. Eight people are very motivated by success and are quite competitive.\n
        They are also prone to being very self-confident, practical and efficient which lends to others trusting them with their business. Eight people are often seen as 'lucky' or having lucky breaks in life - but this is typically due to a natural drive and persistence that helps them attract what they want/need for success.\n"""
    elif single_day_master == 9:
        print """Nine people are compassionate, dreamy and idealistic in nature. They are highly creative and often devote themselves to life-long learning. Many people with multiple degrees will have this number; they are never 'finished' or 'masters' as they embrace continued growth and personal expansion.\n
        Nine people are visionaries who do best when they learn to assert themselves and master their insecurities. Worldly, creative and ever expansive, nine people often appear larger than life.\n"""
    elif single_day_master == 11:
        print """People with master number 11 are exceptionally intuitive and are often naturally drawn to the healing arts. 11 people are compelled with a strong drive towards service to others.\n
        Highly sensitive, a dreamer, 11 people have to work hard to stay motivated and take action on their loftier goals.\n"""
    else:
        print """People with master number 22 are great builders and organizers. This number means you are gifted with the natural ability to not only visualize a plan but to see hte actual result ahead of time.\n
        You are both a 'seer and a doer' and when you properly apply yourself, can see through from start to finish with relative ease. Your perception is keep and you have the right blend of idealism and practicalithy that can take you far.\n"""

    return single_day_master


# definition of function to display challenge number meanings


def chall_meaning(challenge):
    if challenge == 0:
        print """The zero challenge number tends to indicate no one specific area or challenge being greater than others. It can also mean a sort of mixed bag when it comes to minor challenges, but these are all designed to help you find your strength.\n
        Zero challenges are more about developing one's strengths and having confidence in your abilities - becoming more well-rounded.\n"""
    elif challenge == 1:
        print """The challenge with one is learning to exert your independence and speak out authentically. One people tend ot struggle with the need for approval from others from which they base their own sense of self-worth.\n
        The challenge is to value oneself enough to be unique.\n"""
    elif challenge == 2:
        print """People with this challenge struggle with balance emotionally. They take criticism very personally and struggle to assert themselves.\n
        People with this challenge often shirk responsibility because they don't want the pressure of others depending on them or because they are convinced that they can't handle it. People with this challenge in full force tend to shrink back a lot.\n"""
    elif challenge == 3:
        print """People with a 3 challenge number tend to have difficulty finishing what they start. They tend to multi-task in ways that are not effective and have many unfinished projects and goals that they struggle to reach.\n
        Three people also tend to go on the defensive easily or 'react' to situations rather than think them through. They have difficulty expressing themselves at times in ways that are healthy and productive.\n"""
    elif challenge == 4:
        print """This challenge has a lot to do with procrastination and not working hard enough to reach one's goals. Often this challenge can speak of going for the path of least resistance rather than really pushing your limits.\n
        When the 4 is your challenge number, you are being pushed to be more assertive and efficient in your work habits.\n"""
    elif challenge == 5:
        print """The 5 as a challenge indicates a high degree of impusliveness and reckless behavior. The 5 is the number for freedom and adventure, but as a challenge, it can indicate a need to tone it down a bit and to attain some discipline and foresight.\n"""
    elif challenge == 6:
        print """People with a 6 challenge struggle with perfectionism. They demand too much of themselves and often those around them. As a result, they can come off as cynical, too authoritarian, and too critical.\n
        People with this challenge need to learn to lighten up a bit, and unconditional love and acceptance of both self and others are their lessons.\n"""
    elif challenge == 7:
        print """Unexpressed emotions, difficulty accpeing concepts that defy 'norms,' and being too overly analytical can be themes of the 7 challenge number.\n
        People with this challenge tend to be overly anayltical, dismissing anything that does not coincide with their own sense of logic. As a result, people with a 7 challenge are not as open-minded or open to new experiences as they could or should be.\n"""
    else:
        print """Materialism above all else tends to be the theme of the 8 challenge number. People with this challenge give too much importance to material affairs and may rely upon social status and money to provide their sense of self-worth or value.\n
        It can be tempting for people with this challenge to resort to less than scrupulous tactics in their business ventures, and they need to work to better balance the material world with their spiritual side.\n"""
    return challenge


# definition of function to introduce challenge numbers


def challenge_intro():
    print """Challenge numbers define four life cycles and the related challenges that one has to work to grow through, tendencies and obstacles that will pop up during those cycles. When faced with honesty, these numbers can lend great insight into areas for self improvement and personal growth.\n
    Four numbers represent: 1) from birth to approximately age 35; 2) from 35 to approximately 60; 3) primary challenge that one faces throughout life; and 4) from 60 to end of life.\n"""


# definition of function to calculate first challenge number


def first_chall_calc(single_day_uno, single_month_uno):
    first_chall = abs(single_day_uno - single_month_uno)
    print """\nYour first challenge number is {}, which is from birth to approximately age 35.\n""".format(first_chall)
    first_challenge = chall_meaning(first_chall)
    
    return first_chall


# definition of function to calculate second challenge number


def sec_chall_calc(single_day_uno, single_year_uno):
    sec_chall = abs(single_year_uno - single_day_uno)
    print """\nYour second challenge number is {}, which is from approximately age 35 to approximately age 60.\n""".format(sec_chall)
    second_challenge = chall_meaning(sec_chall)
    
    return sec_chall


# definition of function to calculate third challenge number


def third_chall_calc(first_chall, sec_chall):
    third_chall = abs(sec_chall - first_chall)
    print """\nYour third challenge number is {}, which represents the primary challenge that one faces throughout life.\n""".format(third_chall)
    third_challenge = chall_meaning(third_chall)
    
    return third_chall


# definition of function to calculate fourth challenge number


def fourth_chall_calc(single_month_uno, single_year_uno):
    fourth_chall = abs(single_year_uno - single_month_uno)
    print """\nYour fourth (and final) challenge number is {}, which from approximately age 60 to end of life.\n""".format(fourth_chall)
    fourth_challenge = chall_meaning(fourth_chall)
    
    return fourth_chall

# definition of function to calculate personal year number


from datetime import date


def pers_year_calc(single_day_uno, single_month_uno, single_year_uno):
    single_current_uno = single_digit_uno(date.today().year)
    personal_year_raw = single_current_uno + single_month_uno + single_day_uno
    personal_year = single_digit_uno(personal_year_raw)
    print """\nYour personal year number is {}. Personal year number gives insight into what surrounds you for this year cycle and represents various themes and events that will likely occur for you during the year (from your birthday until your next birthday).\n"""

    return personal_year

date(year, month, day)
date.today()
