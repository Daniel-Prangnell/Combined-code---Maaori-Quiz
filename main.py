#setting all trigger based things to no
TriggerKnowHowToPlay = "n"
TriggerLevelPicker = "n"
Continue = "n"
#resetting score and amount of right/wrong answers
CorrectStreak = 0
score = 0
WrongAnswers = 0
CorrectAnswers = 0

#so random can be used later on (to pick the question and to deturmen wether the bonus question will or will not show)
import random



#Date of Creation:22/06/2021
#purpose: to welcome the user to this quiz and ask if they want to play
#version: 1.02
#creator: Daniel Prangnell

#welcoming them to the quiz
print("*********************************")
print("   Welcome to this Te Reo quiz")
print("*********************************")
print()
#looping to make sure they enter yes or no
while True:
  #asking if they want to play?
  play = input("would you like to play? Y/N:").lower()
  #if they do not want to play
  if play == "n" or play == "no":
    #saying goodbye
    print("I am sorry to here that, but have a good day")
    print("Aroha mai ki konei tena, kia pai to ra")
    break
  #if they want to play
  elif play == "y" or play == "yes":
    #to allow going onto the next section
    TriggerKnowHowToPlay = "y"
    #to break to loop
    break
  #if they did not enter yes or no
  else:
    print("Please enter Yes or No")



#Date of Creation:25/06/2021
#purpose: to ask if they know how to play this quiz
#version: 1.03
#creator: Daniel Prangnell

#to allow this section to start
if TriggerKnowHowToPlay == "y":
  #looping to make sure they enter yes or no
  while True:
    #asking if they know how to play
    KnowHowToPlay = input("Do you know how to play this quiz?: ").lower()
    #if they do know how to play
    if KnowHowToPlay == "y" or KnowHowToPlay == "yes":
      #to trigger level picker
      TriggerLevelPicker = "y"
      #to break the loop
      break
    #if they dont know how to play
    elif KnowHowToPlay == "n" or KnowHowToPlay == "no":
      print()
      #rules
      print("To play this quiz you will be asked a question. Based on the difficity you pick.")
      print("There will be four answers to choose from.")
      print("To pick one of those answers you will enter either A, B, C, or D.")
      print("If you get that question correct you will gain score.")
      print("The more questions you answer correctly in a row the higher score you will achieve.")
      print("But if you get an answer wrong you will lose your current correct streak.")
      print("There is also a chance to get a bonus question, which if you get right will times current score by 100.")
      print("The chance of this question appearing will be based on how many questions you get right.")
      #to trigger level picker
      TriggerLevelPicker = "y"
      #to beak the loop
      break
    #if they did not enter yes or no
    else:
      print("Please enter yes or no")



#Date of Creation:29/06/2021
#purpose: to set the difficulty of the quiz
#version: 1.02
#creator: Daniel Prangnell

#to trigger this section
if TriggerLevelPicker == "y":
  #showing the difficultys
  print("Please pick a difficulty out of these 3 options.")
  print("A:Beginner")
  print("B:Intermediate")
  print("C:Advanced")
  #looping till they ether press A, B, or C (corresponding to Beginner, Intermediate, and Advanced)
  while True:
    difficity = input("Please enter your answer here: ").lower()
    #if they choose beginner
    if difficity == "a":
      print("You picked beginner")
      #allow moving to picking the question
      PickingTheQuestion = "y"
      #breaking the loop
      break
    elif difficity == "b":
      print("You picked intermediate")
      #allow moving to picking the question
      PickingTheQuestion = "y"
      #breaking the loop
      break
    elif difficity == "c":
      print("You picked Advanced")
      #allow moving to picking the question
      PickingTheQuestion = "y"
      #breaking the loop
      break
    else:
      print("Please enter A, B, or C")
      #not allow moving to picking the question
      PickingTheQuestion = "n"



#Date of Creation:29/06/2021
#purpose: to Pick the question question
#version: 1.09
#creator: Daniel Prangnell

#allow this section to be triggered
if PickingTheQuestion == "y":
  #list of numbers to determen what question will be chosen
  questions = [1,2,3,4,5,6,7,8,9,10]
  #to loop if there is atleast one question left
  while len(questions) >= 1:
    #to randomly choose a number, which will determen what question will be asked
    questionPicker = random.choice(questions)
    #to remove that question so it doesnt get asked again
    questions.remove(questionPicker)

    #to get what word will be asked and the correct answer and the wrong answers
    #and the level of difficulty of those questions

    #if they picked beginner
    if difficity == "a":
      #if question 1 got picked
      if questionPicker == 1:
        TeReo_Word = "awa?"
        CorrectAnswer = "a"
        AnswerA = "A: River"
        AnswerB = "B: Water"
        AnswerC = "C: Lake"
        AnswerD = "D: Ocean"
      #if question 2 got picked
      elif questionPicker == 2:
        TeReo_Word = "iwi?"
        CorrectAnswer = "b"
        AnswerA = "A: People"
        AnswerB = "B: Tribe"
        AnswerC = "C: Family"
        AnswerD = "D: Clan"
      #if question 3 got picked
      elif questionPicker == 3:
        TeReo_Word = "kai?"
        CorrectAnswer = "c"
        AnswerA = "A: Drink"
        AnswerB = "B: Eat"
        AnswerC = "C: Food"
        AnswerD = "D: Water"
      #if question 4 got picked
      elif questionPicker == 4:
        TeReo_Word = "motu?"
        CorrectAnswer = "d"
        AnswerA = "A: Mountian"
        AnswerB = "B: Cliff"
        AnswerC = "C: New Zealand"
        AnswerD = "D: Island"
      #if question 5 got picked
      elif questionPicker == 5:
        TeReo_Word = "puku?"
        CorrectAnswer = "a"
        AnswerA = "A: Stomach"
        AnswerB = "B: Arm"
        AnswerC = "C: Chest"
        AnswerD = "D: Hips"
      #if question 6 got picked
      elif questionPicker == 6:
        TeReo_Word = "tāne"
        CorrectAnswer = "b"
        AnswerA = "A: Female"
        AnswerB = "B: Male"
        AnswerC = "C: Boy"
        AnswerD = "D: Girl"
      #if question 7 got picked
      elif questionPicker == 7:
        TeReo_Word = "wahine"
        CorrectAnswer = "c"
        AnswerA = "A: Son"
        AnswerB = "B: Male"
        AnswerC = "C: Female"
        AnswerD = "D: Daughter"
      #if question 8 got picked
      elif questionPicker == 8:
        TeReo_Word = "tamāhine"
        CorrectAnswer = "d"
        AnswerA = "A: Girl"
        AnswerB = "B: Boy"
        AnswerC = "C: Son"
        AnswerD = "D: Daughter"
      #if question 9 got picked
      elif questionPicker == 9:
        TeReo_Word = "tama"
        CorrectAnswer = "a"
        AnswerA = "A: Son"
        AnswerB = "B: Daughter"
        AnswerC = "C: Girl"
        AnswerD = "D: Boy"
      #if question 10 got picked
      elif questionPicker == 10:
        TeReo_Word = "tamariki"
        CorrectAnswer = "b"
        AnswerA = "A: Adult"
        AnswerB = "B: Children"
        AnswerC = "C: Morning"
        AnswerD = "D: Night"
      print()
      #printing the question
      print("What is the English word for " + TeReo_Word)
      #bonus question word
      BonusQuestionEnglish = "book"
      #bonus question Te Reo translation
      BonusQuestionTeReo = "pukapuka"
    
    #if they picked intermediate
    elif difficity == "b":
      #if question 1 got picked
      if questionPicker == 1:
        Word = "gift?"
        CorrectAnswer = "a"
        AnswerA = "A: koha"
        AnswerB = "B: hoatu"
        AnswerC = "C: manako"
        AnswerD = "D: utu"
      #if question 2 got picked
      elif questionPicker == 2:
        Word = "New Zealand?"
        CorrectAnswer = "b"
        AnswerA = "A: Motu"
        AnswerB = "B: Aotearoa"
        AnswerC = "C: Whenua"
        AnswerD = "D: Taone Nui"
      #if question 3 got picked
      elif questionPicker == 3:
        Word = "hello?"
        CorrectAnswer = "c"
        AnswerA = "A: kia ora"
        AnswerB = "B: pai"
        AnswerC = "C: tena koutou"
        AnswerD = "D: aue"
      #if question 4 got picked
      elif questionPicker == 4:
        Word = "goodbye?"
        CorrectAnswer = "b"
        AnswerA = "A: pai"
        AnswerB = "B: kia ora"
        AnswerC = "C: tena koutou"
        AnswerD = "D: aue"
      #if question 5 got picked
      elif questionPicker == 5:
        Word = "arm?"
        CorrectAnswer = "a"
        AnswerA = "A: ringa"
        AnswerB = "B: matimati"
        AnswerC = "C: parirau"
        AnswerD = "D: pakihiwi"
      #if question 6 got picked
      elif questionPicker == 6:
        Word = "eye"
        CorrectAnswer = "b"
        AnswerA = "A: tirohanga"
        AnswerB = "B: karu"
        AnswerC = "C: tirohia"
        AnswerD = "D: moana"
      #if question 7 got picked
      elif questionPicker == 7: 
        Word = "shirt"
        CorrectAnswer = "c"
        AnswerA = "A: hāte-hāte"
        AnswerB = "B: tarau"
        AnswerC = "C: koti"
        AnswerD = "D: potae"
      #if question 8 got picked
      elif questionPicker == 8:
        Word = "computer"
        CorrectAnswer = "d"
        AnswerA = "A: pona"
        AnswerB = "B: tātaitai"
        AnswerC = "C: waea"
        AnswerD = "D: rorohiko"
      #if question 9 got picked
      elif questionPicker == 9:
        Word = "job"
        CorrectAnswer = "a"
        AnswerA = "A: mahi"
        AnswerB = "B: tūnga"
        AnswerC = "C: umanga"
        AnswerD = "D: tari"
      #if question 10 got picked
      elif questionPicker == 10:
        Word = "love"
        CorrectAnswer = "b"
        AnswerA = "A: hononga"
        AnswerB = "B: aroha"
        AnswerC = "C: whakahoahoa"
        AnswerD = "D: reka"
      print()
      #printing the question
      print("What is the Te reo word for " + Word)
      #bonus question word
      BonusQuestionEnglish = "monitor"
      #bonus question Te Reo translation
      BonusQuestionTeReo = "aroturuki"


    #if they picked advanced
    elif difficity == "c":
      #if question 1 got picked
      if questionPicker == 1:
        Word = "Hamilton?"
        CorrectAnswer = "a"
        translation = "Te Reo"
        AnswerA = "A: Kirikiriroa"
        AnswerB = "B: Kiriroa"
        AnswerC = "C: kirikiri"
        AnswerD = "D: There is none"
      #if question 2 got picked
      elif questionPicker == 2:
        Word = "Channel?"
        CorrectAnswer = "b"
        translation = "Te Reo"
        AnswerA = "A: honga"
        AnswerB = "B: awakeri"
        AnswerC = "C: awa"
        AnswerD = "D: moenga"
      #if question 3 got picked
      elif questionPicker == 3:
        Word = "im good?"
        CorrectAnswer = "c"
        translation = "Te Reo"
        AnswerA = "A: tena koutou pai"
        AnswerB = "B: takatāpui"
        AnswerC = "C: he pai ahau"
        AnswerD = "D: he kino ahau"
      #if question 4 got picked
      elif questionPicker == 4:
        Word = "im sick?"
        translation = "Te Reo"
        CorrectAnswer = "d"
        AnswerA = "A: pehea koe"
        AnswerB = "B: he paru ahau"
        AnswerC = "C: he ngoikore au"
        AnswerD = "D: kei te mate ahau"
      #if question 5 got picked
      elif questionPicker == 5:
        Word = "Rubbish?"
        CorrectAnswer = "a"
        translation = "Te Reo"
        AnswerA = "A: paru"
        AnswerB = "B: kino"
        AnswerC = "C: whakamataku"
        AnswerD = "D: kirihou"
      #if question 6 got picked
      elif questionPicker == 6:
        Word = "Roto"
        CorrectAnswer = "b"
        translation = "English"
        AnswerA = "A: outside"
        AnswerB = "B: inside"
        AnswerC = "C: house"
        AnswerD = "D: furniture"
      #if question 7 got picked
      elif questionPicker == 7: 
        Word = "taonga taonga"
        CorrectAnswer = "c"
        translation = "English"
        AnswerA = "A: couch"
        AnswerB = "B: seat"
        AnswerC = "C: furniture"
        AnswerD = "D: chair"
      #if question 8 got picked
      elif questionPicker == 8:
        Word = "ka te pi"
        CorrectAnswer = "d"
        translation = "English"
        AnswerA = "A: i will be fine"
        AnswerB = "B: it will be fine"
        AnswerC = "C: i am fine"
        AnswerD = "D: then the bees"
      #if question 9 got picked
      elif questionPicker == 9:
        Word = "nga whetu ki te raki"
        CorrectAnswer = "a"
        translation = "English"
        AnswerA = "A: the northern stars"
        AnswerB = "B: the eastern stars"
        AnswerC = "C: the southern stars"
        AnswerD = "D: the western stars"
      #if question 10 got picked
      elif questionPicker == 10:
        Word = "nga waahanga rorohiko"
        CorrectAnswer = "b"
        translation = "English"
        AnswerA = "A: motherboard"
        AnswerB = "B: computer components"
        AnswerC = "C: graphics card"
        AnswerD = "D: monitor"
      print()
      #bonus question word
      BonusQuestionEnglish = "Keyboard and mouse"
      #bonus question Te Reo translation
      BonusQuestionTeReo = "papapātuhi me te kiore"
      #question
      print("What is the " + translation + ' translation for "' + Word + '"')



  #Date of Creation:29/06/2021
  #purpose: Answering system
  #version: 1.03
  #creator: Daniel Prangnell

    #show the options
    print(AnswerA)
    print(AnswerB)
    print(AnswerC)
    print(AnswerD)
    print()
    #so the answering system loop works in the bigger loop
    answered = "no"
    #looping answering system
    while answered == "no":
      #they put there answer here
      answer = input("Put your answer here: ").lower()
      #if there answer is correct
      if answer == CorrectAnswer:
        print("you got the Correct Answer")
        #to break the answering system loop
        answered = "yes"
        #add on to there correct answer streak
        CorrectStreak += 1
        #add one to there corrct answers
        CorrectAnswers += 1
        #adding to their score
        score = score + (CorrectStreak * 100)
        #showing thier current score
        print("Your current score is " + str(score))
        print()
      #if they didn't put ether A, B, C, or D
      elif answer != "a" and answer != "c" and answer != "b" and answer != "d":
        print("Please enter A, B, C, or D")
      #if there answer was incorrect
      elif answer != CorrectAnswer:
        print("you did not get the correct answer, the correct answer was " + CorrectAnswer)
        #adding one to there wrong answers
        WrongAnswers += 1
        #to break the answering system loop
        answered = "yes"
        #reseting their Correct streak
        CorrectStreak = 0
  #if there are nop questions left
  if len(questions) < 1:
    #trigger AskScore
    AskScore = "y"



  #Date of Creation:3/07/2021
  #purpose: to add a chance for a bonus question
  #version: 1.01
  #creator: Daniel Prangnell

  #the chance for the bonus question to be triggered
  BonusQuestionChance = random.randint(1,(11 - CorrectAnswers))
  #if 1 gets picked randomly bonus question is triggered
  if BonusQuestionChance == 1:
    #triggering bonus question
    TriggerBonusQuestion = "yes"
  #any other number that is randomly picked
  else:
    #making sure that bonus question is not triggered
    TriggerBonusQuestion = "no"

  #if the bonus question should be triggered
  if TriggerBonusQuestion == "yes":
    print("***********************")
    print("*** BONUS QUESTION! ***")
    print("***********************")
    #the question
    print("how do you spell " + BonusQuestionEnglish + " in Te reo?")
    #where they put their answer
    BonusQuestionInput = input("Please put your anwser here: ").lower()
    #if they got the bonus question correct
    if BonusQuestionTeReo == BonusQuestionInput:
      #congratulating them for getting the bonus question correct
      print("You Got The Bonus Question Correct")
      #multipling the score by 100 for getting the question correct 
      score *= 100
    #if they put anything other than the correct answer
    else:
      #telling them they got the question wrong and what the correct answer was
      print("sorry you didn't get the bonus question correct, better luck next time.")
      print("The correct answer was " + BonusQuestionEnglish)

print()



#Date of Creation:6/07/2021
#purpose: to ask if they want to see their score and saying goodbye
#version: 1.01
#creator: Daniel Prangnell

#allow this to be triggered or not
if AskScore == "y":
  #looping this section
  while True:
    #Asking if they want to see their score
    SeeScore = input("Would you like to see your score? ").lower()
    #if they want to see their score
    if SeeScore == "y" or SeeScore == "yes":
      #showing thir score
      print("Your score is: " + str(score) + " points")
      #showing how many questions they got right
      print("You got " + str(CorrectAnswers) + " answers correct")
      #showing how many questions they got wrong
      print("You got " + str(WrongAnswers) + " answers wrong")
      goodbye = "y"
      break
    #if they don't want to see their score
    elif SeeScore == "no" or SeeScore == "n":
      #allow the program to say goodbye
      goodbye = "y"
      #breaking this loop
      break
    #if they did not enter yes or no
    else:
      print("please enter yes or no")
  
  #saying goodbye
  if goodbye == "y":
    print("Have a good day")
    print("Kia pai to ra")
