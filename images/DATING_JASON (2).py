# -*- coding: cp1252 -*-
#Dating Jason

def introduction():
  print("Welcome to The Dating Game! Meet our contestant: Jason Habchi! Let's get to know a little more about our lucky contestant!")
  
#########################################################################

def bad_traits():
  print("Select one following bad trait that is definitely a turn-off for Jason:")
  print ("Type A for short, Type B for crazy, Type C for ugly")
  answer = input()
  if answer ==  "a":
    print("You made Jason too picky and he ended up SINGLE!! End program")
    quit()
  else:
    print ("Select another bad trait for Jason to avoid:")
    print ("Type A for annoying, Type B for smelly, Type C for clingy")
    answer = input()
    if answer ==  "c":
      print("You made Jason too picky and he ended up SINGLE!! End program")
      quit()
#########################################################################

def question1():
  print ("Now let's move on to our question answer segment! The first question for our lovely contestant is: What is your ideal first date? The possible answers are as follows: a long walk on the beach, Netflix & Chill, & a fancy dinner. Select the following answer which you would like Jason to pick. Type A for the beach, Type B for Netflix, or Type C for dinner.")
  answer = input() 
  if answer ==  "b":
    print("You're a thirsty creep and ended up SINGLE!! End program")
    quit()
  
#########################################################################

def question2():
  print ("The next question is: Who is your favorite artist? The possible answers are as follows: Lil Peep, Drake, & Van Gogh. Select the following answer which you would like Jason to pick. Type A for the Lil Peep, Type B for Drake, or Type C for Van Gogh.")
  answer = input() 
  if answer ==  "a":
    print("You have terrible taste and deserve to die alone so you ended up SINGLE!! End program")
    quit()
  if answer ==  "c":
    print("You're hella pretentious and ended up SINGLE!! End program")
    quit()
  
#########################################################################

def question3():
  print ("The next question is: Do you believe in the institution of marriage? The possible answers are as follows: Yes of course, no I don't need a piece of paper to show my comitment to my significant other, indifferent. Select the following answer which you would like Jason to pick. Type A for Yes, Type B for No, or Type C for Indifferent.")
  answer = input() 
  if answer ==  "c":
    print("You're too indecisive for a relationship and you ended up SINGLE!! End program")
    quit()
  
#########################################################################

def question4():
  print ("The next question is: What’s your biggest goal right now? The possible answers are as follows: Pass this class, get lit, stay alive. Select the following answer which you would like Jason to pick. Type A for passing, Type B for littty, or Type C for live.")
  answer = input() 
  if answer ==  "a":
    print("You're goals are too small and you'll end up working at McDonalds. You ended up SINGLE!! End program")
    quit()
  
#########################################################################

def question5():
  print ("The next question is: If you won the lottery, what is the first thing you’d do with the money? The possible answers are as follows: get lit, travel the world, donate to charity. Select the following answer which you would like Jason to pick. Type A for litty, Type B for traveling, or Type C for charity.")
  answer = input() 
  if answer ==  "c":
    print("You gave all your money to charity and ended up homeless and SINGLE!! End Program")
    quit()
  
#########################################################################

def question6():
  print ("Finally, the last question is: What’s on your bucket list? The possible answers are as follows: Try every drug without dying, defeat a gorilla, climb Mount Everest. Select the following answer which you would like Jason to pick. Type A for DRUGS, Type B for gorilla, or Type C for Mount Everest.")
  answer = input() 
  if answer ==  "a":
    print("-_-  End Program")
    quit()
  if answer ==  "c":
    print("You fell off the mountain and died of oxygen deprivation becuase you're stupid and SINGLE!! End Program")
    quit()
  
#########################################################################

def final():
  print ("Congrats! You scored Jason a date!! Select the following lady you want Jason to go out with. The possible answers are as follows: Taylor Swift, Selena Gomez, Emma Stone. Type A for TSwift, Type B for Selena Gomez, or Type C for Emma Stone.")
  answer = input() 
  if answer ==  "a":
    print("You went on one date but Taylor hated you and wrote a song about how gross you are and you stayed SINGLE for the rest of your life.  End Program")
    quit()
  if answer ==  "b":
    print("Selena left you for Justin Beiber and you were so humiliated that you crawled into a hole and died. End Program")
    quit()
  if answer ==  "c":
    print("Congrats! You set Jason up with his celebrity crush and won the game!!")
    quit()
  
#########################################################################

introduction()
bad_traits()
question1()
question2()
question3()
question4()
question5()
question6()
final()