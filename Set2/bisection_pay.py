def bisection_pay(balance, annual_rate):
    # Calculate the monthly interest rate
    monthly_rate = annual_rate / 12.0
    # Store the original balance for reseting purposes
    original_balance = balance
    # Get the upper and lower bounds in our guessing range
    lo = balance / 12
    hi = balance * (1 + monthly_rate)**12 / 12.0
    # The accepted deviation of our guessed value
    epsilon = 0.01
    # Initial guess is in the middle
    guess = (hi+lo)/2.0
    # Assume that paid is false
    paid = False
    while not paid:
        # For each month...
        for i in range(1,13):
            # Update the balance 
            balance -= guess
            balance += balance * monthly_rate
        # If the balance is in our specified deviation range it is probably close enough
        if not (abs(balance) >= epsilon):
            paid = True
        # If it still isn't close enough lets get rid of the unnecessary half    
        elif balance < 0:
            hi = guess
            guess = (hi+lo)/2.0
            balance = original_balance
        elif balance > 0:
            lo = guess
            guess = (hi+lo)/2.0
            balance = original_balance
    print "Lowest payment: %.2f" % guess 
    
# Tests
bisection_pay(320000, 0.2)
bisection_pay(999999, 0.18)
            