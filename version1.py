#version 1
# by kafi ashkir
#Has a yes  / no component which asks the user if they have played the te maaori quiz
# Yes/no component added on 24/6/2021

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

if played_before == "yes":
  print("program continues")

elif played_before == "no":
  print("no")