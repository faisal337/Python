def conversion(mpg):
    #Converting mpg to l/100km
    convert =  282.481/ mpg
    return convert

##Requesting the input from the user
mpg = float(input("Enter the value of MPG:  "))

l_100km = round(float(conversion(mpg)),2)
##Printing the size of the field in acres
print(f"{mpg} MPG in UK will be {l_100km} in Europe")