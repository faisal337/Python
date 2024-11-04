##Requestng input from the user
days = int(input("Enter the number of days: ")) 
hours = int(input("Enter the number of hours: ")) 
minutes = int(input("Enter the number of minutes: ")) 
seconds = int(input("Enter the number of seconds: ")) 

##Converting the time to sseconds

convert = (86400 * days) + (3600 * hours)  + (60 * minutes) + seconds

##Printing the tootal number of seconds
print(f"There are a total of {convert} seconds")