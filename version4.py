#version 4
#by kafi ashkir
#purpose: Added the type of quiz component which asks the user if they want to play the multi choice mode, timed quiz mode, or the classic mode.
# Added type of quiz component on 25/6/21

import random

def yes_no(question):
  valid=False
  while not valid:
    response = input (question) .lower()

    if response == "yes" or response  == "y":   
        response = "yes"
        return response
      
    elif response == "no" or response  == "n":
        response = "no"
        return response 

def level(question):
  valid=False
  while not valid:
    response = input (question) .lower()

    if response == "3" or response  == "three":   
        response = "3"
        return response
      
    elif response == "2" or response  == "two":
        response = "2"
        return response 

    elif response == "1" or response  == "one":
        response = "1"
        return response 


def type_of_quiz(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "multiple choice" or user_response  == "multi" or user_response  == "multi choice":   
        user_response = "multiple"
        return user_response
      
    elif user_response == "Timed quiz".lower() or user_response  == "timed".lower() or user_response  == "time".lower():   
        user_response = "timed"
        return user_response

    if user_response == "classic quiz".lower() or user_response  == "classic".lower() or user_response  == "class".lower():   
        user_response = "class"
        return user_response
    
    else:
      ("thanks for playing the Te Reo Maaori Quiz")


#asks user if they have played the te maaori quiz
played_before = yes_no ("Have you played the Te Reo Maori quiz?" + "\n")
# if yes, program continues
if played_before == "yes":
  print("program continues")
# if no, prints the rules and says what it is
elif played_before == "no":
  print("no")

played_before = level ("What difficulty do you want to play, 1 is easy, 2 is normal, 3 is hard" + "\n")
# if yes, program continues
if played_before == "3":
  print("Thats great")

# if no, prints the rules and says what it is
elif played_before == "2":
  print("no")
elif played_before == "1":
  print("no")
else:
  ("Plese pick 1, 2 or 3. 1 is easy, 2 is normal, 3 is hard")


quiztype = type_of_quiz ("There are 3 type of quizes, Multiple choice, timed, or classic . Which one would you like to play" + "\n")
# if yes, program continues
if quiztype == "multiple choice":
  print("Thats amazing!")
  print("You will be given multiple choice and you will have to pick one")
  

# if no, prints the rules and says what it is
if quiztype == "timed":
  print("Thats amazing")
  print("You will be given a amount of time to answer questions")

if quiztype == "classic":
  print("Program continues")

else:
  ("Please type multi, timed, or classic") 

# quiz questions (These are not the questions that will be in the quiz, these questions are here for testing purposes) and answers
QnA= {
"How many days are there in a year?":"365", 
"How many years are in a century?":"100", 
"How many hours are in a day":"24",
"What year is it":"2021"
}   
#The questions
question = list(QnA.keys())
#input answer here 
while True:
    if not question:
        break
    ques = random.choice(question)
    print(ques)
    while True:
        answer = input('Answer : ')
        # if correct, moves onto next question
        if answer == QnA[ques]:
            print("Correct Answer")
            break
        else:
            #if wrong, Asks the same question again
            print("Wrong Answer")
    question.remove(ques)

