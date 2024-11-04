# Read the input. Don't change this line. 
# No need to handle errors, only integers will be given.
def Collatz(n):
    count = 0
    while n != 1:
        count = count+1
        if n%2 == 0:
            n = n//2
        else:
            n = (3*n)+1
    return count

n = int(input())
r = Collatz(n)
print(r)

# Do your thing here...

def middle(a,b,c):
    el = [a,b,c]