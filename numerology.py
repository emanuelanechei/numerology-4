# introduction to numerology

while True:
    welcome = raw_input("Welcome to the world of numerology. Do you want to learn more about your core numbers? (Y/N) ")
    if welcome.lower() == "n":
        print "You're missing out on the path to enlightenment. Have a great day!"
        break
    elif welcome.lower() != "y":
        print "Input Y or N"
    else:
        # input of birthdate
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
                                        # For leap year, if divisible by 100 but not 400, then not leap year. otherwise, divisible by 4.
                                        print "You took a flying leap off of this planet!"
                                    elif (month == 2) and (year % 4 != 0) and ((day < 1) or (day > 28)):
                                        print "That may be a day on Venus, but not on Earth!"
                                    else:
                                        print "Let's start by looking at your life path number!"
                                        break
                    break
            break
    break

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

single_year_master = single_digit_master(year)
single_month_master = single_digit_master(month)
single_day_master = single_digit_master(day)


# calculation of life path number

life_path_raw = single_year_master + single_month_master + single_day_master
life_path = single_digit_master(life_path_raw)

print ""
print "Your life path number is number is " + str(life_path) + "! Life path number defines limitations or possibilities in life due to ancestry or physicality."
print ""

if life_path == 1:
    print "You are all about power! Number 1s often become great leaders. For this reason, they make great entprepreneurs, freelancers, generals, commanders, CEOs and producers. A number 1 is usually blessed with motivation, enthusiasm, creativity and inspiration. They tend to be physically healthier and mentally stronger than most people are. They often lust for success (especially material) at any cost. Number 1s who stray from their paths often end up in clingy co-dependent relationships."
elif life_path == 2:
    print "You are all about love. The most important thing to you is finding a soulmate. Those following a number 2 life path tend to be diplomatic, sensitive individuals who make great judges, mediators, lawyers, counselors or social workers as they bring harmony to all group situations. It is very important for them to get out and socialize. A number 2 who is isolated courts pessimism, lethargy and depression."
elif life_path == 3:
    print "You are all about performance! Number 3s are entertainers of the world and most of them are truly gifted musicians, writers, actors, dancers, public speakers and politicians. The number 3 life path is one that is characterized by beauty, excitment, eccentricity and fame. Number 3s stray off their life path by giving up their dreams and talents. Many escape into drug abuse or promiscuity to avoid hearing the nagging voice of their true calling to express their talents."
elif life_path == 4:
    print "You are all about stability! Number 4s often end up becoming the pillars of the community. These individuals are hard working, practical and trustworthy. These loyal individuals make fantastic marriage and business partners. However, self-sacrificing number 4s often demand too much, both of themselves and others, and develop reputations as martyrs or tyrants. Their willpower and stubbornness can also be interpreted as greed and selfishness."
elif life_path == 5:
    print "You are all about freedom! 5s are highly inquisitive individuals who consider hands-on experience to be the best teacher in life. Many of them are deeply intelligent, philosophical and spiritually-minded. They are also great communicators that make excellent social antrhopologists, archaeologists, teachers, writers and historians. However, 5s tend to be very self-absorbed and unaware of the effect of their actions on other people. As other people often feel tricked or fooled by number 5s, experiencing a series of broken relationships is also often a part of their path."
elif life_path == 6:
    print "You are all about nurturing. Number 6 life path are usually people-pleasers that have a great need to feel indispensible to others. For this reason, many number 6s often dedicate their lives to being caregivers and service providers such as doctors, nurses, counselors, fire fighters and law keepers. Sixes usually feel a spiritual obligation to help others. Sixes that find themselves enslaved to an addicted or mentally ill partner might not be following their true path, as this is a sign that they have become enablers, rather than healers of the diseases."
elif life_path == 7:
    print "You are all about knowledge! Sevens' intellectual and studious personalities often pursue advanced academic careers. As they love to absorb informaton, they usually require a great deal of private time to cultivate their knowledge. These reserved and analytical deep-thinkers make great mathematicians, engineers, inventors, scientists, and doctors. A sign that a number 7 has strayed completely off his or her life path is a complete withdrawal from society. In this case, the troubled 7 should try to recognize his or her original ambitions to improve the world through the application of wisdom."
elif life_path == 8:
    print "You are all about wealth. Number 8s are usually confident, charismatic individuals. Usually, their life purpose is learning to manipulate money and power without becoming corrupted in the process. Tehy become landowners, builders and bankers. Eights have tremendous potential for pracitcally improving the lives of thousands, perhaps millions, of people. Sometimes the pursuit of riches becomes more important htan personal relationships and cost them their personal relationships, morality and popularity."
elif life_path == 9:
    print "You are all about spirituality. Those on the number 9 life path are destined to travel a humanitarian path. These sophisticated individuals are very selfless souls and are often patient, trustworthy, and honorable from the very beginning to the end of their lives. These individuals make great environmentalists, teachers, artists, priests and healers. Sometimes a nine's lofty ideals are presented in a manner that others find absurd. Part of a 9s life path is to express spiritual principles through actions, rather than through preaching or proselytizing."
elif life_path == 11:
    print "You are about enlightenment. Elevens tend to lead a life of extremes. In their quest to find a balance between the rational and the irrational, they will often pursue the most eclectic of religions and cultures. These avant-garde and visionary individuals make great students, psychics, mystics, healers, teachers, writers, musicians and artists. Many of them are 'wounded healers' who at some point in their life suffer a devastating experience that propels them on the search for spirituality. However, along with these situations, usually comes a lot of toxic emotional baggage and harsh inner critic. It takes many 11s their entire life to rid themselves of the 'chip on their shoulder' and achieve enlightenment."
else:
    print "You are a master builder. Whatever a 22 thinks about is almost sure to become manifest so it is very important for them to choose their thoughts carefully. If they are willing to work for what they desire, they can achieve enormous prestige, success and fame. They are the most capable of the life path numbers and are endowed with many powers. They have a unique talent for manifesting ideas into the realm of reality. Sometimes they display what looks like insensitivity but actually they are just very focused on their goals. This is part of a spiritual directive to be detached from objects and the outcomes of events. Many of them work for material gain, with the idea that their wealth should be spread among the masses."

print ""


# calculation of birth day number

while True:
    birth_day_text = raw_input("Birth day number defines your very special talent or strength that greatly facilitates the fulfillment of your destiny. Would you like to know your birth day number? (Y/N) ")
    if birth_day_text.lower() == "n":
        print "Namaste. Have a great day!"
        break
    elif birth_day_text.lower() != "y":
        print "Input Y or N"
    else:
        print ""
        if single_day_master == 1:
            print "Your birth day number is 1. This birth day signifies natural born leaders, those with a lot of drive and initiative. One people are ambitious, hard working, and often very career focused. One people have a keen intelligence and are quick learners who are able to do things on a grand scale."
        elif single_day_master == 2:
            print "Two people are very balanced and tend to be natural peace keepers and diplomats. Natural negotiators, two people dislike conflict and will work hard to make compromises that benefit everyone. Two people love to do important things behind the scenes and tend to have a good blend of both creative and analytical skills."
        elif single_day_master == 3:
            print "Three people are natural artists and love to express themselves creatively in a variety of forms. Three people are inspiring and display greath enthusiasm. Three people have great imagination and vision and are also sharp and able to pick up on subtle details."
        elif single_day_master == 4:
            print "Four people are very hard-working and diligent. They are those who build a strong foundation and like structure and stability. Loyal and genuinely honest, four people find others trust and rely upon their quiet strength and strong common sense approach to life."
        elif single_day_master == 5:
            print "Five people are your movers and shakers who long for adventure and new experience. Five people love and embrace diversity and require a lot of changes to keep them motivated and inspired. Five people can be prone to carelessness at times, but their deep love of adventure and naturally keep social skills make them a joy to know - 'never a dull moment' as the saying goes."
        elif single_day_master == 6:
            print "Six people work hard to walk the 'middle ground' in life and feel the need for balance weighing on them quite often. Naturally artistic and expressive, but highly sensitive, six people tend to be very vulnerable to criticism and require a lot of positive reinforcement in life to keep them motivated. They are naturally good at working for compromise, but have a strong sense of duty and don't tolerate excuses or 'victim' mentality in others. 'If they can do it, you can too' is their motto, but they are always eager to extend themselves to encourage and help others find their own inner strength."
        elif single_day_master == 7:
            print "Seven people are your natural born seekers and philosophers, those who seek truth and higher wisdom in all experiences Seven people tend to have a naturally strong intuition, but often struggle with their emotions which can sometimes cloud their judgment unless they learn to work through their emotional sensitivities with honesty. Seven people are often highly intellectual as well and need to learn to balance that with their deep emotions so that they don't become cynical or detached from others."
        elif single_day_master == 8:
            print "Eight people are daring and bold, usually naturally good in business, and they have a knack for making or acquiring money. Eight people are very motivated by success and are quite competitive. They are also prone to being very self-confident, practical and efficient which lends to others trusting them with their business. Eight people are often seen as 'lucky' or having lucky breaks in life - but this is typically due to a natural drive and persistence that helps them attract what they want/need for success."
        elif single_day_master == 9:
            print "Nine people are compassionate, dreamy and idealistic in nature. They are highly creative and often devote themselves to life-long learning. Many people with multiple degrees will have this number; they are never 'finished' or 'masters' as they embrace continued growth and personal expansion. Nine people are visionaries who do best when they learn to assert themselves and master their insecurities. Worldly, creative and ever expansive, nine people often appear larger than life."
        elif single_day_master == 11:
            print " People with master number 11 are exceptionally intuitive and are often naturally drawn to the healing arts. 11 people are compelled with a strong drive towards service to others. Highly sensitive, a dreamer, 11 people have to work hard to stay motivated and take action on their loftier goals."
        else:
            print "People with master number 22 are great builders and organizers. This number means you are gifted with the natural ability to not only visualize a plan but to see hte actual result ahead of time. You are botha  'seer and a doer' and when you properly apply yourself, can see through from start to finish with relative ease. Your perception is keep and you have the right blend of idealism and practicalithy that can take you far."
    break


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

single_year_uno = single_digit_uno(year)
single_month_uno = single_digit_uno(month)
single_day_uno = single_digit_uno(day)


# calculation of challenge numbers

first_chall = abs(single_day_uno - single_month_uno)
sec_chall = abs(single_year_uno - single_day_uno)
third_chall = abs(sec_chall - first_chall)
fourth_chall = abs(single_year_uno - single_month_uno)

print ""
print "Challenge numbers define four life cycles and the related challenges that one has to work to grow through, tendencies and obstacles that will pop up during those cycles. When faced with honesty, these numbers can lend great insight into areas for self improvement and personal growth. Four numbers represent: 1) from birth to approximately age 35; 2) from 35 to approximately 60; 3) primary challenge that one faces throughout life: and 4) from 60 to end of life."
print ""

def chall_meaning(challenge):
    if challenge == 0:
        print "The zero challenge number tends to indicate no one specific area or challenge being greater than others. It can also mean a sort of mixed bag when it comes to minor challenges, but these are all designed to help you find your strength. Zero challenges are more about developing one's strengths and having confidence in your abilities - becoming more well-rounded."
    elif challenge == 1:
        print "The challenge with one is learning to exert your independence and speak out authentically. One people tend ot struggle with the need for approval from others from which they base their own sense of self-worth. The challenge is to value oneself enough to be unique."
    elif challenge == 2:
        print "People with this challenge struggle with balance emotionally. They take criticism very personally and struggle to assert themselves. People with this challenge often shirk responsibility because they don't want the pressure of others depending on them or because they are convinced that they can't handle it. People with this challenge in full force tend to shrink back a lot."
    elif challenge == 3:
        print "People with a 3 challenge number tend to have difficulty finishing what they start. They tend to multi-task in ways that are not effective and have many unfinished projects and goals that they struggle to reach. Three people also tend to go on the defensive easily or 'react' to situations rather than think them through. They have difficulty expressing themselves at times in ways that are healthy and productive."
    elif challenge == 4:
        print "This challenge has a lot to do with procrastination and not working hard enough to reach one's goals. Often this challenge can speak of going for the path of least resistance rather than really pushing your limits. When the 4 is your challenge number, you are being pushed to be more assertive and efficient in your work habits."
    elif challenge == 5:
        print "The 5 as a challenge indicates a high degree of impusliveness and reckless behavior. The 5 is the number for freedom and adventue, but as a challenge, it can indicate a need to tone it down a bit and to attain some discipline and foresight."
    elif challenge == 6:
        print "People with a 6 challenge struggle with perfectionism. They demand too much of themselves and often those around them. As a result, they can come off as cynical, too authoritarian, and too critical. People with this challenge need to learn to lighten up a bit, and unconditional love and acceptance of both self and others are their lessons."
    elif challenge == 7:
        print "Unexpressed emotions, difficulty accpeing concepts that defy 'norms,' and being too overly analytical can be themes of the 7 challenge number. People with this challenge tend to be overly anayltical, dismissing anything that does not coincide with their own sense of logic. As a result, people with a 7 challenge are not as open-minded or open to new experiences as they could or should be."
    else:
        print "Materialism above all else tends to be the theme of the 8 challenge number. People with this challenge give too much importance to material affairs and may rely upon social status and money to provide their sense of self-worth or value. It can be tempting for people with this challenge to resort to less than scrupulous tactics in their business ventures, and they need to work to better balance the material world with their spiritual side."
    return challenge


while True:
    first_chall_text = raw_input("Would you like to know your first challenge from birth to approximately age 35? (Y/N) ")
    if first_chall_text.lower() == "n":
        print "Namaste. Have a great day!"
        break
    elif first_chall_text.lower() != "y":
        print "Input Y or N"
    else:
        print ""
        first_challenge = chall_meaning(first_chall)
        break

print ""

while True:
    sec_chall_text = raw_input("Would you like to know your second challenge from age 35 to approximately age 60? (Y/N) ")
    if sec_chall_text.lower() == "n":
        print "Namaste. Have a great day!"
        break
    elif sec_chall_text.lower() != "y":
        print "Input Y or N"
    else:
        print ""
        second_challenge = chall_meaning(sec_chall)
        break

print ""

while True:
    third_chall_text = raw_input("Would you like to know your third challenge, which is your primary challenge throughout your life? (Y/N) ")
    if third_chall_text.lower() == "n":
        print "Namaste. Have a great day!"
        break
    elif third_chall_text.lower() != "y":
        print "Input Y or N"
    else:
        print ""
        third_challenge = chall_meaning(third_chall)
        break

print ""

while True:
    fourth_chall_text = raw_input("Would you like to know your final challenge in your geriatric years? (Y/N) ")
    if fourth_chall_text.lower() == "n":
        print "Namaste. Have a great day!"
        break
    elif fourth_chall_text.lower() != "y":
        print "Input Y or N"
    else:
        print ""
        fourth_challenge = chall_meaning(fourth_chall)
        break

# calculation of personal year number

from datetime import date

single_current_uno = single_digit_uno(date.today().year)
personal_year_raw = single_current_uno + single_month_uno + single_day_uno
personal_year = single_digit_uno(personal_year_raw)

print ""
print "Personal year number gives insight into what surrounds you for this year cycle and represents various themes and events that will likely occur for you during the year (from your birthday until your next birthday)."
print ""

date(year, month, day)
date.today()