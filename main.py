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




played_before = yes_no ("Have you played the Te Reo Maori quiz?" + "\n")

if played_before == "yes":
  print("program continues")

elif played_before == "no":
  print("no")


QnA= {
"How many days are there in a year?":"365", 
"How many years are in a century?":"100", 
"How many hours are in a day":"24"
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
        if answer == QnA[ques]:
            print("Correct Answer")
            break
        else:
            print("Wrong Answer")
    question.remove(ques)