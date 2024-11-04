def area(width, length):
    #Computing the area of the field
    total_area = width * length
    total_area = round(total_area/43560,2)
    return total_area

##Requesting the input from the farmer
width = float(input("Enter the Width of the field in feet:  "))
length = float(input("Enter the length of the field in feet: "))

field_area = area(width, length)
##Printing the size of the field in acres
print(f"The Total area of the field is {field_area} acres")