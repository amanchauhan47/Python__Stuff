n = int(input("Enter the number: "))

## Method 1

# count = 0

# for i in range(2,int(n/2)):
#     if (n%i == 0):
#         count+=1
#         break

# if count == 0:
#     print("Prime Number")
# else:
#     print("Not a prime number.")


## Method 2
for i in range(2,int(n/2)):
    if(n%i == 0):
        print("Not a prime")
        break
else:
        print("Prime Number")
