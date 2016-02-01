def pay_min(balance, annual_rate, monthly_pay_rate):
    # Calculate monthly interest rate
    monthly_rate = annual_rate/12.0
    # Initialise total paid ammount to 0
    total_paid = 0
    # For each month...
    for i in range(1,13):
        # Calculate minimum monthly pay rate for each month
        min_monthly_pay = monthly_pay_rate * balance
        # Reduce the unpaid balance as we have just paid some ammount
        balance -= min_monthly_pay
        # Add the monthly interest rate to the balance
        balance += monthly_rate * balance
        # Increment total paid
        total_paid += min_monthly_pay
        # Print information
        print "Month: %i" %i
        print "Minimum monthly payment: %.2f" % min_monthly_pay
        print "Remaining balance: %.2f" % balance
    # Print the data after a year of payments    
    print "Total paid: %.2f" % total_paid
    print "Remaining balance: %.2f" % balance

#Tests
pay_min(4213, 0.2, 0.04)
pay_min(4842, 0.2, 0.04)