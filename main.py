# Name: Scott Daily | Student ID: 001052707

from deliverysim import runDeliverySim
from hashtable import HashTable

userInput = None

while True:
    print("Welcome to the WGU Package Delivery Simulator")
    print("Choose from one of the menu options below")
    print("Type 'run' to run the complete delivery simulation until all packages are delivered")
    print("Type 'time' to see package delivery status at a specific time")
    print("Type 'exit' to quit the program")

    userInput = input()

    if userInput == 'exit':
        break

    if userInput == 'run':
        runDeliverySim(None,'05:00 PM')

    if userInput == 'time':
        print("Type in a specific time to view the package statuses at that time")
        print("The time must be entered in this exact format: '05:27 PM' or '11:17 AM'")

        time = input()
        print("The time entered was: ", time)

        runDeliverySim(None, time)

