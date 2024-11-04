def nsum(n):
    #Computing the sum of all the n positive integrs
    sum = ((n)*(n+1)/2)
    return sum

##Requesting the input from the user

n = int(input("Enter the number to compute the sum of positive integers: "))
if n < 0:
    print("Not a positive integer")
sum = int(nsum(n))

##Printing the sum of n postive integrs
print(f"The Total sum of {n} positive integers is {sum}")