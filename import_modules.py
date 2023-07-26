import re #regex module 

string = "This is NOT working 'he said'."
print(string)

new = re.sub('[A-Z]', '', string) #this will remove all capital letters and we can also pass particular alphabet to remove like [T,N]
print(new)

new = re.sub('[a-z]', '', string) #this will remove all lower case letters in the string.
print(new)

new = re.sub('[.,\']', '', string)
print(new)

new = re.sub('[.,\',A-Z]', '', string)
print(new)

new = re.sub('[.,\',A-Z, ]', '', string) #remove spaces
print(new)

new = re.sub('[.,\',A-Z,a-z]', '', string) #remove everything except spaces " "
print(new)

string = string + "12 + 14 = 26"

new = re.sub('[^0-9]', '', string)
print(new)