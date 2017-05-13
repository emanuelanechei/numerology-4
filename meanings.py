# definition of a function to display life path meaning based on calculation of life path number


def life_path_meaning(life_path):
    # displays objective of life path number
    print """\nYour life path number is {}. Life path number defines limitations or possibilities in life and gives insights to the direction you'll take and the decisions that will affect the life you lead.\n""".format(life_path)

    # displays meanings based on life path number calculation
    if life_path == 1:
        print """\nYou are all about power! Strong and determined individuals carry this life path number. They are often leaders in business and have great personal ambition.\n
They are motivated by personal success and competition. Highly independent by nature - the person with the 1 life path is often very innovative and creative in his/her thinking. Highly analytical and very sharp, they are natural problem solvers.\n
Number 1s who stray from their paths often end up in clingy co-dependent relationships.\n
The company you keep (10%): Tiger Woods, George Washington, Walt Disney, Steve Jobs, Martin Luther King Jr., Sting\n"""
    elif life_path == 2:
        print """\nYou are all about love. People with life path 2 love to find and maintain balance. They are natural peacemakers and tend to be drawn towards service to others.\n
Often they are too self-sacrificing and struggle to find balance in life when it comes to valuing themselves as much as others. People with this life path number tend to be somewhat reserved and quiet. They have excellent listening skills and tend to be very drawn to music.\n
It is very important for them to get out and socialize. A number 2 who is isolated courts pessimism, lethargy and depression.\n
The company you keep (5%): Tony Blaire, Barrack Obama, Madonna, Amelia Earhart, Tim Burton, Sarah Brightman\n"""
    elif life_path == 3:
        print """\nYou are all about performance! This is the life path number of creative people who are very expressive and unique. They are skilled communicators, naturally charming and attractive to others. They know how to convey ideas.\n
Three people tend to be very optimistic and hopeful people, who encourage and nourish that quality in others. They tend to be very energetic and busy - to the point that they may wear themselves out.\n
Number 3s stray off their life path by giving up their dreams and talents. Many escape into drug abuse or promiscuity to avoid hearing the nagging voice of their true calling to express their talents.\n
The company you keep (10%): Alfred Hitchcock, Celine Dion, Charles Dickens, Rihanna, David Bowie, Jodi Foster\n"""
    elif life_path == 4:
        print """\nYou are all about stability! This is the life path number of the pragmatic organizer - the one who builds, constructs, works hard and who is very diligent and persistent in his/her efforts.\n
People with this life path are considered 'practical' and down to earth. Many workaholic types have the 4 as a life path number. People with this life path tend to prefer to follow established rules and believe in order. They don't tend to like surprises and are rather meticulous.\n
However, self-sacrificing number 4s often demand too much, both of themselves and others, and develop reputations as martyrs or tyrants. Their willpower and stubbornness can also be interpreted as greed and selfishness.\n
The company you keep (8%): Frank Sinatra, Brad Pitt, Bill Gates, Leonardo da Vinci, Margaret Thatcher, Oprah Winfrey\n"""
    elif life_path == 5:
        print """\nYou are all about freedom! Those with a 5 life path are gregarious, fun-loving people who love to be surrounded by others. The 5 life path is a bit free-spirited and enjoys adventure, travel, and diversity.\n
People with this life path often thrive in careers that involve travel or working abroad. They do not do well in office settings or any place that limits their freedom and creative expression.\n
However, 5s tend to be very self-absorbed and unaware of the effect of their actions on other people. As other people often feel tricked or fooled by number 5s, experiencing a series of broken relationships is also often a part of their path. People with this life path sometimes have difficulty with discipline or finishing what they started.\n
The company you keep (10%): Malcolm X, Angelina Jolie, Steven Spielberg, Mick Jagger, Jay-Z, Vincent van Gogh\n"""
    elif life_path == 6:
        print """\nYou are all about nurturing. Those with this life path of 6 are hard workers, tend to have a variety of skills and interests and are very 'direct' in their approach. Sometimes prone to being too hard on themselves, they will push themselves to their limits.\n
Six people are typically very organized and efficient and dislike waste - whether it be wasted time or resources. Those with this life path are sometimes seen as strict or sharp, but in actuality, they do have the best interests of others at heart and love to see people reach their potentical. People with this life path make good personal trainers, drill instructors, etc. because they can push others to their personal limits in ways that are both compassionate and motivating.\n
Sixes that find themselves enslaved to an addicted or mentally ill partner might not be following their true path, as this is a sign that they have become enablers, rather than healers of the diseases.\n
The company you keep (10%): Albert Einstein, Eleanor Roosevelt, Galileo Galilei, Stephen King, Michael Jackson, Thomas Edison\n"""
    elif life_path == 7:
        print """\nYou are all about knowledge! Seven is the life path number of the Seeker. People with this life path number are drawn to the bigger mysteries in life and are always looking for a larger purpose behind their circumstances.\n
Sevens are often psychic or extremely intuitive by nature with an innate ability to see to the heart and soul of others and situations. Seven people tend to love people, but are also very independent, requiring a great deal of solitary time to recharge their batteries. Seven people can be prone to being slow movers and procrastinators and need to work to keep their motivation levels up.\n
A sign that a number 7 has strayed completely off his or her life path is a complete withdrawal from society. In this case, the troubled 7 should try to recognize his/her original ambitions to improve the world through the application of wisdom.\n
The company you keep (12%): Muhammad Ali, Sir Winston Churchill, Diana (Princess of Wales), James Cameron, Bruce Lee, Stephen Hawking\n"""
    elif life_path == 8:
        print """\nYou are all about wealth. Eight is the life path of the natural born leader. These are people who are often very good at business and attracting wealth and favors. Eight people are often visionaries and capable of great things because they can also do the hard work required to make thier visions a reality.\n
Eight people are very capable and inspiring leaders, and people are compelled to follow their lead or be left behind. Eights do better when they don't let their ambitions get the better of their compassionate side - doing so can lead to greed and accumulation of wealth for less noble reasons.\n
Sometimes the pursuit of riches becomes more important than personal relationships and cost them their personal relationships, morality and popularity.\n
The company you keep (10%): Michelangelo, Pablo Picasso, Mary Kate & Ashley Olsen, Anna Nicole Smith, Alexander Graham Bell, Nelson Mandela\n"""
    elif life_path == 9:
        print """\nYou are all about spirituality. Life path 9 is the life path of the humanitarian. A natural born leader by nature, you are compelled to lead and to serve. Your high ideals give you a strong desire to improve the lives of others.\n
You are innovative, visionary, and good at implementing new concepts and ideas. People with this life path sometimes struggle with disappointment when they can't live up to their high ideals. There is a need to learn to accept themselves more because when they do, they are capable of great things.\n
These sophisticated individuals are very selfless souls and are often patient, trustworthy, and honorable from the very beginning to the end of their lives. Sometimes a 9's lofty ideals are presented in a manner that others find absurd. Part of a 9's life path is to express spiritual principles through actions, rather than through preaching or proselytizing.\n
The company you keep (10%): Elvis Presley, Mohandas Gandhi, Mother Teresa, Bob Marley, Jimi Hendrix, Kurt Cobain\n"""
    elif life_path == 11:
        print """\nYou are about enlightenment. Those with this life path number are extremely intuitive and feel a strong connection with others, sometimes to the point that it overwhelms their emotions.\n
Eleven people are very visionary and tend to be great thinkers. Solutions to problems seem to come to them with very little effort and sometimes they don't understand how gifted they are at seeing what is 'hidden' or elusive to others.\n
Many of them are 'wounded healers' who at some point in their life suffer a devastating experience that propels them on the search for spirituality. However, along with these situations, usually comes a lot of toxic emotional baggage and harsh inner critic. It takes many 11s their entire life to rid themselves of the 'chip on their shoulder' and achieve enlightenment.\n
The company you keep (8%): Ronald Reagan, Michael Jordan, Wolfgang Amadeus Mozart, Bill Clinton, Edgar Allan Poe, Robert Downey Jr.\n"""
    elif life_path == 22:
        print """\nYou are a master builder. The strongest of the life path numbers, the 22 carries great potential, but also great weight and responsibility. This number represents those who can be master builders and visionaries, who can rally around a cause and bring people together for the common good.\n
Those with this life path often face weighty decisions at several points in their life where they must embrace the crossroads with confidence and make a choice. Those who are not fully in tune with this higher vibration may find they struggle with choice in life and must work to take the path that challenges them over the path of least resistence.\n
Sometimes they display what looks like insensitivity but actually they are just very focused on their goals. This is part of a spiritual directive to be detached from objects and the outcomes of events.\n
Twenty-two life path people who push themselves and embrace change can live truly astounding, creative lives.\n
The company you keep (5%): Tina Fey, Dalai Lama, Paul McCartney, Matthew McConaughey, Will Smith, Tupac Shakur\n"""


# definition of function to display birth day number


def birth_day_meaning(single_day_master):
    # displays objective of birth day number
    print """\nYour birth day number is {}. Birth day number defines your very special talent or strength that greatly facilitates the fulfillment of your destiny.\n""".format(single_day_master)

    # displays meaning based on birth day number calculation, which is the birth day digits sum down to 1-9, 11 or 22
    if single_day_master == 1:
        print """\nYour birth day number is 1. This birth day signifies natural born leaders, those with a lot of drive and initiative.\n
One people are ambitious, hard working, and often very career focused. One people have a keen intelligence and are quick learners who are able to do things on a grand scale.\n"""
    elif single_day_master == 2:
        print """\nTwo people are very balanced and tend to be natural peace keepers and diplomats. Natural negotiators, 2 people dislike conflict and will work hard to make compromises that benefit everyone.\n
Two people love to do important things behind the scenes and tend to have a good blend of both creative and analytical skills.\n"""
    elif single_day_master == 3:
        print """\nThree people are natural artists and love to express themselves creatively in a variety of forms. Three people are inspiring and display great enthusiasm.\n
Three people have great imagination and vision and are also sharp and able to pick up on subtle details.\n"""
    elif single_day_master == 4:
        print """\nFour people are very hard-working and diligent. They are those who build a strong foundation and like structure and stability.\n
Loyal and genuinely honest, 4 people find others trust and rely upon their quiet strength and strong common sense approach to life.\n"""
    elif single_day_master == 5:
        print """\nFive people are your 'movers and shakers' who long for adventure and new experiences. Five people love and embrace diversity and require a lot of changes to keep them motivated and inspired.\n
Five people can be prone to carelessness at times, but their deep love of adventure and naturally keen social skills make them a joy to know - 'never a dull moment' as the saying goes.\n"""
    elif single_day_master == 6:
        print """\nSix people work hard to walk the 'middle ground' in life and feel the need for balance weighing on them quite often. Naturally artistic and expressive, but highly sensitive, 6 people tend to be very vulnerable to criticism and require a lot of positive reinforcement in life to keep them motivated.\n
They are naturally good at working for compromise, but have a strong sense of duty and don't tolerate excuses or 'victim' mentality in others. 'If they can do it, you can too' is their motto, but they are always eager to extend themselves to encourage and help others find their own inner strength.\n"""
    elif single_day_master == 7:
        print """\nSeven people are your natural born seekers and philosophers - those who seek truth and higher wisdom in all experiences. Seven people tend to have a naturally strong intuition, but often struggle with their emotions which can sometimes cloud their judgment unless they learn to work through their emotional sensitivities with honesty.\n
Seven people are often highly intellectual as well, and need to learn to balance that with their deep emotions so that they don't become cynical or detached from others.\n"""
    elif single_day_master == 8:
        print """\nEight people are daring and bold, usually naturally good in business, and they have a knack for making or acquiring money. Eight people are very motivated by success and are quite competitive.\n
They are also prone to being very self-confident, practical and efficient which lends to others trusting them with their business. Eight people are often seen as 'lucky' or having lucky breaks in life - but this is typically due to a natural drive and persistence that helps them attract what they want/need for success.\n"""
    elif single_day_master == 9:
        print """\nNine people are compassionate, dreamy and idealistic in nature. They are highly creative and often devote themselves to life-long learning. Many people with multiple degrees will have this number; they are never 'finished' or 'masters' as they embrace continued growth and personal expansion.\n
Nine people are visionaries who do best when they learn to assert themselves and master their insecurities. Worldly, creative and ever expansive, 9 people often appear larger than life.\n"""
    elif single_day_master == 11:
        print """\nPeople with master number 11 are exceptionally intuitive and are often naturally drawn to the healing arts. Eleven people are compelled with a strong drive towards service to others.\n
Highly sensitive, a dreamer, 11 people have to work hard to stay motivated and take action on their loftier goals.\n"""
    elif single_day_master == 22:
        print """\nPeople with master number 22 are great builders and organizers. This number means you are gifted with the natural ability to not only visualize a plan but to see the actual result ahead of time.\n
You are both a 'seer and a doer' and when you properly apply yourself, can see through from start to finish with relative ease. Your perception is keen and you have the right blend of idealism and practicality that can take you far.\n"""


# definition of function to introduce challenge numbers


def challenge_intro():
    # displays objective of the challenge numbers and the 4 categories
    print """\nChallenge numbers define four life cycles and the related challenges that one has to work to grow through, tendencies and obstacles that will pop up during those cycles. When faced with honesty, these numbers can lend great insight into areas for self improvement and personal growth.\n
Four numbers represent: 1) from birth to approximately age 35; 2) from 35 to approximately 60; 3) primary challenge that one faces throughout life; and 4) from 60 to end of life.\n"""


# definition of function to display challenge number meaning


def chall_meaning(challenge):
    # displays meaning based on various challenge number calculations
    if challenge == 0:
        print """\nThe 0 challenge number tends to indicate no one specific area or challenge being greater than others. It can also mean a sort of mixed bag when it comes to minor challenges, but these are all designed to help you find your strength.\n
Zero challenges are more about developing one's strengths and having confidence in your abilities - becoming more well-rounded.\n"""
    elif challenge == 1:
        print """\nThe challenge with 1 is learning to exert your independence and speak out authentically. 1 people tend to struggle with the need for approval from others from which they base their own sense of self-worth.\n
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
        print """\nUnexpressed emotions, difficulty accepting concepts that defy 'norms,' and being too overly analytical can be themes of the 7 challenge number.\n
People with this challenge tend to be overly anayltical, dismissing anything that does not coincide with their own sense of logic. As a result, people with a 7 challenge are not as open-minded or open to new experiences as they could or should be.\n"""
    elif challenge == 8:
        print """\nMaterialism above all else tends to be the theme of the 8 challenge number. People with this challenge give too much importance to material affairs and may rely upon social status and money to provide their sense of self-worth or value.\n
It can be tempting for people with this challenge to resort to less than scrupulous tactics in their business ventures, and they need to work to better balance the material world with their spiritual side.\n"""


# definition of function to display personal year meaning


def pers_year_meaning(personal_year):
    # displays objective of the personal year number
    print """\nYour personal year number is {}. Personal year number gives insight into what surrounds you for this year cycle and represents various themes and events that will likely occur for you during the year (from your birthday until your next birthday).\n""".format(personal_year)

    # displays meaning based on personal year number calculation
    if personal_year == 1:
        print """\nThe first of the 9 year cycle, a personal year 1 means a year of major changes and a need to make some decisions and work to embrace the opportunities coming rather than resisting change. A good time to focus on personal growth and making positive changes on that front as well.\n
Avoid procrastination this year as it will have more detrimental effects than usual. Conversely, determination truly pays long-term for efforts made during this cycle.\n"""
    elif personal_year == 2:
        print """\nA personal year 2 indicates slow but steady growth, with patience and persistence required. you may find yourself in competition with others at this time or that you have to work harder to resolve conflicts or find creative solutions to challenges.\n
This can also indicate feeling at a bit of crossroads or some uncertainty. It's important not to let it undermine your goals.\n"""
    elif personal_year == 3:
        print """\nExpansion and continued unfoldment that lead to success are the themes of a personal year 3. This is a good time to embrace partnerships and cooperation with others for common goals and the benefit of the whole.\n
More breathing room and a feeling of a burden being lifted often accompany a personal year 3.\n"""
    elif personal_year == 4:
        print """\nA personal year 4 means a lot of responsibility, hard work, and diligent efforts will be required. Four speaks of 'hands on' effort and making every effort count.\n
This is a year of building solid foundations and likely a year where you may feel you are not accomplishing as much as you actually are. The personal year 4 speaks of ground work and solidifying.\n"""
    elif personal_year == 5:
        print """\nA personal year 5 speaks of a strong desire for change, adventure and trying new things. This is a year where you will be more inclined to travel, move, or even change career paths.\n
This cycle brings out the pioneering spirit and the desire for new experience and expression. This is a personal year cycle where it can be easy to become distracted, and self-discipline is more difficult.\n"""
    elif personal_year == 6:
        print """\nThis personal year cycle tends to focus more on personal relationships. It is an excellent cycle for meeting new people, deepening or finding love with a special someone and otherwise, forming or strengthening lasting bonds with others.\n
You may find that you make new friends or mend fences at this time. A personal year 6 also indicates a phase where you may be called to face yourself with more honesty and work on cultivating more love/respect within.\n"""
    elif personal_year == 7:
        print """\nThe personal year 7 cycle typically rings a period of introspection and more solitude. A time for focusing on personal goals, growth, and expansion.\n
A 7 cycle can mean withdrawing a bit socially to focus on personal issues. A great time for pursuing growth through education, enlightenment, etc.\n"""
    elif personal_year == 8:
        print """\nPersonal year 8 tends to indicate a good cycle for investments, monetary issues, and growth on a more material/career level. The 8 personal year cycle is a great time to focus on increasing business or even starting a new business.\n
It is during this phase that many people find themselves growing financially, getting promotions, and finding and building further success. A cycle of prosperity.\n"""
    elif personal_year == 9:
        print """\nThe personal year cycle 9 says as one thing ends another begins. There is a certain feeling of restlessness and anticipation that can make a 9 personal year a bit uncomfortable for some, particularly for those who have difficulties accepting change.\n
This cycle rings the strong desire to make changes, to clear away areas that are no longer serving your growth and to remove limitations from your life as you prepare to start fresh on a new 1 cycle.\n"""


# definition of a function to display expression/destiny meaning


def exp_dest_meaning(exp_dest):
    # displays objective of expression (destiny) number
    print """\nYour expression (destiny) number is {}. Expression number describes your inherent traits and natural talents. It defines your highest potential and how to make the most of your experience in this life.\n""".format(exp_dest)

    # displays meaning based on expression (destiny) number calculation
    if exp_dest == 1:
        print """\nThis expression number represents the pioneering spirit, the risk taker and someone who is willing to put him/herself 'out there' and try new things. Extroverted (typically) and very self-confident, sometimes even a bit too self-centered.\n
This number speaks of someone with the desire to win, who will work harder than most to reach his/her goals. Independent and competitive - always growing and striving.\n"""
    elif exp_dest == 2:
        print """\nThe natural diplomat is represented with this destiny number. Two people are well-balanced, able to bring people together and reach compromise.\n
They are quite intuitive and can sense the feelings of others which leads to this innate ability for teamwork. Twos embody fairness and balance. They also tend to develop strong musical talents as well due to their natural sense of rhythm and harmony.\n"""
    elif exp_dest == 3:
        print """\nThe 3 expression number speaks of someone who is very theatrical by nature - very expressive, outgoing, and a natural charmer. People with this number are often drawn towards writing, acting, or the arts - anywhere they can express themselves and share their views with others.\n
Threes are capable of abstract thought and can paint pictures easily with words and communication. They have an innate ability to explain complex concepts in a way that is easy for everyone to grasp.\n"""
    elif exp_dest == 4:
        print """\nPeople with a 4 expression number are considered down to earth, practical and orderly. Four people thrive in environments that are well-organized, and they love structure and stability.\n
They are often seen as 'the rock' or pillar strength in their families and businesses because of their strong sense of duty and discipline.\n"""
    elif exp_dest == 5:
        print """\nThe person with the 5 expression number is a natural adventurer - someone who thrives on new experiences and who is a life long seeker and learner through hands on methods. These people are often 'jack of all trades' types who are self-taught in many areas and are always wanting to try something new.\n
The 5 expression number is destined to travel, have a variety of experiences and break free of the societal mold that tells us to 'do one thing' career wise, etc. Fives change their minds often and when they give themselves the freedom to explore, they lead very rich and interesting lives.\n"""
    elif exp_dest == 6:
        print """\nSix people are driven by a strong sense of duty and often put others ahead of themselves. They are called often to careers that allow them to help others - counselors, health care fields, teaching, etc.\n
People with a 6 expression number tend to measure their own sense of self-worth based on what they do for others. They need to be careful to not be too overprotective and to allow others the freedom to make their own choices in life.\n"""
    elif exp_dest == 7:
        print """\nPeople with 7 expression number are very intuitive, intelligent - the seekers of truth and understanding. Seven people tend to be rather introverted and require a great deal of 'personal space' in order to thrive.\n
Seven people are motivated in life by a need for greater understanding and are often drawn to philosophical, spiritual, and/or metaphysical pursuits in their quest for deeper meaning.\n"""
    elif exp_dest == 8:
        print """\nPeople with an 8 expression number are incredibly competitive, ambitious and hard working. Often destined for great successes in life, particularly in their career field.\n
Eight people are excellent managers and builders who are very efficient and effective. They are able to balance strong ambitions with care and concern for others, which allows them to create strong enterprises that serve their communities well.\n"""
    elif exp_dest == 9:
        print """\nPeople with a 9 destiny/expression number are the lofty idealists that inspire us to aim higher. Humanitarian by their very nature, 9 people are typically called to lives of activism and social issues.\n
They are driven by a need to be accepted and loved by others and often become very well known or famous for their efforts. People with a 9 expression number are typically highly artisitc and creative and use those talents to promote a cause.\n"""
    elif exp_dest == 11:
        print """\nPeople with the master number 11 as their expression number are naturally psychic and very intelligent. They have a great blend of logic and creativity and when they can balance these aspects and channel their vast energy in productive ways, nothing can stop them.\n
Elevens have to work hard to keep their higher vibrational energy levels up. Elevens can become too caught up in fantasy over reality as an escape when their emotions overwhelm them. It is very important for people with this expression number and life path to work hard to keep their energy fields in balance.\n"""
    elif exp_dest == 22:
        print """\nPeople with this master number 22 as their destiny number are great at bringing the sacred to the mundane - they can and do embrace all life and experience as a spiritual adventure and put this reverence into everything they build and create.\n
Natural builders, those with a 22 expression number are blessed as visionaries with strong leadership abilities. They can see a project through from start to finish - build what they envision with ease and grace.\n"""


# definition of a function to display soul urge meaning


def soul_urge_meaning(soul_urge):
    # displays objective of soul urge number
    print """\nYour soul urge number is {}. Soul urge number defines your reason for being and what gives you true fulfillment - your very essence or heart's desire.\n""".format(soul_urge)

    # display meaning of soul urge number calculation
    if soul_urge == 1:
        print """\nYour soul urge is to be the best. As you believe you are directly connected to a higher power, you just can't bear it when you let yourself and others down. In your universe you are the sun, and everything and everybody else rotates around you. You live to be the center of attention.\n
One of your soul lessons might be to recognize that 'to rule is truly to serve'.\n"""
    elif soul_urge == 2:
        print """\nYour soul urge is to be admired and loved by all. The height of personal gratification for you is to be desired by a special someone. You have an enormous faith in other people, and if they do let you down, you tend to behave as if it's the end of the world.\n
One of your soul challenges is to realize that only the divine is perfect, and others are not god-like in their actions.\n"""
    elif soul_urge == 3:
        print """\nYour soul urge is about the cultivation and expression of your personality. Usually this energy manifests as a great achievement in the theatrical or atistic world. You shine at any kind of activity that involves public performance including acting, singing or politics.\n
You desire to be admired for your craft, and one of your soul challenges might be to recognize that there will always be a critic.\n"""
    elif soul_urge == 4:
        print """\nStability, beauty and order satiate your soul. You find a zen-life satisfaction in performing the simplest of repetitive chores as you feel closest to the divine when you are restoring harmony to unbalanced situations. You are a perfectionist that loves art and design.\n
One of the challenges of your number is that sometimes others don't understand your need for everything to be perfect and see you as controlling.\n"""
    elif soul_urge == 5:
        print """\nChange rules the fires of your inner passions. You have an inquisitive mind and a thirst for adventure that is only satisifed by the collecting of unusual experiences and plenty of travel. You appreciate the fact that life is short and are bound and determined to make the most of every minute you have on this earth.\n
One of the challenges of this soul number is setting down real roots and foundations in life.\n"""
    elif soul_urge == 6:
        print """\nYour soul urge is to nurture and take care of others. You love people and believe the greatest expression of your inner divinitiy is through teaching and guidance. You are happiest when you see the positive results of your influence blossom in other people. However, you also have a tendency to become very attached to a perceived soulmate.\n
One of your challenges is to learn to 'let go' when relationships end.\n"""
    elif soul_urge == 7:
        print """\nThe highest calling of your soul is to learn about everything scientific and esoteric. It is knowledge that feeds your soul. You love to read, and subjects such as history, science, metaphysics, physics, archaeology and religion fuel your rich imagination with inspiration and ideas.\n
Many of you are geniuses, and because of this, one of the challenges of your number is to be understood by a stupid world.\n"""
    elif soul_urge == 8:
        print """\nYour soul urge is to 'go forth and multiply' especially when it comes to family dynasties and aggregating wealth. The highest expression of your soul urge number is when you are in power and improving the lives of those that work for you or love you. You support anything that brings beauty, meaning and profit to the world.\n
The challenge of this number is to realize that 'money isn't everything'.\n"""
    elif soul_urge == 9:
        print """\nThe highest expression of your soul's urge is to connect in a mystical way with others. Although your aspirations are lofty, you are also a humanitarian who is often gifted with a sharp intuition and keep analytical skills. Your fatih in yourself, the divine and the future is so strong that you live by your convictions.\n
Your challenge in life is to be understood as more than a fanatic or flake by others who may not understand your idealism.\n"""
    elif soul_urge == 11:
        print """\nYour soul's purpose is to manifest ideals into reality. Your highest calling is to become the master of a religion or of a spiritual realm. You are the ultimate seeker of truth and will go to any lengths to find a spiritual teacher or guru.\n
This search often leads you on a path that is full of many pitfalls and disappointments as you realize that one spiritual system doesn't work for you or that a guru or teacher is only human after all.\n"""
    elif soul_urge == 22:
        print """\nYou have the highest soul calling of all of the numbers, as it is the call to transform the world permanently and for the better. Usually you are born with all of the tools that you need to accomplish this including a stable personality, intelligence, courage and charisma.\n
Perhaps the most healing thing for your soul is simply to read out loud the words of ancient texts as these writings resonate very strongly with the noblest apsirations of your higher self.\n"""


# definition of a function to display personality meaning


def personality_meaning(personality):
    # displays objective of personality number
    print """\nYour personality number is {}. Personality number defines how you present yourself to the public and how others perceive you.\n""".format(personality)

    # displays meaning of peronality number calculation
    if personality == 1:
        print """\nAmbitious, strong-willed and determined. A natural leader who commands attention and usually rises to the forefront of the group. When they have a strong sense of purpose, they are very inspiring and motivating.\n
When they don't, they can appear egotistical or attention starved.\n"""
    elif personality == 2:
        print """\nFair-minded and well-rounded. Two people are seen as trustworthy and reliable. People with this personality number are often asked for help by strangers or approached because they have an openness about them and a caring demeanor.\n
Sometimes they are seen as indecisive because they carefully weigh all things before making decisions.\n"""
    elif personality == 3:
        print """\nCreative and articulate, 3 people are seen as interesting and great story tellers. Three people seem to have a knack for finding opportunities and can always see a silver lining in the clouds.\n
People see them as creative thinkers who sometimes get carried away or may be prone to a bit of exaggeration to highlight their point.\n"""
    elif personality == 4:
        print """\nStability and a solid foundation. People with this personality are pillars of strength who are well-organized and structured.\n
People tend to view them as having the answers and being knowledgeable. Four people are considered reliable and steady - sometimes a tad too predictable or serious.\n"""
    elif personality == 5:
        print """\nFive personalities are community leaders who take an active interest socially and love to be involved with others. They are adventurous, highly passionate people who love to travel and immerse themselves in different cultures.\n
Five people are seen as stimulating, interesting, but not always the most reliable or dependable. They tend to do their own thing on their own time.\n"""
    elif personality == 6:
        print """\nThe 6 personality is someone who loves to help others and who will give of him/herself tirelessly when needed. They love to see others reach their personal best. Six people are typically peacemakers and try to avoid conflict. They can fit in well with a variety of people and are very easy going and agreeable.\n"""
    elif personality == 7:
        print """\nThe 7 personality tends to be somewhat introverted. They are keenly observant and highly intelligent. This ability to 'see through' people, coupled with their intelligence/observation skills, can make them intimidating to others initially. Seven people are seekers of truth, highly opinionated, but always looking for the greater wisdom in all experience.\n
People often see them as wise or 'old souls'.\n"""
    elif personality == 8:
        print """\nThe 8 personality is very ambitious and competitive, but typically good-natured about it. They appear confident, lucky, and highly resourceful. Eight people love to push themselves to reach consistently higher goals. They are very good at envisioning and developing projects.\n
People see them as well rounded and having good business sense.\n"""
    elif personality == 9:
        print """\nThe 9 personality is naturally charming, very well-versed in many subjects, and very idealistic and positive. This personality is seen as conscientious, inspiring and having a strong charisma and influence.\n
9 personalities tend to be naturally able to lead groups of people and others tend to gravitate towards their strong positive energy.\n"""
    elif personality == 11:
        print """\nEleven personalities go to great lengths to hide their inner shyness and nervousness. Highly intuitive and emotional, the 11 personality is a soul who radiates warmth and genuine kindness.\n
People often gravitate to this person for their gentle spirit.\n"""
    elif personality == 22:
        print """\nThis master number equates to someone who is both highly creative and intuitive, but also deeply practical and hard working. People with this personality number crave consistency and balance in their lives and will work hard to achieve it.\n
The person with a 22 personality number often does not give him/herself enough credit and doesn't fully recognize the extremely strong energy which they possess. Twenty-two is capable of great creative accomplishments due to their talent and discipline.\n"""


# definition of a function to display hidden passion meaning


def hid_pass_meaning(hid_pass):
    # displays objective of hidden passion number
    print """\nYour hidden passion number is {}. Hidden passion number defines your greatest natural talents, strengths and motivations. They are strengths that are readily available to you, that you can easily develop and use throughout your life.\n""".format(hid_pass)

    # displays meaning of hidden passion number calculation
    if hid_pass == 1:
        print """\nThis person is driven by a strong individualism and need to stand out in the crowd and get noticed. Ambitious and motivated, those with this hidden passion number are natural leaders.\n"""
    elif hid_pass == 2:
        print """\n2 people are natural peacemakers and negotiators who strive to create harmony in the family, workplace, and wherever they may go. People naturally gravitate to you because they feel a strong innate sense of trust.\n
You are patient and persistent. Two people are naturally inclined towards music and the arts.\n"""
    elif hid_pass == 3:
        print """\nThe 3 person is a natural born entertainer who is very social. You have a natural charm which is alluring to others. Three people are naturally gifted creatively and are often multi-talented in various forms of art, music, writing, etc.\n"""
    elif hid_pass == 4:
        print """\n4 people are extremely diligent, determined hard-workers, and for this reason, they are capable of uilding great successes from the ground up. Practical, disciplined, and seen as a great provider or support sytem to others.\n
You are 'the rock' of your family/group. Four people are very organized and efficient and need a sense of order in their lives.\n"""
    elif hid_pass == 5:
        print """\nFive is the number of those who love adventure and new experiences. People with this number love to indulge the senses and are natural communicators. Many are drawn to writing and other forms of communication.\n
People with this number can be prone to being a bit too impulsive at times and need to work to cultivate self-discipline. Five people thrive on change in life and often struggle when they feel they have to 'choose' one path.\n"""
    elif hid_pass == 6:
        print """\nSix people have a natural call to service and are often healers, counselors, teachers, etc. Responsibble and self-sacrificing, 6 people have an inner need to be recognized and valued by others in order to feel a strong sense of self-worth.\n"""
    elif hid_pass == 7:
        print """\nSeven people are naturally intuitive and highly intelligent. They are the thinkers who seek the deeper meanings behind experience and are often drawn to philosophy, metaphysics, psychology and any area that explores the subconscious or hidden truths. Seven people are often sought out for their insight and keen understanding.\n"""
    elif hid_pass == 8:
        print """\nEight people are natural salesmen and business people. They have an innate drive that pushes them to accomplish great things. The right blend of vision and ambition, people with an 8 passion are driven by material success and the need to compete with themselves and others. No other number is as energetic and motivated by winning/reaching goals.\n"""
    elif hid_pass == 9:
        print """\nNine people are visionaries with a deep sense of humanitarianism. They have lofty ideals and strive to make their communities and even the world a better place.\n
Highly emotional and idealistic, it can be difficult for 9s to bring their ideas down to earh in a more practical way. Nines see the future and have great vision and need to surround themselves with those who can help them actually manifest these goals/dreams.\n"""


# definition of a function to display karmic meaning


def karmic_meaning(karmic):
    # displays objective of karmic number
    print """\nYour karmic number is {}. Karmic number reflects your subconscious and highlights your deepest fears and insecurities. It shows you what you need to work to overcome during this lifetime.\n
It gives insights into hopes and dreams, as well as fears, to show you where to focus your energy for spiritual growth.\n""".format(karmic)

    # displays meaning of karmic number calculation
    if karmic == 1:
        print """\nThis number speaks of learning to be more independent and able to stand on your own. Karmic number 1 can indicate a tendency to become too dependent on others.\n"""
    elif karmic == 2:
        print """\nThe karmic number 2 has to do with learning to trust your instincts and intuitions. You struggle with choices and need to learn to develop confidence in your decision making.\n"""
    elif karmic == 3:
        print """\nThe 3 karmic number must learn balance between work and play. Organization and managing one's time and resources effectively and efficiently can be a challenge for those with a 3 karmic number.\n"""
    elif karmic == 4:
        print """\nThe 4 karmic number speaks of someone who may need to work harder than others at times in order to be successful. This number speaks of pushing oneself to new limits through effort and perseverance despite obstacles.\n"""
    elif karmic == 5:
        print """\nThe 5 karmic number points to a tendency towards overindulgence and addiction. It is very important for people with this karmic number to learn the true meaning of moderation and to avoid excesses in life which can quickly grow out of control.\n"""
    elif karmic == 6:
        print """\nThe 6 karmic number speaks of obligation and loyalty to family and domestic duties. People with this karmic number often face challenges with certain family members and may also struggle with meeting familial obligations.\n"""
    elif karmic == 7:
        print """\nThe 7 karmic lesson number speaks of developing more spiritually and coming to a place where you feel ready and able to seek your own truth without being swayed by the judgements of others.\n"""
    elif karmic == 8:
        print """\nThis is the karmic number that deals with prosperity and abundance and learning to appreciate what one has been given. People with this karmic number often struggle with money in life until they learn to focus on gratitude and simple abundance, which in turn draw true prosperity.\n"""
    elif karmic == 9:
        print """\nThis karmic number deals with learning to be more selfless and put others needs ahead of your own desires. Nine is the number of the humanitarian who is called in life to help the suffering and struggling. They often develop their empathy for others through difficult experiences of their own in life.\n"""


# definition of a function to display cornerstone/capstone meaning


def cc_meaning(letter):
    # displays meaning of cornerstone and capstone based on first and last letter of first name
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
        print """\nYou are motivated and self-confident. You prefer to take action over sitting back and show great initiative. Sometimes there is a tendency towards impulsive behavior.\n"""
    elif letter == "k":
        print """\nYou are strong-willed and emotional. You are also able to pick up on subtle insights that others often miss and are very perceptive.\n"""
    elif letter == "l":
        print """\nYou have strong social skills and are naturally attractive to others. Easy going and appreciative of the simple things in life.\n"""
    elif letter == "m":
        print """\nYou are considered practical and hard working - a problem solver who doesn't shy away from a challenge. M people are quite independent, but can still work well with others when necessary.\n"""
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
        print """\nYou are creative and passionate in all you do and have a tendency towards strong desires that can make moderating behaviors more challenging for you. Truly unique and deeply in tune to your emotions, you experience richness in all life's experiences.\n"""
    elif letter == "y":
        print """\nYou are a freedom loving person who does not accpet limitations or allow anything to hold you back. You are ambitious and independent with a keen intuition.\n"""
    elif letter == "z":
        print """\nYou are an optimist who has great vision, but are ale to balance that with rational thought and ojectivity. Your compassion and kindness are like a magnet to others.\n"""


# definition of a function to display generic compatibility based on life path number


def comp_gen(life_path):
    # displays generic compatibility table based on life path number
    # displays note that life path numbers are reduced to single digit for relationship purposes
    print """\nFor relationship purposes, life path numbers are reduced to single digits (e.g., master numbers 11 and 22 are reduced to 2 and 4, respectively).\n"""

    if life_path == 1:
        print """\n     Very good combination: 3 and 5"""
        print """     OK combination: 2 and 6"""
        print """     Could go either way: 1, 7 and 9"""
        print """     Challenging combination: 4 and 8\n"""
    elif life_path == 2:
        print """\n     Very good combination: 2, 4 and 8"""
        print """     OK combination: 1, 3 and 6"""
        print """     Could go either way: 7"""
        print """     Challenging combination: 5 and 9\n"""
    elif life_path == 3:
        print """\n     Very good combination: 1 and 5"""
        print """     OK combination: 2, 3, 6 and 9"""
        print """     Could go either way: 4 and 8"""
        print """     Challenging combination: 7\n"""
    elif life_path == 4:
        print """\n     Very good combination: 2 and 8"""
        print """     OK combination: 6 and 7"""
        print """     Could go either way: 3 and 4"""
        print """     Challenging combination: 1, 5 and 9\n"""
    elif life_path == 5:
        print """\n     Very good combination: 1, 3 and 7"""
        print """     OK combination: 5"""
        print """     Could go either way: 6"""
        print """     Challenging combination: 2, 4, 8 and 9\n"""
    elif life_path == 6:
        print """\n     Very good combination: 6 and 9"""
        print """     OK combination: 1, 2, 3, 4 and 8"""
        print """     Could go either way: 5"""
        print """     Challenging combination: 7\n"""
    elif life_path == 7:
        print """\n     Very good combination: 5 and 7"""
        print """     OK combination: 4"""
        print """     Could go either way: 1, 2 and 9"""
        print """     Challenging combination: 3, 6 and 8\n"""
    elif life_path == 8:
        print """\n     Very good combination: 2, 4 and 8"""
        print """     OK combination: 6"""
        print """     Could go either way: 3"""
        print """     Challenging combination: 1, 5, 7 and 9\n"""
    elif life_path == 9:
        print """\n     Very good combination: 6 and 9"""
        print """     OK combination: 3"""
        print """     Could go either way: 1 and 7"""
        print """     Challenging combination: 2, 4, 5 and 8\n"""
    else:
        print """\nBetter luck next time!\n"""


# definition of a function to display life path compatibility based on combinations


def comp_life_meaning(life_path_1, life_path_2):
    # displays compatibility based on various combinations of life path numbers of individual and partner
    # displays note that life path numbers are reduced to single digit for relationship purposes
    print """\nFor relationship purposes, life path numbers are reduced to single digits (e.g., master numbers 11 and 22 are reduced to 2 and 4, respectively).\n"""

    # the following are "very good" pairings
    if ((life_path_1 == 1) and (life_path_2 == 3)) or ((life_path_1 == 3) and (life_path_2 == 1)):
        print """\nThis is a very lively couple, and there is little negative to say about this combination. The 3 is good at acknowledging the 1's accomplishments and stroking the ego.\n
The creative 3 provides the ideas and the light hearted, anything goes attitude, while the 1 provides the originality and the push, making this combination one of happiness and mutual pleasure for a long time.\n
Despite the positive aspects, there are some pitfalls they have to be careful about, but overall this is a well balanced combination.\n"""
    elif ((life_path_1 == 1) and (life_path_2 == 5)) or ((life_path_1 == 5) and (life_path_2 == 1)):
        print """\nThe compatibility of these two numbers is about as good as it gets. There will never be any danger of boredom, complacency, or emptiness in a relationship that has heads turning and people whispering.\n
Both of these numbers like to have a lot of freedom in a relationship, and the one real threat is they try to impose their will on one another. The personality traits in this combination can both create and destroy, but like wind and fire, the 1 and 5 feed on each other and respect each other's powers, and when they set out side by side to fulfill their goals and dreams, nothing can withstand their combined forces.\n
This is a relationship of intensity and moments of rarely achieved highs, where the promise of ecstatic experiences of love, spiritual bonding and shared dreams is very real.\n"""
    elif life_path_1 == life_path_2 == 2:
        print """\nThis is a great match of two souls who have a healthy respect for the power of feelings and emotions. You should have little difficulty finding common ground on just about any issue that might arise.\n
The only word of caution for this pairing is that as two people who feel and experience emotions strongly, they must each remember how thin their own skin and realize how vulnerable you both are to criticism. You may need to consciously work on this in order to prevent verbal injury to one other.\n
Generally this is not a problem because of your mutual respect and the ability to relate to each other's emotional experiences.\n"""
    elif ((life_path_1 == 2) and (life_path_2 == 4)) or ((life_path_1 == 4) and (life_path_2 == 2)):
        print """\nAlthough perfection is not easy, if not impossible to find, and your relationship, just like any other is not without difficulty, this is one of the best combinations possible. This is a good pairing resulting in comfort personified.\n
When it comes to home and family, the 4 is the ultimate builder and provider. Four's grounded and practical perspective complements the 2's sensitive and intuitive side, bringing a healthy balance to the relationship.\n"""
    elif ((life_path_1 == 2) and (life_path_2 == 8)) or ((life_path_1 == 8) and (life_path_2 == 2)):
        print """\nThis number combination usually works out well. Because it is likely that each of you has a clear vision of your role, this relationship is often seen as the classic traditional family model, where the female 2 takes care of the family, and the male 8 takes care of the financial needs ... or in the case of the male being a 2 and female an 8, the classic male/female role reversal.\n
Regardless of the roles, this combination's qualities can produce a balanced relationship, and when these two unite their individual strengths, you have the potential of a rewarding relationship that lasts for years and years.\n"""
    elif ((life_path_1 == 3) and (life_path_2 == 5)) or ((life_path_1 == 5) and (life_path_2 == 3)):
        print """\nThe 3 and the 5 get along very well, making this is an excellent combination. You both communicate well, and the two of you will generally find each other's company interesting and enjoyable.\n
Numerous activities, such as social events and travel, will keep this relationship from getting boring. The downfall, or rather dangers, of this pairing is because you are so compatible, you may end up enhancing each other's less desirable traits.\n"""
    elif ((life_path_1 == 4) and (life_path_2 == 8)) or ((life_path_1 == 8) and (life_path_2 == 4)):
        print """\nBecause both parties know how to work hard, and have a good head for getting ahead in the world, this is a very good combination, not only in romance, but also in business.\n
This is a couple that knows how to build for the future and develop a very secure relationship. Like in any other number combination, dangers do exist, and feelings of frustration can overshadow the love and respect that is the foundation of this relationship, but overall this is an excellent number pairing.\n"""
    elif ((life_path_1 == 5) and (life_path_2 == 7)) or ((life_path_1 == 7) and (life_path_2 == 5)):
        print """\nThis is a combination of two numbers that can fulfill each other's needs and desires in many ways. The 7 enjoys its alone time, and the 5 is a busy body that appreciates the lack of demands for attention from its partner.\n
When together, the pairing is able to find a stream of mutual interests to discuss and explore, particularly on the intellectual and spiritual planes, making this one of the best combinations for a long lasting relationship.\n"""
    elif life_path_1 == life_path_2 == 6:
        print """\nThis is a very good, highly committed number pairing. Just like in any other relationship, there will come a time when obstacles will need to be overcome; however, because of the harmonious and loving nature of the 6, this is a combination charged with romance, and one that has a very good chance to form a strong, long lasting romantic relationship.\n"""
    elif ((life_path_1 == 6) and (life_path_2 == 9)) or ((life_path_1 == 9) and (life_path_2 == 6)):
        print """\nWhen 6 and 9 are found between two partners, the compatibility is usually very good. It is important that your respective negative traits aren't allow to grow and fester, creating an environment where you are more likely to clash.\n
The give and take compromise is something you will need to do, in order to prevent unnecessary arguments from escalating, but because both of you are self-sacrificing, caring people, this is something that is not hard for either of you to do. Overall this is a highly compatible match.\n"""
    elif life_path_1 == life_path_2 == 7:
        print """\nNo one understands the psyche of a 7 nearly as well as another 7. This is an excellent combination of two people who take life's mysteries seriously. With the right attitude, you will happily explore the world, or spend quiet days in solitude together.\n
This is a beautiful pairing with potential for spiritual growth for both partners, and one where the term 'soul mates' often applies.\n"""
    elif life_path_1 == life_path_2 == 8:
        print """\nThis is a good pairing, not only in romance, but also in business. Having two 8s in a relationship puts each of you in a position where you are well suited to support each other.\n
The pitfalls arise when you find yourselves competing with one another, or when you are both financially strapped. If you are able to unite your competitive natures against other forces, and follow your heart and intuition in the pursuit of success, this pairing has a strong chance of a long and happy relationship.\n"""
    elif life_path_1 == life_path_2 == 9:
        print """\nThe compatibility between two 9s is excellent, and offers much promise for a very happy, inspiring, and engaging relationship.\n
The many similarities, coupled with the selfless nature of the 9, make for a combination that faces very few challenges. Despite some pitfalls that may exist, this number set has great potential to form an unbreakable bond ... one that will not weaken over time.\n"""
    # the following are "ok" pairings
    elif ((life_path_1 == 1) and (life_path_2 == 2)) or ((life_path_1 == 2) and (life_path_2 == 1)):
        print """\nThis meeting of two very different people is a very promising combination, with the key being mutual respect and sincerity. One, being strong, driven, competitive, and sometimes overbearing, is best equipped to be the leader, to be the motivating force. The 2, being sensitive, insightful and supportive, is by nature the 'power behind the throne', allowing the 1 to throw some weight around without losing sight of what has to be done and how to do it.\n
There is no power struggle, both of you know what you want, and you complement each other very well.\n"""
    elif ((life_path_1 == 1) and (life_path_2 == 6)) or ((life_path_1 == 6) and (life_path_2 == 1)):
        print """\nThis is a combination that has the potential for a long lasting relationship, without ever going through the kind of turbulence so many other relationships experience. The important thing for both 1 and 6 is to understand that they are very different in the way they view human qualities.\n
Their priorities differ and if they are able to keep an eye open for their differences, and are able to work past this roadblock, this can be a successful pairing ...the key is to value their respective good qualities, and give each other the support they both need.\n"""
    elif ((life_path_1 == 2) and (life_path_2 == 3)) or ((life_path_1 == 3) and (life_path_2 == 2)):
        print """\nMore often than not, the combination of 2 and 3 enhances each other's creative juices, potentially making this is a very good partnership. While the 3 is full of life and social energy, the 2 is happy standing back and enjoying the show, and as long as the 3 can keep its verbal impulses under control, and the 2 has enough confidence to handle occasional criticism, the relationship has every chance of bringing love and joy to both of you.\n"""
    elif ((life_path_1 == 2) and (life_path_2 == 6)) or ((life_path_1 == 6) and (life_path_2 == 2)):
        print """\nThis is in general a good compatibility match. The 6's priorities lie with family, to care for and comfort your loved ones, while the 2 is a sensitive, emotionally aware number, enabling you both to love easily and without holding back, forming a strong foundation for a long lasting relationship.\n
Despite these common traits that bring a positive energy to your relationship, you both need to watch your own negative traits, such as 6's need for approval and praise, or 2's insecurity and occasional bouts of jealousy and envy. With these under control, and with considerations of feelings for each other on both sides, the likelihood of a clash in less likely than in most other number combinations.\n"""
    elif life_path_1 == life_path_2 == 3:
        print """\nHappy go lucky, interesting, and creative ... describes this pairing of two numbers who joke easily, and know how to please each other, while at the same time being able to enjoy each other's company within your dynamic social environment. This is a fun pair that understands and supports one another.\n
Troubles might arise, however, when the question becomes as to who is going to take care of the mundane tasks. You both have a tendency to skim over the rough spots, and when fun and joy become too high a priority and neither partner is willing, or able, to take care of the practical everyday details, this can destabilize the foundations and bring friction to your relationship.\n"""
    elif ((life_path_1 == 3) and (life_path_2 == 6)) or ((life_path_1 == 6) and (life_path_2 == 3)):
        print """\nThis combination is a creative couple, with an active social life. The 3, full of enthusiasm and sense of humor, and the 6 providing the warmth, support, and self sacrificing love, makes this combination an ideal team that will work well in most cases.\n
The chemistry here is very strong, but while there is no lack of emotion, the pitfall here is the possibly excessive emotional bond experienced by the 6. Usually it will be the 6 who will have to learn to deal with this inborn trait, and allow the 3 enough space and freedom to move and breathe.\n"""
    elif ((life_path_1 == 3) and (life_path_2 == 9)) or ((life_path_1 == 9) and (life_path_2 == 3)):
        print """\nThe pairing of a 3 and a 9 is a combination of two people who, through their powerful imaginations, are able to keep each other endlessly engaged in a variety of creative ways. Despite the occasional self-centered and egocentric tendency of both numbers, this combination reflects excellent compatibility.\n
The problem the couple faces is when they are both vying for the same limelight, and despite the fact that privately they respect and like each other, they can become very competitive, in which case they will do almost anything to win.\n"""
    elif ((life_path_1 == 4) and (life_path_2 == 6)) or ((life_path_1 == 6) and (life_path_2 == 4)):
        print """\nDespite the common traits shared by this pairing, it is usually not very common for these two numbers to fall in love. However, because you are both responsible and family oriented, and you both value stability and security. If you do get involved in a romantic relationship, it is usually a strong, comfortable match straight from the beginning, with potential to last for a life time.\n"""
    elif ((life_path_1 == 4) and (life_path_2 == 7)) or ((life_path_1 == 7) and (life_path_2 == 4)):
        print """\nThis combination is one in which the earth meets the heaven, and just like earth and heaven, the two of you can't exist without one another. There are some sharp angles that will need to be rounded off, but this pairing, which makes life both secure and at the same time more interesting for both of you, can much more easily overcome the challenges inherit in every relationship.\n"""
    elif life_path_1 == life_path_2 == 5:
        print """\nThe two 5s form a very comfortable match. This is a relationship that is tolerant, easy going and flexible, and in which both of you take your commitment to each other seriously, allowing you to weather many storms.\n
The dangers of this pairing come from within, and it is the adventurous, freewheeling lifestyle, which is normally a plus, that can cause difficulty in focusing on the mundane day-to-day affairs, and can lead to somewhat of a wild streak that can include drugs, alcohol, and other such vices.\n"""
    elif ((life_path_1 == 6) and (life_path_2 == 8)) or ((life_path_1 == 8) and (life_path_2 == 6)):
        print """\nThe practical, goal oriented, and responsible nature of these two numbers makes this a very positive and compatible pairing. The dangers lay in the different ways the 6 and the 8 view responsibility, and how they go about accomplishing their goals.\n
The 6 is more oriented on family and friends, while the 8 is more focused on the executive lifestyle and the obligations that come with it. Despite these differences, the combination is all together a very good match.\n"""
    # the following could go either way
    elif life_path_1 == life_path_2 == 1:
        print """\nBoth of you are head strong, with a strong desire to lead, which can make this a challenging combination. Even though as 1s you might understand each other's needs, and share things in common, in this case this is not necessarily an advantage.\n
This is a relationship of extremes with either partner refusing to surrender their leadership qualities, and the match can get dicey, especially when they start to compete, particularly at the onset of the relationship.\n
Despite this 'butting of heads', when two people with such driving forces do get along, and their mutual competitive streaks are overcome, this can be a very ping combination.\n"""
    elif ((life_path_1 == 1) and (life_path_2 == 7)) or ((life_path_1 == 7) and (life_path_2 == 1)):
        print """\nOne and 7, your compatibility is unpredictable ... some relationships between 1s and 7s thrive while others don't stand a chance.\n
The initial connection in this combination is usually intellectual - a level where you can relate and have plenty to share. One's willingness to get off the beaten path, and open and unconventional mind make for a great intellectual partnership with 7.\n
You are two people who happily venture into new, strange or unknown intellectual and spiritual territories, and if you happen to click, this can lead to a very promising combination. Free thinkers, for very different reasons, driven by very different perspectives, and with very different energies, somehow blend nicely to make a nice, spicy recipe.\n"""
    elif ((life_path_1 == 1) and (life_path_2 == 9)) or ((life_path_1 == 9) and (life_path_2 == 1)):
        print """\nDue to the fact that both of you have a tendency towards arrogance, as well as to being somewhat egocentric, this is a very difficult relationship, as far as romance is concerned. It will only work if a certain amount of distance is maintained.\n
Each of you has to live your own life. Ironically, although difficult, this is not a bad combination for most other kinds of relationships. Friendships, parent-child, as well as business relationships, often work very well with this combination.\n
One and 9 stand on opposite ends of the spectrum ... they complement and balance each other. Together, they represent a lot of talents and useful qualities that ensure a powerful combination in most relationships, except in romance.\n"""
    elif ((life_path_1 == 2) and (life_path_2 == 7)) or ((life_path_1 == 7) and (life_path_2 == 2)):
        print """\nThis is a unique combination that has both strong and dissimilar needs, a combination where intuition meets intelligence, sensitivity meets analysis, and the heart meets the mind. Although these two numbers rarely express interest in one another, when they do, the result can often lead to a relationship that's welded for life.\n"""
    elif ((life_path_1 == 3) and (life_path_2 == 4)) or ((life_path_1 == 4) and (life_path_2 == 3)):
        print """\nThe pairing of 3 and 4 can lead to either a promising, or a very difficult and challenging combination. When the spontaneous 3 pairs with the grounded 4, something has to give, and often it won't. The 3 is an optimistic, fun loving number, one of 'go with the flow' attitude that takes each day as it comes. The 4 on the other hand is more disciplined, practical, and has a definite plan for the future.\n
If the two of you can ever figure out how to meet in the middle, and balance each other's shortcomings, this can be a good combinations. However, when life becomes a challenge and wordly problems arise, the 3 and 4 are a pair least prepared to deal with them.\n"""
    elif ((life_path_1 == 3) and (life_path_2 == 8)) or ((life_path_1 == 8) and (life_path_2 == 3)):
        print """\nThis is a combination where the number set is compatible in some areas and incompatible in others; therefore, this relationship requires a bit of extra effort. Because of the 3 and the 8 having very different views as to what is important in life, unless they learn to respect each other's needs and expectations, the relationship will not last long.\n
Despite this, because you complement each other well, more often than not, you can get along very well and can be quite compatible.\n"""
    elif life_path_1 == life_path_2 == 4:
        print """\nThis is a stable pairing; however, because of the nature of the 4, you both tend to get somewhat irritated when established routine is disturbed. This can lead to a relationship that is either very good, or extremely stressful, with little room in the middle, and so the compatibility can depend largely on how compatible your daily routines are.\n
Upside of this pairing is stability and security ... the downside is that it is hard to relax, be spontaneous, and enjoy the moment.\n"""
    elif ((life_path_1 == 5) and (life_path_2 == 6)) or ((life_path_1 == 6) and (life_path_2 == 5)):
        print """\nThis combination of numbers is a match that is usually very physical and sensual. The 5's freedom loving nature and 6's grounding force can complement each other well, but only if both of you are willing to compromise.\n
If you can find a way to meet in the middle, avoid the tendency to become stuck in your individual positions, and live a lifestyle that is in harmony with that of your partner, this can be a promising relationship.\n"""
    elif ((life_path_1 == 7) and (life_path_2 == 9)) or ((life_path_1 == 9) and (life_path_2 == 7)):
        print """\nThis combination is somewhat neutral as far as compatibility is concerned. There is neither like nor dislike between you two.\n
Discourse can arise when your positions on religion and spirituality are not in harmony with one another, or when your different tastes in general are questioned by one another.\n
On the plus side, because of your unique energies, there is otherwise rarely any kind of friction, and conflicts are dealt with reasonably.\n"""
    # the following are "challenging" pairings
    elif ((life_path_1 == 1) and (life_path_2 == 4)) or ((life_path_1 == 4) and (life_path_2 == 1)):
        print """\nOne's and 4's strengths can make for a solid relationship for a long time only to crash and burn in the blink of an eye.\n
This can be a thriving relationship as long as 1 doesn't start on a path of unknowns and risky, questionable results. However, that will unavoidably happen, and 4 will at times be seen as a 'stick in the mud', a source of frustration for 1. When this kind of situation becomes overwhelming, it will almost certainly bring this relationship to an end.\n
On the other hand, as long as 1 is able to respect 4's need for a secure, perhaps even predictable, lifestyle, and 4 can understand 1's need to try new avenues, take risks, occasionally venture out into unknown territories, the relationship can endure.\n"""
    elif ((life_path_1 == 1) and (life_path_2 == 8)) or ((life_path_1 == 8) and (life_path_2 == 1)):
        print """\nFrom the love angle, this combination is questionable at best. Both of you are strong-willed, assertive and demanding, while at the same time stubborn people ... it's like having two captains on deck ... which leads to uneasiness, discomfort and distress.\n
Neither one of you accepts anything less than full respect and an equal playing field, and neither one of you can be dominated or would accept being someone's sidekick. Even though both of you may share many common interests, any negative feedback from either of you can be deadly in this pairing.\n
Success depends on a mutual willingness to compromise and limit demands, otherwise small arguments can be blown out of proportion.\n"""
    elif ((life_path_1 == 2) and (life_path_2 == 5)) or ((life_path_1 == 5) and (life_path_2 == 2)):
        print """\nThis is a combination where the chemistry has to be very strong in order for the two very different souls to forge some significant compromises. Like fire and water, when 2 and 5 occupy the same space, either the fire makes the water evaporate, or the water drowns out the fire.\n
Although the two numbers can provide a lot for one another that may otherwise be missing, it is not an easy road, and in general, when the 2 and 5 are in the same part of the numerological chart, it makes for a short lived relationship.\n"""
    elif ((life_path_1 == 2) and (life_path_2 == 9)) or ((life_path_1 == 9) and (life_path_2 == 2)):
        print """\nThis combination of numbers doesn't get along too well in terms of romantic compatibility. Despite both being loving and caring numbers, the 9's focus is on the world, and the care they naturally possess is shared with all of humanity, while the 2's emotions like to be focused on the one single person they love.\n
Generally speaking, the 2 and a 9 can form successful alliances in other circumstances, such as a business partnership, but when it comes to the needs and desires of their heart, you will need much effort to make it work.\n"""
    elif ((life_path_1 == 3) and (life_path_2 == 7)) or ((life_path_1 == 7) and (life_path_2 == 3)):
        print """\nThese two make up an interesting combination, one of two very different types of people. The 3 is restless, energetic, and constantly on the go, with a swirl of activity, travel, and social contact which the 7 usually finds intolerable. The 7 needs quiet and solitude to recharge, and can only take so much human contact before retreating to their place of peace and quiet.\n
Confrontation in this pairing never works well, and because of the different natures of the 3 and the 7, this is a relationship that can either last for a couple of weeks, or remain exciting and strong for a lifetime.\n"""
    elif ((life_path_1 == 4) and (life_path_2 == 5)) or ((life_path_1 == 5) and (life_path_2 == 4)):
        print """\nIn short, this is a challenging combination. The 4 and the 5 are each other's polar opposites. Four likes routine and predictability; 5 prefers change and unexpected. The only way this pairing can survive is if you accept each other as you are, respect your differences, and don't try to change your partner.\n"""
    elif ((life_path_1 == 4) and (life_path_2 == 9)) or ((life_path_1 == 9) and (life_path_2 == 4)):
        print """\nThe successful pairing of these two numbers is very rare, and important differences will have to be addressed and accepted by both of you if you want this relationship to last.\n
The two numbers usually don't connect, and rarely see eye to eye. If you have a successful relationship, this usually indicates that other numbers in your numerological chart play a significant enough of a role to overcome this particular incompatible combination.\n"""
    elif ((life_path_1 == 5) and (life_path_2 == 8)) or ((life_path_1 == 8) and (life_path_2 == 5)):
        print """\nRomantically, this is not a very good match. Your individual qualities and interests rarely overlap, and while the 5 is dynamic and likes freedom from rules and restraints, the 8 is a strong authoritative figure used to being the boss. It will take careful planning and compromise, and roles that are very different and far apart, for this relationship to work.\n"""
    elif ((life_path_1 == 5) and (life_path_2 == 9)) or ((life_path_1 == 9) and (life_path_2 == 5)):
        print """\nThere is very little that these two numbers have in common. Nine perceives the 5's love of freedom as irresponsible, while the idealism of the 9 appears superficial to the 5.\n
If you are in a relationship, it would suggest that other numbers in your numerological chart are responsible for the attraction between the two of you. You will need to compromise and be much more diplomatic than other number sets in order for this match to be successful.\n"""
    elif ((life_path_1 == 6) and (life_path_2 == 7)) or ((life_path_1 == 7) and (life_path_2 == 6)):
        print """\nBecause the 6 and the 7 represent very two different people, with very different ideas, each number expresses love in a different way. This can lead this number pairing to form a somewhat of a love-hate relationship.\n
Seven's secretive and 'aloof' nature, with the need for certain amount of distance, doesn't bode well with the 6's need for open expressions of love and emotions. This can cause a rift where the 6 feels insecure about the relationship, while the 7 experiences the 6's loving attention as an annoying disruption.\n
Not all is lost, however, and as long as the two of you are able to recognize these differences, there is potential here.\n"""
    elif ((life_path_1 == 7) and (life_path_2 == 8)) or ((life_path_1 == 8) and (life_path_2 == 7)):
        print """\nThese two numbers neither attract nor repel one another, and it is most common that this pairing is based more on the physical rather than the emotional. The 7's aversion against the 8's tendency to control, and the 8's preference of practical matters as opposed to the 7's philosophical and spiritual nature can lead to frequent verbal battles.\n
This is a combination where your attraction is most likely based on other numbers in you numerological chart.\n"""
    elif ((life_path_1 == 8) and (life_path_2 == 9)) or ((life_path_1 == 9) and (life_path_2 == 8)):
        print """\nThis number pairing is not considered very compatible at all. Your goals are very different and you'll frequently find yourselves on the opposite spectrum of a discussion. Although there is often a strong attraction that can form the foundation for an interesting relationship, the only way this pairing will last is if both of you recognize and respect the big differences between one another.\n"""
    else:
        print """\nBetter luck next time!\n"""


# definition of a function to display expression number compatibility based on combinations


def comp_exp_meaning(exp_1, exp_2):
    # displays compatibility based on various combinations of expression numbers of individual and partner
    # displays note that expression (destiny) numbers are reduced to single digit for relationship purposes
    print """\nFor relationship purposes, expression (destiny) numbers are reduced to single digits (e.g., master numbers 11 and 22 are reduced to 2 and 4, respectively).\n"""

    # the following are "very good" pairings
    if exp_1 == exp_2 == 1:
        print """\nThis combination comprises two people with a strong desire to lead and two people who want very much to be independent. Two 1s in a relationship understand and accept each other perhaps better than any other number can understand the 1.\n
This is a relationship not without pitfalls as the match can get dicey when they start to compete. But for the most part, it is a good one filled with excitement and activity.\n"""
    elif ((exp_1 == 1) and (exp_2 == 5)) or ((exp_1 == 5) and (exp_2 == 1)):
        print """\nThis is a very compatible combination as both of these numbers are ones that like to have a lot of freedom in a relationship. The drive for independence is paramount for each.\n
They may be so busy with their own 'thing' that time together is limited, very special, and often exciting. As you might expect, the most serious threat is when either tries to impose his or her will on the other.\n"""
    elif ((exp_1 == 1) and (exp_2 == 7)) or ((exp_1 == 7) and (exp_2 == 1)):
        print """\nThese are very different energies but ones that somehow blend nicely. The 7 provides wise insights while the 1 becomes a needed motivator. The key is to understand the tendencies; the 1 can get too busy with the outer world to always be there for the 7, and the 7 can be too into their own world to be there for the 1. Neither should take this absence personally.\n"""
    elif exp_1 == exp_2 == 2:
        print """\nA great match of two souls both needing to give and receive love. Experts at mediation, they have little difficulty finding common ground on just about any issue that arises.\n
The only word of caution for this pairing is that they must each remember how thin their own skin is so as to not cause verbal injury to the other. Generally this is not a problem because of their polite manner and mutual respect.\n"""
    elif ((exp_1 == 2) and (exp_2 == 4)) or ((exp_1 == 4) and (exp_2 == 2)):
        print """\nThis is a steady pairing resulting in comfort personified. When it comes to home and family, the 4 is the ultimate builder and provider. Security is 4's forte. Nothing is more appealing to the 2 than home, hearth, and family.\n
The only difficulty likely here is one of perception. The 2 needs love to be shown and always physically apparent, and the 4 is sometimes not so demonstrative.\n"""
    elif ((exp_1 == 2) and (exp_2 == 8)) or ((exp_1 == 8) and (exp_2 == 2)):
        print """\nA pairing that usually works very well because it is likely that each has a clear vision of their role. The 8 is about the outer world of business and attainment, taking care of the financial needs of the family. The 2 takes care of the family and is there to pamper the ego of their partner.\n
A pitfall in this relationship can occur if the 8 fails to sufficiently value the labors of the 2. Generally, this is the classic traditional family model, or in the case of the male 2, female 8, the classic male/female role reversal.\n"""
    elif exp_1 == exp_2 == 3:
        print """\nWild and interesting describes this pairing of two with so much creative and social potential. No one has more fun that a pair of 3s who understand and support one another.\n
The question may become who is going to take care of the mundane. The pitfall of this relationship comes when neither partner can hold on to reins of practical everyday details.\n"""
    elif ((exp_1 == 3) and (exp_2 == 6)) or ((exp_1 == 6) and (exp_2 == 3)):
        print """\nThis is a natural combination that works well in most cases. The 3 is full of enthusiasm and ideas, and the 6 provides the stability, support, and encouragement that often makes this combination an idea team in many ways. The chemistry here is very strong and durable.\n
The challenge of this combination can come in the form of 6's jealous feelings toward the oft flirtatious 3. Usually it will be the 6 who will have to learn to deal with an inborn trait.\n"""
    elif ((exp_1 == 3) and (exp_2 == 9)) or ((exp_1 == 9) and (exp_2 == 3)):
        print """\nThis is a wonderful combination of two people who are apt to keep each other endlessly engaged in a variety of creative ways. Both like to be on stage and both are interested in people. They care about people and the 9 can be generous to a fault.\n
The 9 is the teacher, and the 3 is the ever eager student. Sharing experience is a never ending joy of this pairing. The problem the couple faces is settling down, feathering a nest, and keeping the bills paid. Even after they are settled and set, romantic adventures will always be important.\n"""
    elif exp_1 == exp_2 == 4:
        print """\nThe keywords for this combination are solid and secure. For individuals who need to know that the bills are paid and future is totally secure, who better to fill this need than another 4.\n
These two will share goals that they work for and nearly always achieve. Success is measured by a sense that growth is continual, and this includes love and romance.\n
The down side of this pairing, if there is one, is the sense that nothing is ever completely okay. It's hard to relax , be spontaneous, and enjoy the moment and each other. Nonetheless, there are few relationships destined to be more stable than this one.\n"""
    elif ((exp_1 == 4) and (exp_2 == 8)) or ((exp_1 == 8) and (exp_2 == 4)):
        print """\nThis is a comfortable pairing because both parties understand hard work and have a good head for business and getting ahead in the world. The 4 is the cautious planner, while the 8 has a more grandiose approach to endeavors.\n
The only problem probably can be one of finding the time to spend together in a quest for romance. Yet this is a couple that knows how to build for the future and develop a very secure relationship.\n"""
    elif exp_1 == exp_2 == 5:
        print """\nA pair of 5s is a very compatible couple who prize their freedom to be different and adventuresome. Few others will be as open to the constant flow of new ideas and changes so common in the 5.\n
In this relationship, partners easily anticipate what the other is thinking and where they are going. They also have a sense for staying out of the way and accepting the freewheeling lifestyle. Fives choosing to support one another can do just about anything.\n
The difficulty with this pairing is focus, and there may be a problem handling the mundane day-to-day affairs.\n"""
    elif ((exp_1 == 5) and (exp_2 == 7)) or ((exp_1 == 7) and (exp_2 == 5)):
        print """\nThis is a relationship which is more or less free of rules and procedures. In some ways, these two are much alike and the relationship is generally very compatible.\n
The 7 values the time to be alone and enjoy the world of study and reflection in their private space. At the same time, the 5 has plenty going on and appreciates not having demands for attention being the paramount feature of the relationship.\n
Yet these two can get together and find a never ending stream of mutual interests to discuss and explore.\n"""
    elif exp_1 == exp_2 == 6:
        print """\nThis is a combination charged with romance, but in essence it is rather practical by nature. Home and family is second nature here, and these will be the top priorities for sure. This is a very compatible pairing.\n
The 6 knows what's best for their partner, so they do a good job of taking care of each other, and a family is a must. Yet the 6 by its nature wants the whole family under his/her thumb, so the challenge may be in agreeing who is going to be charge. The circumstances of the relationship will usually be able to sort this out.\n"""
    elif ((exp_1 == 6) and (exp_2 == 9)) or ((exp_1 == 9) and (exp_2 == 6)):
        print """\nThis is generally a very compatible relationship prospect as the 9 is one of the few numbers to gain 6's utmost respect. In a family situation, the 6 is unsurpassed as a manager, and the 9 is never reticent in heaping praise in recognition. This often creates a mutual admiration environment that provides a happy home for both partners.\n
The 6 helps the 9 stay focused on details and common sense issues, while the 9 broadens the 6's outlook and sense of the world at large. The expansiveness of this pairing may suggest the need to keep a close eye on the budget.\n"""
    elif exp_1 == exp_2 == 7:
        print """\nThis is one situation in which no one understands the eccentricities of a 7 nearly as well as another 7. Thus, this is a very compatible pairing. With the right attitude, this couple will find the interest to freely explore the world together, or spend their days in happy solitude together. Chances are you are on the same psychic wavelength, so you will surely catch the signals as they flash by.\n
The downside of this pairing is the tendency to not communicate, so an effort may have to be made to keep the lines open and operating.\n"""
    elif exp_1 == exp_2 == 8:
        print """\nThis pairing might be known as the 'Dynamic Duo' as this is a combination that is full of passion and romance. Indeed, this pairing is a strong and enduring match-up. Yet both partners will be easily distracted by the events in their life as goals and professional demands often supersede romantic possibilities.\n
Solid as the relationship probably is, the couple may have a hard time communicating the depth of feeling in either word or deed. Guard against competing with one another, and getting caught up in schedules and the demands of work. Make time for each other and always focus on being equal partners.\n"""
    elif exp_1 == exp_2 == 9:
        print """\nThis relationship has much promise as it usually engages two charismatic types possessing much intellectual stimulation. The nature of the 9 is selfless, so this combination usually faces few challenges; each wanting to please the other and always be there for each other. A relationship offering the opportunity to grow, learn, and serve, this is often an inspiring combination.\n"""
    # the following are "ok" pairings
    elif ((exp_1 == 1) and (exp_2 == 3)) or ((exp_1 == 3) and (exp_2 == 1)):
        print """\nThis is a very lively couple that seem to shamelessly enjoy life and each other. The 3 is good at acknowledging the 1's accomplishments and stroking the ego. The 3 provides the ideas and the 1 provides the push, so this couple can cover a lot of ground. Yet they have to be careful about what they say since neither handles criticism very well.\n"""
    elif ((exp_1 == 1) and (exp_2 == 9)) or ((exp_1 == 9) and (exp_2 == 1)):
        print """\nThe 9 brings a selflessness to the relationship which allows the 1 to operate in an environment that is understanding and smooth flowing. The 1 will have to learn to share the partner who is inclined to extend a giving nature outside the home.\n
If there is trouble in this partnership, it will generally come from the 9's difficulty tolerating the 1's assertive and individualistic behavior.\n"""
    elif ((exp_1 == 2) and (exp_2 == 3)) or ((exp_1 == 3) and (exp_2 == 2)):
        print """\nThese are potentially very good partners because of the good humor and good chemistry. The 3 is always 'on stage' and full of life and social energy, while the 2 is happy as a lark standing back and enjoying the show. The 2 balances the needs of the 3 by providing a soothing and calming influence.\n"""
    elif ((exp_1 == 2) and (exp_2 == 6)) or ((exp_1 == 6) and (exp_2 == 2)):
        print """\nThis is another good love match. The 6 ranks first in family while the 2 tops the chart in love and caring. Still the pair needs to watch their 'Ps and Qs' as the 6 has a surprising need for approbation, and 2's thin skin can suffer with the direct and demanding approach that sometimes characterizes the 6. Considerations of feelings is a must.\n"""
    elif ((exp_1 == 3) and (exp_2 == 5)) or ((exp_1 == 5) and (exp_2 == 3)):
        print """\nThis is one of the most social combinations you will find. The two will generally find each other very interesting and their ability to entertain will be never ending.\n
Social opportunities, travel, and numerous activities promise this relationship won't get boring. Both are creative by nature, yet neither excels at managing the budget, so everyday affairs can cause problems sometimes.\n"""
    elif ((exp_1 == 4) and (exp_2 == 6)) or ((exp_1 == 6) and (exp_2 == 4)):
        print """\nA comfortable match of traditional types, this pairing has promise from the very beginning. Chances are the 6 will want to take the lead in this relationship, and a secure home and family are all that is needed to produce a satisfying long-term situation.\n
The challenge of this relationship is compromise. Neither is very good at this.\n"""
    elif ((exp_1 == 4) and (exp_2 == 7)) or ((exp_1 == 7) and (exp_2 == 4)):
        print """\nThis is a relationship that has a serious tone about it and may be driven by a mutual need for security. It is loyal and devoted, even it it may lack the fire and passion of some combinations.\n
The 4 is a natural provider of rock solid security and home values. The 7 provides a quest for continued mental development and adventure. The combination makes life both secure and yet more interesting for both.\n"""
    elif ((exp_1 == 5) and (exp_2 == 9)) or ((exp_1 == 9) and (exp_2 == 5)):
        print """\nThis is a relationship between two who may find it hard to work the relationship into their busy schedules. Both of these numbers represent people who are apt to be in a constant state of transition and change. In this regard they have much in common and will generally find each other very interesting, for the moment or for the long haul.\n
The compassion of the 9 and progressive thinking of the 5 seems to blend well. Establishing a commitment to security is a must.\n"""
    elif ((exp_1 == 6) and (exp_2 == 8)) or ((exp_1 == 8) and (exp_2 == 6)):
        print """\nThis is a very positive and compatible relationship of two who are usually open and positive in most that they do. This is a couple with big ideas, and their ideas are usually brought to reality in grand fashion. The home will provide plenty of space for family, work, and frequent entertaining of their many friends.\n
A down side to the relationship can occur if the possessive 6 has to compete too much with the business interests of the 8. Likewise, the 8 will be frustrated when the demands at home cramp the executive lifestyle and obligations.\n"""
    # the following could go either way
    elif ((exp_1 == 1) and (exp_2 == 8)) or ((exp_1 == 8) and (exp_2 == 1)):
        print """\nFrom a business standpoint, this is a good match. But from the love angle, it is questionable at best. Both are so assertive and demanding, that expectations can far exceed reality.\n
Negative feedback from either will be deadly in this pairing. Success depends on a open and mutual willingness to compromise and limit demands.\n"""
    elif ((exp_1 == 2) and (exp_2 == 9)) or ((exp_1 == 9) and (exp_2 == 2)):
        print """\nThese two can have a wonderful relationship or it can be not so wonderful. The 2 needs constant attention, and certainly the 9 is a caring individual. But the care they naturally possess is spread to all humanity and often it is not focused enough at home.\n
The 9 is a natural leader and the 2 is a natural follower, so there is always hope. The 9 needs to remember that the 2 hates to be alone, and the 2 needs to be forewarned that the 9's love will only stretch so far.\n"""
    elif ((exp_1 == 5) and (exp_2 == 8)) or ((exp_1 == 8) and (exp_2 == 5)):
        print """\nThis is a relationship between two individuals who don't always follow the rules, and they might find themselves locking horns on the rules of a relationship. The 8 is used to being the boss and dominating most situations. The 5 seeks freedom from any restraints.\n
The 8 is focused on success, particularly in a financial sense, and the 5 doesn't even want to think about money. It will take careful planning and compromise to make this relationship work.\n"""
    elif ((exp_1 == 7) and (exp_2 == 9)) or ((exp_1 == 9) and (exp_2 == 7)):
        print """\nThis couple is anything but neutral in their affiliation. They are listed neutral because the relationship can go either way depending largely on spiritual beliefs. Both have strong spiritual inclinations and deeply held positions. However, these views of the spiritual and the divien often divide along rigidly held lines. In such cases, compromise is usually not an option.\n
When the spiritual positions are in harmony, this can be a very compatible combination.\n"""
    # the following are "challenging" pairings
    elif ((exp_1 == 1) and (exp_2 == 2)) or ((exp_1 == 2) and (exp_2 == 1)):
        print """\nTwo very different people who do well if they remember their roles. The 1 is best equipped to be the breadwinner, and the 2 will be the one to feather the nest and keep the warmth of romance alive and well.\n
The 1 must avoid being distracted and never forget how important attention is for the 2 partner.\n"""
    elif ((exp_1 == 1) and (exp_2 == 4)) or ((exp_1 == 4) and (exp_2 == 1)):
        print """\nFour's desire for control is a tough sell on the 1. The 1's need to make things happen now, frustrates the meticulous 4. Opposites in many ways, these two should not expect easy compromise.\n
If they ever can accept one another for who they are, their respective strengths will make a solid relationship.\n"""
    elif ((exp_1 == 1) and (exp_2 == 6)) or ((exp_1 == 6) and (exp_2 == 1)):
        print """\nThis is a power struggle waiting to happen. The 6 wants and needs to a caretaker. The 1 has an absolute need to be independent and unrestrained. This can be a successful pairing only if they can work past this roadblock, and give each other the support they both need.\n"""
    elif ((exp_1 == 2) and (exp_2 == 5)) or ((exp_1 == 5) and (exp_2 == 2)):
        print """\nThe 2 needs family and an ever present sense of being loved, and the 5 need total freedom to pursue whatever avenues appear on the horizon. This is one where the chemistry has to be very strong in order for the two very different souls to forge some significant compromises.\n
Obviously, these two can provide a lot that may otherwise be missing, but it won't be an easy road.\n"""
    elif ((exp_1 == 2) and (exp_2 == 7)) or ((exp_1 == 7) and (exp_2 == 2)):
        print """\nThis is a couple that has some strong and dissimilar needs. The 2's need for demonstrative love and 7's need for a good deal of space and solitude make this a pairing that will work only if both can stay tuned in to the other's needs and be willing to cater to them at least to some degree.\n
Generally the 2 will have to find something to occupy much of the time that would otherwise be devoted to the mate.\n"""
    elif ((exp_1 == 3) and (exp_2 == 4)) or ((exp_1 == 4) and (exp_2 == 3)):
        print """\nWhen the spontaneous 3 pairs with the micro-manager 4, something has to give, and often it won't. The 3 will take each day as it comes while the 4 has to have a definite plan far into the future. If the two can ever figure out how to meet in the middle, they will do a good job of balancing each other's shortcomings.\n
The 3 will show the 4 how to have fun while the 4 can give the 3 a needed sense of security.\n"""
    elif ((exp_1 == 3) and (exp_2 == 7)) or ((exp_1 == 7) and (exp_2 == 3)):
        print """\nThese two are about as different as people get. The 3 wants to be constantly on the go with a swirl of activity, travel, and social contact that the 7 will find intolerable. The 7 needs solitude and can only take so much human contact before retreating to their preferred peace and quiet.\n
Confrontation in this pairing never works well, and it will be up to both to understand the long-term need for compromise. The key to success here is open dialog regarding wants, needs, and goals.\n"""
    elif ((exp_1 == 3) and (exp_2 == 8)) or ((exp_1 == 8) and (exp_2 == 3)):
        print """\nThis is a combination that requires extra effort mostly because of the departure of needs. The 8 needs goals and authority to feel happy, and efforts focused here leave the 3 without needed attention and stimulation.\n
The secret to success in this combination, if there is one, is frequent getaways; periods when the 3 gets the 8 away from business and relaxed enough to have some fun. There isn't much frivolity in the 8, and this can sometimes be a tough sale.\n"""
    elif ((exp_1 == 4) and (exp_2 == 5)) or ((exp_1 == 5) and (exp_2 == 4)):
        print """\nThe 4 and the 5 have different temperaments and different ways of communicating. The 4 is very direct to the point, while the 5 will be more diplomatic and indirect. Fours don't like change, and 5s have to have it.\n
To find success, this couple will need to respect the difference and pay attention to what is said and what is inferred.\n"""
    elif ((exp_1 == 4) and (exp_2 == 9)) or ((exp_1 == 9) and (exp_2 == 4)):
        print """\nThese two are so very different that successful pairings are rare. The 9 is far more social and fosters deep humanitarian instincts. The 4 is focused on the basics of building a secure and solid immediate world.\n
To succeed in a relationship requires both to be aware of how different their approaches are, and somehow muster a willingness to accept. The 4 will certainly appreciate the 9's knowledge and intelligence, and the 9 must likewise value the 4's ruthless consistency.\n"""
    elif ((exp_1 == 5) and (exp_2 == 6)) or ((exp_1 == 6) and (exp_2 == 5)):
        print """\nThis is a combination requiring great compromise since the 5 thrives on freedom and space, and the 6 is noted for exerting control and nurturing supervision. The 6 wants complete commitment, and the 5 is looking for adventure and new horizons.\n
In a relationship, they would probably be good for each other if they could find a way to meet somewhere near the middle. They must avoid any tendency to become entrenched in positions that just won't work for the other.\n"""
    elif ((exp_1 == 6) and (exp_2 == 7)) or ((exp_1 == 7) and (exp_2 == 6)):
        print """\nThese are two very different people with very different ideas about a relationship. The 6 is openly interested in a permanent situation complete with a stable home and family. With the secretive 7, it is hard to tell what the goal might be, and only time will tell.\n
Despite the sexual attraction that may be present, this is a very challenged combination. The 6 is too controlling, and the 7 just isn't to be closely managed. The compromises required in this relationship really bend and manipulate the natural traits of both numbers.\n"""
    elif ((exp_1 == 7) and (exp_2 == 8)) or ((exp_1 == 8) and (exp_2 == 7)):
        print """\nThis is a combination that seems to work well physically, but one which is plagued with problems on the emotional level. The 8 has a tendency to dominate and control, and the 7 is a very private person prone to resist attempts to exert authority.\n
The power of both numbers can result in frequent verbal battles. Yet there is a stability factor in the pairing that makes long-term success a possibility if accommodations can be reached.\n"""
    elif ((exp_1 == 8) and (exp_2 == 9)) or ((exp_1 == 9) and (exp_2 == 8)):
        print """\nThis is a challenging combination in which two highly motivated individuals - motivated in very different ways - find it hard to accept the ways of the other. In general the goals of the 9 are lofty and may have a humanitarian bend, while the 8 seeks the reward that comes with development of leadership and material success.\n
To have much of a chance, the 8 will have to appreciate the lessons that can be learned from their generous partner. When they are able to work as a team, this is a powerful and often inspirational pair. Too often, however, the combination fails to click.\n"""
    else:
        print """\nBetter luck next time!\n"""
