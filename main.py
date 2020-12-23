from deliverysim import runDeliverySim
from hashtable import HashTable

#Use Package class method to view the package contents
#print(packages[1].packageView())

# MUST BE ABLE TO SEE ALL PACKAGE STATUSES AT ANY GIVEN TIME!
# The user should be able to look up package #19 at 10:43 am and check the info and status. 
# Having the user provide a time and printing the info and status of all the packages will meet this requirement.

#runDeliverySim(1,'11:15 AM')

userInput = None

while True:
    print("Welcome to the WGU Package Delivery Simulator")
    print("Choose from one of the menu options below")
    print("Type 'run' to run the complete delivery simulation until all packages are delivered")
    print("Type 'time' to see package delivery status at a specific time")
    print("Type 'exit' to quit the program")

    userInput = input()
    print(userInput)

    if userInput == 'exit':
        break

    if userInput == 'run':
        runDeliverySim(None,'07:00 PM')

    if userInput == 'time':
        print("Type in a specific time to view the package statuses at that time")
        print("The time must be entered in this exact format: '05:27 PM' or '11:17 AM'")

        time = input()
        print(time)

        runDeliverySim(None, time)

