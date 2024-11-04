
def middle(a,b,c):
    sorted_list =[a,b,c]
    sorted_list.sort()
    median = sorted_list[1]
    return median

sin = middle(333,3,33)
pin = middle(33,333,3) 
rin = middle(33333,333,3333) 
din = middle(33,33,333)
lin = middle(1,501, 50) 

print(sin)
print(pin)
print(rin)
print(din)
print(lin)
