a= int(input())
b = [13]
n = 0
for i in range(1,a):
    c = (70 * i) + 13
    print(c)
    b.append(c)
    if c%360  == 13:
        print(i, c)
        break
    
print(b) 