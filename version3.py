#version 3 
#by kafi ashkir
#What makes it different to version 2: Added a level component which asks the user what difficlutly they want to play, difficulty 1 is easy, difficulty 2 is normal, difficulty 3 is hard, 
# Difficulty component added on 25/6/21

import random

# Main routine

# yes no component
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

# difficulty component
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


#asks user if they have played the te maaori quiz
played_before = yes_no ("Have you played the Te Reo Maori quiz?" + "\n")
# if yes, program continues
if played_before == "yes":
  print("program continues")
# if no, prints the rules and says what it is
elif played_before == "no":
  print("no")

played_before = level ("What difficulty do you want to play, 1 is easy, 2 is normal, 3 is hard" + "\n")
# if user chooses diifulty 3, they will be given very difficult questions
if played_before == "3":
  print("Thats great")

# if user chooses diifulty 2, they will be given normal difficulty questions
elif played_before == "2":
  print("no")

# if user chooses diifulty 1, they will be given easy questions
elif played_before == "1":
  print("no")
else:
  ("Plese pick 1, 2 or 3. 1 is easy, 2 is normal, 3 is hard")




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











