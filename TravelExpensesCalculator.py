def main(): 
    ##Input fromm the employee for the travel expenses
    stay = int(input("Enter the amount spent for Hotel Stay: "))
    food = int(input("Enter the amount spent for Food: "))
    publicTransport = int(input("Enter the amount spent for Public Transport: "))
    milesTravlled = int(input("Enter the amount spent for Car Travel: "))

    ## Calling the reimburse function for calculation
    total_Amount = reimburse(stay, food,publicTransport, milesTravlled)

    ##Printing the final amount 
    print(f"The Total amount to be reimbursed is {total_Amount}")

def reimburse(stay, food,publicTransport, milesTravlled):
    ## Setting the condition that only £50 of food can be reimbursed
    if food >= 50:
        food = 50 
    total = stay + food + publicTransport + (0.43 * milesTravlled)
    return total

main()