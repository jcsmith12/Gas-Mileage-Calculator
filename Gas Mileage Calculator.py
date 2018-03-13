# Check user input to see if it is a number
def inputNumber(message):
  while True:
    try:
       userInput = float(input(message))       
    except ValueError:
       print("Please enter a valid number")
       continue
    else:
       return userInput 
       break 

# Create an average of a given list of numbers
def average(list):
    avg = sum(list)    
    avg = float(avg) / len(list)
    return avg
    
# Determine single trip gas mileage and records value to 'mileages' list
def gas_mileage(mil, gal):
    mileage = float(mil) / float(gal)
    mileages.append(mileage)
    return mileage

# Main function
def get_trip_info(mileages):
    # Gather info from user (Miles, Gallons, Price per gallon, Total Cost)
    miles = inputNumber("Miles: ")
    gallons = inputNumber("Gallons: ")
    ##  ppg = input("Price per Gallon: ")
    ##  cost = input("Total Cost: ")
    
    # Calculate mileage for this trip and display to user
    trip_mileage = gas_mileage(miles, gallons)
    print ("This Trip's gas mileage: %0.2f MPG" % trip_mileage)
    
    # Calculate running gas mileage average for user's vehicle
    running_avg = average(mileages)
    print ("Average Gas Mileage: %0.2f MPG\n" % running_avg)
 
# Setup Mileages as an empty list.
mileages = []


# User Entry Loop
while True:
    ans = input("Enter trip data? (y/n)")
    
    while ans != 'y' and ans != 'n':
        ans = input("Please enter 'y' or 'n'")
    
    
    if ans == 'y':
        get_trip_info(mileages)
    elif ans == 'n':
        break
    else:
        break
        
""" Features to add
    - save and retrieve mileages from previous sessions.
    - record date and associate with each individual gas and miles record.
    - instead of taking in miles traveled on last tank, ask for total mileage and calculate miles traveled since last fill up.
    - LONG SHOT: add graphical user interface to input new data instead of through command line
    
    """