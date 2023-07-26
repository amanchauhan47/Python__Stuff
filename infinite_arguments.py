#Passing infinity Arguments using For Loop

def infinity(*people):     # Asterisk means its an array in which all arguments are passed.
    for person in people:
        print("The name is", person)

infinity("Aman","Batman","Arkham","Gotham","Amanisher")
