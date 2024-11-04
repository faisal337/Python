def area(width, length):
    #Computing the area of the room
    total_area = width * length
    return total_area

width = float(input("Enter the Width of the room in feet:  "))
length = float(input("Enter the length of the room in feet: "))

room_area = area(width, length)
print(f"The Total area of the room is {room_area} square feet")