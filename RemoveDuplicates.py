l = int(input("Enter the length of the list: "))
b = []
for i in range(0,l):
    a = int(input())
    b.append(a)

print(list(set(b)))