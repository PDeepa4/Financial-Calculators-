import math


print(""" 
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan. \n""")

selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if selection == 'investment':

    # P = The amount deposited
    P = float(input("Please enter amount you would like to deposit : "))

    # r = Rate of interest (%), but user shoud not input the % symbol
    r = float(input("Please enter the rate of interest (exclude '%' symbol) : ")) / 100

    # t = The number of years of investment
    t = int(input("Please enter the years of investment : "))

    interest = input("Please select either 'simple' or 'compound' interest: ").lower()

    if interest == 'simple':
        # calculating simple interest using formula given
        simple_interest = P*(1+(r*t))
        
        # rounding off simple interest value to 2 decimal places
        r_simple_interest = round(simple_interest, 2)
        print(f"The amount available (using simple interest) at the end of {t} years is : £{r_simple_interest}")
    
    elif interest == 'compound':
        # calculating compound interest using formula given
        compound_interest = P*math.pow((1+r),t) 
        
        # rounding off compound interest value to 2 decimal places
        r_compound_interest = round(compound_interest, 2)
        print(f"The amount available (using compound interest) at the end of {t} years is : £{r_compound_interest}")
    
    else:
        print("Invalid selection")


elif selection == 'bond' :

    # P  = The present value of the house
    P = float(input("Enter the present value of your house : "))
    
    # i = Monthly interest rate
    i = float(input("Please enter the rate of interest (exclude '%' symbol) : "))/100 
    i = i/12

    # n = Number of months for repayment
    n = int(input("Please enter the amount of months planned for repayment : "))
    
    # calculating monthly repayment amount using given formula
    monthly_repayment = (i*P)/(1-(1+i)**(-n))
    
    # rounding off monthly repayment amount to 2 decimal places
    r_monthly_repayment = round(monthly_repayment, 2)
    print(f"The monthly repayment amount for {n} months is : £{r_monthly_repayment}")

else:
    print('Invalid input')