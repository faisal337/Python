##Requestng input from the user
height_feet = int(input("Enter your height in feet: ")) 
height_inches = int(input("Enter your height in inches: ")) 

##Converting from feet, inches to cm
convert = ((height_feet *12) + height_inches) * 2.54

##Printing the final output
print(f"{height_feet}'{height_inches} will be {convert} cm")