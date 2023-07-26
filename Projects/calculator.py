import re

print("Our Magical Calculator.")
print("Type 'quit' to exit the Calculator.\n")

previous = 0
run = True

def math_function():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Thank you.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.\'()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
    
    
while run:
    math_function()