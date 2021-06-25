#version 2 
#by kafi ashkir
#What did i add: Added the question and answer component into the code. It randomly selects a question and asks the user the question, if the user gets the question correct, It will print Correct Answer and move onto the next question, if wrong it will print wrong answe and ask the same question again
# Question and answer component added on 24/6/21

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

#asks user if they have played the te maaori quiz
played_before = yes_no ("Have you played the Te Reo Maori quiz?" + "\n")
# if yes, program continues
if played_before == "yes":
  print("program continues")
# if no, prints the rules and says what it is
elif played_before == "no":
  print("no")

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