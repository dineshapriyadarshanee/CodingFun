#Name: Dinesha Priyadarshanee 

######Pseudocode########
#load file 'data.npy' and store to data array
#Prompt user to enter 'N' for name or 'L' for license number to search the record
#if input is 'N' 
#   Prompt user to enter name
#   if name in dataArray
#       get the index of name in array
#       display summary of hire with name, license number, days hired and rental
#   else display customer not found error
#else if input is 'L'
#   Prompt user to enter license number
#   if license number in dataArray
#       get index of license number in array
#       display summary of hire with name, license number, days hired and rental
#   else display customer not found error
#else display invalid input message

import numpy

#Display the summary including name, license no and hire details in a formatted way 
def displaySummaryOfHire(customerName, licenseNumber, numberOfDaysHired, rental):
    topic = 'Summary of Hire'
    
    print('\n')
    print(topic.center(50))
    print(('-'*21).center(50))
    print(('Customer: ' + customerName).center(50))
    print(('License No: ' + licenseNumber).center(50))
    print(('Number of days: ' + str(numberOfDaysHired)).center(50))
    print(('The rental is $' + str(rental)).center(50) + '\n')

data = numpy.load('data.npy')#load the numpy file saved before.

userInput = input('Type N for entering Customer Name or type L for entering License Number: ')
if userInput == 'N':
    name = input('Type the name of the customer: ')
    if name in data:
        i = numpy.where(data == name)[0][0]
        #get data after name using the index
        displaySummaryOfHire(data[i], data[i+1], data[i+2], data[i+3])
    else:
        print('Customer not found, try again')
elif userInput == 'L':
    licenseNumber = input('Type the license number: ')
    if licenseNumber in data:
        i = numpy.where(data == licenseNumber)[0][0]
        #license number is the second data and to access the name get the element before
        displaySummaryOfHire(data[i-1], data[i], data[i+1], data[i+2])
    else:
        print('Customer not found, try again')
else:
    print('Invalid input')#for inputs other than 'N' and 'L'
