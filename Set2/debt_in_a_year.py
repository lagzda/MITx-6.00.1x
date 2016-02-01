def debt_in_a_year(balance, annual_rate):
    # Calculate monthly interest rate
    monthly_rate = annual_rate / 12
    # Store the original balance in case I need to reset it
    original_balance = balance
    # Initialise the starting guess
    guess = 10
    # The interval to increment guesses
    step = 10
    # Assume that the debt is not paid
    paid = False
    while (not paid):
        for i in range(1,13):
            # Calculate the balance after paying and updating th rate
            balance -= guess
            balance += balance * monthly_rate
        # Check if the balance is paid after a year    
        if balance <= 0:
            paid = True
        # If the balance is not paid increment guess and reset the initial balance    
        else:
            guess += step
            balance = original_balance
    # Print answer        
    print "Lowest payment: %.2f" % guess

# Tests    
debt_in_a_year(3329, 0.2)
debt_in_a_year(4773, 0.2)
debt_in_a_year(3926, 0.2)