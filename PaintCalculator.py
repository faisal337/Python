def main(): 
    ##Input for measuuring the dimesnsions of the wall
    height = int(input("Enter the Height of the wall in meters: "))
    width = int(input("Enter the Width of the wall in meters:  "))

    ## Calling the paint function for calculation
    paint_required = paint(height, width)

    ##Printing the final paint required  
    print(f"The Total amount to be reimbursed is {paint_required}")

def paint(height, width):
    ## Calculating the paint reuqired for the wall
    total_area = height * width
    paint_area = 2 * total_area
    paint_needed = int(round(paint_area/10,0))
    return paint_needed

main()