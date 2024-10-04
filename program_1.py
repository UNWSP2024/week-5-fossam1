# Samuel Foss
# Program 1: Kilometer Converter
# 10/4/2024

# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers,
# then converts that distance to miles.  The conversion formula is as follows:
# Miles = kilometers x 0.6214.
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):
    miles = 0.0
    ######################
    miles = kiloamount * 0.6214
    ######################

    # Return the variable to the calling function
    return miles


#### This piece of the code has been done for you,
#### you only need to worry about the actual temp
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    kiloamount = float(input("How many Kilometers? : "))
    # Call kilometer_conversion
    miles = kilometer_conversion(kiloamount)
    # Display the miles
    print(f"{kiloamount} kilometers is equal to {miles:.2f} miles.")
    
#Output
#in main
#How many Kilometers? : 6
#6.0 kilometers is equal to 3.73 miles.

#Process finished with exit code 0
