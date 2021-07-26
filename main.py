#setting all trigger based things to no
TriggerKnowHowToPlay = "n"
TriggerLevelPicker = "n"
Continue = "n"
#resetting score and amount of right/wrong answers
CorrectStreak = 0
score = 0
WrongAnswers = 0



#Date of Creation:22/06/2021
#purpose: to welcome the user to this quiz and ask if they want to play
#version: 1.02
#creator: Daniel Prangnell

print("Welcome to this Te Reo quiz")
while True:
  play = input("would you like to play? Y/N:").lower()
  if play == "n" or play == "no":
    print("I am sorry to here that, but have a good day")
    print("aroha mai ki konei tena, kia pai to ra")
    break
  elif play == "y" or play == "yes":
    TriggerKnowHowToPlay = "y"
    break
  else:
    print("Please enter Yes or No")





#Date of Creation:25/06/2021
#purpose: to ask if they know how to play this quiz
#version: 1.03
#creator: Daniel Prangnell

if TriggerKnowHowToPlay == "y":
  while True:
    KnowHowToPlay = input("Do you know how to play this quiz?: ").lower()
    if KnowHowToPlay == "y" or KnowHowToPlay == "yes":
      TriggerLevelPicker = "y"
      break
    elif KnowHowToPlay == "n" or KnowHowToPlay == "no":
      print()
      print("To play this quiz you will be asked a question. Based on the difficity you pick.")
      print("There will be four answers to choose from.")
      print("To pick one of those answers you will enter either A, B, C, or D.")
      print("If you get that question correctly you will gain some score.")
      print("The more questions you answer correctly in a row the higher score you will achieve.")
      print("But if you get an answer wrong you will lose your current correct streak.")
      print()
      TriggerLevelPicker = "y"
      break
    else:
      print("Please enter yes or no")





#Date of Creation:29/06/2021
#purpose: to set the difficulty of the quiz
#version: 1.02
#creator: Daniel Prangnell


if TriggerLevelPicker == "y":
  print("Please pick a difficulty out of these 3 options.")
  print("A:Beginner")
  print("B:Intermediate,")
  print("C:Advanced")
  Continue = "n"
  while True:
    LevelOfSkill = input("Please enter your answer here: ").lower()
    if LevelOfSkill == "a":
      print("You picked beginner")
      Continue = "y"
      break
    elif LevelOfSkill == "b":
      print("You picked intermediate")
      Continue = "y"
      break
    elif LevelOfSkill == "c":
      print("You picked Advanced")
      Continue = "y"
      break
    else:
      print("Please enter A, B, or C")
      Continue = "n"





#Date of Creation:29/06/2021
#purpose: to generate a random question
#version: 1.07
#creator: Daniel Prangnell

import random

if Continue == "y":
  #testing list
  questions = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
  #to make see if their is any letters left in questions
  while len(questions) >= 1:
    #to randomly choose a letter, which will deturmen what question will be asked
    questionPicker = random.choice(questions)
    #to remove that question so it doesnt get asked again
    questions.remove(questionPicker)
    #to get what word will be asked and the correct answer and the wrong answers
    #and the levl of difficulty of those questions/words
    
    if LevelOfSkill == "a":
      if questionPicker == "a":
        TeReo_Word = "awa?"
        CorrectAnswer = "a"
        AnswerA = "A: River"
        AnswerB = "B: Water"
        AnswerC = "C: Lake"
        AnswerD = "D: Ocean"
      elif questionPicker == "b":
        TeReo_Word = "iwi?"
        CorrectAnswer = "b"
        AnswerA = "A: People"
        AnswerB = "B: Tribe"
        AnswerC = "C: Family"
        AnswerD = "D: Clan"
      elif questionPicker == "c":
        TeReo_Word = "kai?"
        CorrectAnswer = "c"
        AnswerA = "A: Drink"
        AnswerB = "B: Eat"
        AnswerC = "C: Food"
        AnswerD = "D: Water"
      elif questionPicker == "d":
        TeReo_Word = "motu?"
        CorrectAnswer = "d"
        AnswerA = "A: Mountian"
        AnswerB = "B: Cliff"
        AnswerC = "C: New Zealand"
        AnswerD = "D: Island"
      elif questionPicker == "e":
        TeReo_Word = "puku?"
        CorrectAnswer = "a"
        AnswerA = "A: Stomach"
        AnswerB = "B: Arm"
        AnswerC = "C: Chest"
        AnswerD = "D: Hips"
      elif questionPicker == "f":
        TeReo_Word = "tāne"
        CorrectAnswer = "b"
        AnswerA = "A: Female"
        AnswerB = "B: Male"
        AnswerC = "C: Boy"
        AnswerD = "D: Girl"
      elif questionPicker == "g":
        TeReo_Word = "wahine"
        CorrectAnswer = "c"
        AnswerA = "A: Son"
        AnswerB = "B: Male"
        AnswerC = "C: Female"
        AnswerD = "D: Daughter"
      elif questionPicker == "h":
        TeReo_Word = "tamāhine"
        CorrectAnswer = "d"
        AnswerA = "A: Girl"
        AnswerB = "B: Boy"
        AnswerC = "C: Son"
        AnswerD = "D: Daughter"
      elif questionPicker == "i":
        TeReo_Word = "tama"
        CorrectAnswer = "a"
        AnswerA = "A: Son"
        AnswerB = "B: Daughter"
        AnswerC = "C: Girl"
        AnswerD = "D: Boy"
      elif questionPicker == "j":
        TeReo_Word = "tamariki"
        CorrectAnswer = "b"
        AnswerA = "A: Adult"
        AnswerB = "B: Children"
        AnswerC = "C: Morning"
        AnswerD = "D: Night"
      print()
      print("What is the english word for " + TeReo_Word)
    
    
    elif LevelOfSkill == "b":
      if questionPicker == "a":
        Word = "gift?"
        CorrectAnswer = "a"
        AnswerA = "A: koha"
        AnswerB = "B: "
        AnswerC = "C: "
        AnswerD = "D: "
      elif questionPicker == "b":
        Word = "New Zealand?"
        CorrectAnswer = "b"
        AnswerA = "A: Motu"
        AnswerB = "B: Aotearoa"
        AnswerC = "C: Whenua"
        AnswerD = "D: Taone Nui"
      elif questionPicker == "c":
        Word = "hello?"
        CorrectAnswer = "c"
        AnswerA = "A: "
        AnswerB = "B: "
        AnswerC = "C: tena koutou"
        AnswerD = "D: "
      elif questionPicker == "d":
        Word = "bye?"
        CorrectAnswer = "d"
        AnswerA = "A: "
        AnswerB = "B: "
        AnswerC = "C: "
        AnswerD = "D: aue"
      elif questionPicker == "e":
        Word = "arm?"
        CorrectAnswer = "a"
        AnswerA = "A: ringa"
        AnswerB = "B: "
        AnswerC = "C: "
        AnswerD = "D: "
      elif questionPicker == "f":
        Word = "eye"
        CorrectAnswer = "b"
        AnswerA = "A: "
        AnswerB = "B: karu"
        AnswerC = "C: "
        AnswerD = "D: "
      elif questionPicker == "g": 
        Word = "shirt"
        CorrectAnswer = "c"
        AnswerA = "A: hāte-hāte"
        AnswerB = "B: tarau"
        AnswerC = "C: koti"
        AnswerD = "D: "
      elif questionPicker == "h":
        Word = "computer"
        CorrectAnswer = "d"
        AnswerA = "A: pona"
        AnswerB = "B: tātaitai"
        AnswerC = "C: waea"
        AnswerD = "D: rorohiko"
      elif questionPicker == "i":
        Word = "job"
        CorrectAnswer = "a"
        AnswerA = "A: mahi"
        AnswerB = "B: tūnga"
        AnswerC = "C: umanga"
        AnswerD = "D: tari"
      elif questionPicker == "j":
        Word = "love"
        CorrectAnswer = "b"
        AnswerA = "A: hononga"
        AnswerB = "B: aroha"
        AnswerC = "C: whakahoahoa"
        AnswerD = "D: reka"
      print()
      print("What is the Te reo word for " + Word)




  #Date of Creation:29/06/2021
  #purpose: Answering system
  #version: 1.07
  #creator: Daniel Prangnell

    #asking the question
    print(AnswerA)
    print(AnswerB)
    print(AnswerC)
    print(AnswerD)
    #them putting their answer
    print()
    ABCD = "no"
    while ABCD == "no":
      answer = input("Put your answer here: ").lower()
      #to deturmin if their answer is correct
      if answer == CorrectAnswer:
        print("you got the Correct Answer")
        ABCD = "yes"
        CorrectStreak += 1
        score = score + (CorrectStreak * 10)  
        print()
        #if
      elif answer != "a" and answer != "c" and answer != "b" and answer != "d":
        print("Please enter A, B, C, or D")
      elif answer != CorrectAnswer:
        print("you did not get the correct answer, the correct answer was " + CorrectAnswer)
        WrongAnswers += 1
        ABCD = "yes"
        CorrectStreak = 0

  if len(questions) == 0:


    #Date of Creation:6/07/2021
    #purpose: to ask if they want to see their score and saying goodbye
    #version: 1.00
    #creator: Daniel Prangnell
    score = 2010
    CorrectAnswers = 8
    WrongAnswers = 2
    while True:
      SeeScore = input("Would you like to see your score? ").lower()
      if SeeScore == "y" or SeeScore == "yes":
        print("Your score is: " + str(score) + " points")
        print("You got " + str(CorrectAnswers) + " answers correct")
        print("You got " + str(WrongAnswers) + "answers wrong")
        goodbye = "y"
        break
      elif SeeScore == "no" or SeeScore == "n":
        goodbye = "y"
        break
      else:
        print("please enter yes or no")
    if goodbye == "y":
      print("Have a good day")
      print("Kia pai to ra")