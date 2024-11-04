def weight(widget, gizmo):
    #Computing the weight of the parts
    total_weight = (75 * widget) + (112 * gizmo) 
    return total_weight

##Requesting the input from the user
widget = int(input("Enter the number of Widgets:  "))
gizmo = int(input("Enter the number of Gizmos: "))

total_weight = weight(widget, gizmo)
##Printing the wight of the pats
print(f"The Total weight of the parts is {total_weight} grams")