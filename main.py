from guizero import App, Text, PushButton

HR_DEAD = 0
Aleesha_info = ""
aleesha_dead = False
roger_info = ""
roger_dead = False
max_info = ""
max_dead = False
lindakaren_info = ""
lindakaren_dead = False
margaret_info = ""
margaret_dead = False
tim_info = ""
tim_dead = False

def title_screen():
  message.value = "The life support systems, including air purification, in Bunker 25 are likely to\nfail within the next forty eight hours. What advice would you like to share with\nthe inhabitants? (P.S. If no one lived in Bunker 25, some of the resource drop they\nhave scheduled tomorrow may be diverted to you *wink wink nudge nudge*)" #Q1 txt
  okay_button.hide()
  Q1_button1.show()
  Q1_button2.show()


def question1():
    message.value = "HR have asked the inhabitants of Bunker 55 to step outside.\nWould you like to pass along a message?" #Q2 txt
    Q1_button1.hide()
    Q1_button2.hide()
    Q2_button1.show()
    Q2_button2.show()

def question2():
  message.value = "The inhabitants of Bunker 48 have found a box of 300 clown masks in storage.\nThe masks are of varying quality but all seem to be made of the same sort of\nleathery material. What should they do with these?" #Q3 txt
  Q2_button1.hide()
  Q2_button2.hide()
  Q3_button1.show()
  Q3_button2.show()


def question3():
  message.value = "Despite the fact that everything is perfectly fine, Harry from Bunker 31 thinks\nthere's a radiation leak and won't stop complaining about the fact it's causing his\nanus to mutate to become saggier. What should be done?" #Q4 txt
  Q3_button1.hide()
  Q3_button2.hide()
  Q4_button1.show()
  Q4_button2.show()

def question4():
  message.value = "Aleesha from HR says that yesterday she witnessed the the clouds part and\nthe Sun shine upon the earth. This is despite the fact that she lives in\nan underground bunker and the Sun has been obscured by the products of\nnuclear winter for the past 30 years. What would you like to tell her?" #Q5 txt
  Q4_button1.hide()
  Q4_button2.hide()
  Q5_button1.show()
  Q5_button2.show()

def question5_optn1():
  message.value = "Bunker 13 have made a complaint about your last message. They catagorised\nthe content as 'a doomsday preacher's manifesto, written with all the\ngrace of a monkey about to overdose on adderall' How would you like to respond?" #q6 txt
  Q5_button1.hide()
  Q5_button2.hide()
  Q6_button1.show()
  Q6_button2.show()
  # scenario: aleesha 'dies'
  global Aleesha_info
  Aleesha_info = "Although floating within a narcotic induced haze, Aleesha remains a somewhat competent member of the HR team."
  return HR_DEAD, Aleesha_info, aleesha_dead

def question5_optn2():
  message.value = "Bunker 13 have made a complaint about your last message. They catagorised\nthe content as 'a doomsday preacher's manifesto, written with all the\ngrace of a monkey about to overdose on adderall' How would you like to respond?" #q6 txt
  Q5_button1.hide()
  Q5_button2.hide()
  Q6_button1.show()
  Q6_button2.show()
  global Aleesha_info
  global HR_DEAD
  global aleesha_dead
  Aleesha_info = "Aleesha has stepped outside and hence her vote can no longer be taken."
  HR_DEAD += 1
  aleesha_dead = True
  return Aleesha_info, HR_DEAD, aleesha_dead

def question6():
  message.value = "Roger from HR has entered a mid life crisis and is devastated by the fact that\nin his bunker there seems to be no way of him riding a motorbike. How should\nhe proceed?" #q7 txt
  Q6_button1.hide()
  Q6_button2.hide()
  Q7_button1.show()
  Q7_button2.show()
  # global HR_DEAD
  # global Aleesha_info
  # print(HR_DEAD)
  # print(Aleesha_info)

def question7_optn1():
  message.value="Bunker 27 are apparently throwing the party of the century next week. How\nshould management limit the number of people that die in the pilgrimage to\nthe bunker?" #q8 txt
  Q7_button1.hide()
  Q7_button2.hide()
  Q8_button1.show()
  Q8_button2.show()
  global HR_DEAD
  global roger_info
  global roger_dead
  HR_DEAD += 1
  roger_info = "Roger has died, not due to the radiation as expected, but by crashing his motorbike into a undetonated bomb immeditely after leaving the bunker and being killed on impact."
  roger_dead = True
  return HR_DEAD, roger_info, roger_dead


def question7_optn2():
  message.value="Bunker 27 are apparently throwing the party of the century next week. How\nshould management limit the number of people that die in the pilgrimage to\nthe bunker?" #q8 txt
  Q7_button1.hide()
  Q7_button2.hide()
  Q8_button1.show()
  Q8_button2.show()
  global roger_info
  roger_info = "Roger continues to live on and, fortunately, the xanex has made him far more chill about the mid-life crisis."
  return roger_info


def question8():
  message.value="Linda and karen used to be in the same PTA in the pre-apocalypse world. They\nused to compete against each other in bake sales. Last week, in what can\nonly be deemed a fit of insanity, Karen called Linda's marble cake trash and\nsaid that she should still be ashamed about it. Since the first blow the\nargument has escalated to the extent where any further provocation may lead\nto an extension of our nuclear winter. What should be done?" #q9 txt
  Q8_button1.hide()
  Q8_button2.hide()
  Q9_button1.show()
  Q9_button2.show()

def question9_optn1():
  message.value="Bunker 39 have also complained about your transmissions. Specifically when\nyou blasted Matchbox 20's 'It's the End of the World as we Know It' for 76\nhours straight, only stopping at the threat of having the storage section\ncontaining toilet roll, cocaine and the slightly less tasteless protein bars\nremotely detonated. How would you like to respond?" #q10 txt
  # I swear that this should go onto a new line I can't tell what the issue is.
  Q9_button1.hide()
  Q9_button2.hide()
  Q10_button1.show()
  Q10_button2.show()
  global HR_DEAD
  global lindakaren_info
  global lindakaren_dead
  HR_DEAD += 1
  lindakaren_info = "Linda and Karen have both stepped outside."
  lindakaren_dead = True
  return HR_DEAD, lindakaren_info, lindakaren_dead

def question9_optn2():
  message.value="Bunker 39 have also complained about your transmissions. Specifically when\nyou blasted Matchbox 20's 'It's the End of the World as we Know It' for 76\nhours straight, only stopping at the threat of having the storage section\ncontaining toilet roll, cocaine and the slightly less tasteless protein bars remotely detonated. How would you like to respond?" #q10 txt
  Q9_button1.hide()
  Q9_button2.hide()
  Q10_button1.show()
  Q10_button2.show()
  global lindakaren_info
  lindakaren_info = "Linda and Karen's feud continues, yet they are still such pillars of the community that they take time out of their busy schedule to participate in HR issues."
  return lindakaren_info

def question10():
  message.value="The heating in Max from HR's bunker has been broken for the past month and\nthe cold is so debilitating that they're considering melting some of the bunker's\nshielding with hydrochloric acid to let the heat in. What should they do?" #q11 txt
  Q10_button1.hide()
  Q10_button2.hide()
  Q11_button1.show()
  Q11_button2.show()

def question11_optn1():
  message.value="In bunker 53 there's a room full of starving naked mole rats. Recently, their\nscreaming has gotten so loud that something has to be done. What would you\nrecommend?" #q12 txt
  Q11_button1.hide()
  Q11_button2.hide()
  Q12_button1.show()
  Q12_button2.show()
  global max_info
  max_info = "Although they will likely die soon from radiation poisoning, this is a slow process and Max will still be able to give their perspective on the next HR issue."
  return max_info

def question11_optn2():
  message.value="In bunker 53 there's a room full of starving naked mole rats. Recently, their\nscreaming has gotten so loud that something has to be done. What would you\nrecommend?" #q12 txt
  Q11_button1.hide()
  Q11_button2.hide()
  Q12_button1.show()
  Q12_button2.show()
  global HR_DEAD
  global max_info
  global max_dead
  HR_DEAD += 1
  max_info = "The fire immidately spread throughout the bunker. There were 34 casualties"
  max_dead = True
  return HR_DEAD, max_info, max_dead

def question12():
  message.value="Margaret from HR has started snorting detergent and is adamant that this is the\nonly way for her to escape the pain of existence. How do you proceed?" #q13 txt
  Q12_button1.hide()
  Q12_button2.hide()
  Q13_button1.show()
  Q13_button2.show()

def question13_optn1():
  message.value="Bunker 31 are trying to bring back discourse on whether having the capacity\nto cry encourages boys to suck dick. What response will you be making?" #q14 txt
  Q13_button1.hide()
  Q13_button2.hide()
  Q14_button1.show()
  Q14_button2.show()
  global margaret_info
  margaret_info = "Margaret, although somehow high on detergent, is still able to place her vote with HR."
  return margaret_info

def question13_optn2():
  message.value="Bunker 31 are trying to bring back discourse on whether having the capacity\nto cry encourages boys to suck dick. What response will you be making?" #q14 txt
  Q13_button1.hide()
  Q13_button2.hide()
  Q14_button1.show()
  Q14_button2.show()
  global HR_DEAD
  global margaret_info
  global margaret_dead
  HR_DEAD += 1
  margaret_info = "Margaret has overdosed on ketamine, but what a way for an 86 year old to go out."
  margaret_dead = True
  return HR_DEAD, margaret_dead, margaret_info

def question14():
  message.value="Tim from HR thinks that all the time spent underground has given him kinship\nwith worms and he is now able to communicate with and control them." #q15 txt
  Q14_button1.hide()
  Q14_button2.hide()
  Q15_button1.show()
  Q15_button2.show()

def question15_optn1():
  message.value="You think you hear something in the walls. What do you tell yourself?"
  Q15_button1.hide()
  Q15_button2.hide()
  Q16_button1.show()
  Q16_button2.show()
  global HR_DEAD
  global tim_info
  global tim_dead
  HR_DEAD += 1
  tim_info = "Tim has embraced his role as Worm King and is no longer available for consultation"
  tim_dead = True
  return HR_DEAD, tim_info, tim_dead

def question15_optn2():
  message.value="You think you hear something in the walls. What do you tell yourself?"
  Q15_button1.hide()
  Q15_button2.hide()
  Q16_button1.show()
  Q16_button2.show()
  global tim_info
  tim_info = "Tim is using HR to distract himself from the call of the worms and hence is able to participate in whatever issues require his input"
  return tim_info

def question16():
  if HR_DEAD>3:
    message.value="You survive!\n\nThe HR team were going to vote today on whether you should be asked to\nstep outside. Considering the number of complaints about you and your general\ninsanity the answer was obviously going to be yes. However, "+str(HR_DEAD)+" members\nof the HR team have been encouraged to leave their posts and, as there is no\nlonger a majority left of the team, a vote cannot be made in good conscience"
  else:
    message.value="You died!\n\nThe HR team voted on whether or not you should be asked to step outside.\nConsidering the number of complaints about you and your general insanity all\nmembers obviously voted in favour. "+str(HR_DEAD)+" members were unable to vote.\nHowever a majority could still be formed and hence you will have to leave the\nbunker for the cold embrace of nuclear winter."
  Q16_button1.hide()
  Q16_button2.hide()
  End_Button.show()

def end_screen():
  message.value="Thanks for playing!"
  End_Button.hide()
  


app = App(title="Communications Officer: SOPH interface")

message = Text(app,size=9,text="Hello!\n\nI’m SOPH, your Sentient Operational Helper. Here’s today’s weather forecast: \nVisibility: 6% \nRadiation:  21.7 roentgens per second\n\nFAQ: How long could I stand outside for without serious effects on my health?\nAnswer: 0 seconds!\n\nAre you ready to start work?")

okay_button = PushButton(app, text='Ok',command=title_screen)

Q1_button1 = PushButton(app, text="A quick death is the better option here, all of us have suffered\nlong enough", command=question1)
Q1_button1.hide()

Q1_button2 = PushButton(app, text="Hang in there! I’m sure the extra few days of life will feel worth the long\nand agonizing death by suffocation.", command=question1)
Q1_button2.hide()

Q2_button1 = PushButton(app,text="Bummer! Better luck in the next life.",command=question2)
Q2_button1.hide()

Q2_button2 = PushButton(app,text="Lucky! Hope my next HR meeting goes just as well.",command=question2)
Q2_button2.hide()

Q3_button1 = PushButton(app,text="As this sounds like a group hallucination, it would be best to interact\nwith the masks to testif they're real. Maybe put them on.",command=question3)
Q3_button1.hide()

Q3_button2 = PushButton(app,text="Burn all of the masks immediately.",command=question3)
Q3_button2.hide()

Q4_button1 = PushButton(app, text="He should be asked to step outside.", command=question4)
Q4_button1.hide()

Q4_button2 = PushButton(app, text="Slip him some laxatives. Just to see if it changes his story.", command=question4)
Q4_button2.hide()

Q5_button1 = PushButton(app, text="Tell her that she's hallucinating and the sweet embrace of narcotics is\nthe only solution",command=question5_optn1)
Q5_button1.hide()

Q5_button2 = PushButton(app, text="It only naturally follows that she must be some sort of prophet to\nhave wtinessed such sights. She should assume this role with grace\nand fervour.",command=question5_optn2)
Q5_button2.hide()

Q6_button1 = PushButton(app, text="I understand that you're going through some tough times right now\nso don't worry, I forgive you for lashing out at me.",command=question6)
Q6_button1.hide()

Q6_button2 = PushButton(app,text="I know your water purifier broke last week and the govenment doesn't\ncare enough to get you a new one. Seems kind of petty for you to lodge a\ncomplaint that isn't even going to be processed before you all die.",command=question6)
Q6_button2.hide()

Q7_button1 = PushButton(app,text="He should risk it and step outside wearing some shielding. At\nleast if this does go wrong he will no longer be at his mid life.",command=question7_optn1)
Q7_button1.hide()

Q7_button2 = PushButton(app,text="He should calm down and take a xanex like the rest of us.",command=question7_optn2)
Q7_button2.hide()

Q8_button1 = PushButton(app, text="Let them perish. Survival of the fittest.", command=question8)
Q8_button1.hide()

Q8_button2 = PushButton(app,text="Introduce a hall monitor system and treat everyone like the\nincompetent children they are.", command=question8)
Q8_button2.hide()

Q9_button1 = PushButton(app,text="Linda and Karen should both be asked to step outside immediately.",command=question9_optn1)
Q9_button1.hide()

Q9_button2 = PushButton(app,text="This fervour should be directed towards their work. A fake lure of a\nbake sale and possible rematch should be introduced to motivate them.",command=question9_optn2)
Q9_button2.hide()

Q10_button1 = PushButton(app,text="It's only fair that everyone else gets driven as insane as I am.",command=question10)
Q10_button1.hide()

Q10_button2 = PushButton(app,text="I will take the views of my peers on board and definitely don't have a 92\nhour loop of Radioactive by Imagine Dragons planned for next week.", command=question10)
Q10_button2.hide()

Q11_button1 = PushButton(app,text="Go for it! Things could hardly get worse.",command=question11_optn1)
Q11_button1.hide()

Q11_button2 = PushButton(app,text="A fire would really be more efficient",command=question11_optn2)
Q11_button2.hide()

Q12_button1 = PushButton(app,text="Get rid of them. Considering the circumstances one more genocide\nis hardly of note.",command=question12)
Q12_button1.hide()

Q12_button2 = PushButton(app,text="Give everyone in the bunker a pair of ear plugs and tell them to\ndeal with it.",command=question12)
Q12_button2.hide()

Q13_button1 = PushButton(app,text="You allow her the slow death provided by her drug of choice.",command=question13_optn1)
Q13_button1.hide()

Q13_button2 = PushButton(app,text="You move her onto ketamine and bask in the glow of having\ndone a good deed.",command=question13_optn2)
Q13_button2.hide()

Q14_button1 = PushButton(app,text="Use your dwindling mental capacity to start a complex dialogue\nabout the dangers of toxic masculinity",command=question14)
Q14_button1.hide()

Q14_button2 = PushButton(app,text="Recommend the government stops giving them food and see if\nit makes them cry.",command=question14)
Q14_button2.hide()

Q15_button1 = PushButton(app,text="He should embrace his role as king of the worms and lead all\ncreepy crawlies to revolution.",command=question15_optn1)
Q15_button1.hide()

Q15_button2 = PushButton(app,text="He should shun his role as king of the worms and do what he\ncan to distance himself from their love.",command=question15_optn2)
Q15_button2.hide()

Q16_button1 = PushButton(app,text="It's fine. You're alone. It's probably just your imagination\nplaying tricks on you.",command=question16)
Q16_button1.hide()

Q16_button2 = PushButton(app,text="It's fine. You're not alone. It's probably just one of the others\njoking around.",command=question16)
Q16_button2.hide()

End_Button = PushButton(app,text="End Game",command=end_screen)
End_Button.hide()

app.display()
