#We want to print "My name is Bat and my age is 26"

def print_something(name = "Bat",age = 18):
    print("My name is", name, "and my age is", age)

print_something(26) #It will print My name is 26 and my name is 18

print_something(age = 26) #To do that we can pass keyword as argument i.e. age = 26 

print_something(age = 2, name = "Aorus") #here order will not matter.
