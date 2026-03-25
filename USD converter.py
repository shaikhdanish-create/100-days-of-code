# Function to convert USD to INR
def converter(usd_val):
    
    # Multiply USD value by 83 to convert into INR
    inr_val = usd_val * 83  
    
    # Print the result in a readable format
    print(usd_val, "USD =", inr_val, "INR")


# Take input from user (convert input string to float number)
usd = float(input("Enter amount in USD: "))

# Call the function and pass user input
converter(usd)
