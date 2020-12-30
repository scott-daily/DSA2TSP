import math

from data import import_packages, import_distances
from minutes import timeToMinutes, minutesToTime
from routebuilder import buildRoute
from hashtable import HashTable
from truck import Truck
from package import Package

dist_map = {'HUB': 0,'1060 Dalton Ave S': 1, '1330 2100 S': 2, '1488 4800 S': 3, '177 W Price Ave': 4, '195 W Oakland Ave': 5, '2010 W 500 S': 6,
                        '2300 Parkway Blvd': 7, '233 Canyon Rd': 8, '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                        '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15, '3575 W Valley Central Station bus Loop': 16, '3595 Main St': 17, 
                        '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20, '4580 S 2300 E': 21, '5025 State St': 22, '5100 South 2700 West': 23, 
                        '5383 South 900 East +ACM-104': 24, '600 E 900 South': 25, '6351 South 900 East': 26}
    
# Use the import_distances function to transfer CSV distance data into a python list.
distance_table = import_distances()
# Use the import_packages function to transfer CSV package data into a python list.
package_list = import_packages()
print(package_list)
packages = HashTable(41)

# Iterate through each list in the imported list of Packages.  
# Create a new package with the associated parameters and then insert the newly created Package object into the custom hash table (packages).
for item in package_list:
    package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    package.packageLocation = 'At the hub'
    package.deliveryTime = None          
    packages.insert(package['packageId'], package)

# This is a function that is created to be run by the main method.  This function begins by initializing three truck
# lists.  The packages are placed according to the stated requirements.  Trucks are set to leave at times so that all delayed packages, etc leave the
# hub at the correct time.  It's time complexity is a combination of a single for loop for each truck which is O(N) multiplied
# by the time complexity of the buildRoute function, which is O(N^4 * logN).  This means that it's time complexity following these function calls is
# O(N^5 * logN).  Finally, simulateDelivery is called and this has a time complexity of O(N^2).  So the overall complexity is O(N^7 * logN).
# The space complexity is O(N).
def runDeliverySim(package_id, end_time):
    # Initiate custom hash table with 41 slots
    truck1_list = [15,16,14,20,21,31,40,29,13,12,22,26,27,19,23,34]
    truck2_list = [25,6,1,4,8,7,3,28,30,33,35,36,37,38,39,18] 
    truck3_list = [10,5,9,32,11,24,17,2]

    
    # Iterate through the package numbers in the truck list and add them to the Truck objects list.  Must use 'package_number-1' since the index
    # of the package list begins at 0 for package #1.  This has a time complexity of O(N).  It has a space complexity of O(1).
    truck1 = Truck()
    for package_number in truck1_list:
            packages[package_number].packageLocation = 'At the hub'
            truck1.loadPackage(package_list[package_number-1])

    truck2 = Truck()
    for package_number in truck2_list:
            packages[package_number].packageLocation = 'At the hub'
            truck2.loadPackage(package_list[package_number-1])

    truck3 = Truck()
    for package_number in truck3_list:
            packages[package_number].packageLocation = 'At the hub'
            truck3.loadPackage(package_list[package_number-1])

    # After each Truck object has been intialized, the route is built for each trucks individual package list.
    # The return values are the minutes taken to deliver the packages, which is utilized later to display the total miles traveled by all trucks.
    truck1_route = buildRoute(truck1)
    # Append 'HUB' so that truck1 returns to the Hub so that the driver can switch to truck3
    truck1_route.append('HUB')
    truck2_route = buildRoute(truck2)
    truck3_route = buildRoute(truck3)

    # To fulfill requirement of viewing the status of any package at any time
    # Run simulateDelivery with the specified end time for all three routes.  
    # The start_time for truck3 depends on the end time for truck1's route.    
    # Use simulateDelivery with truck1's route, list, start & end time as the start_time parameter for
    # truck3 in the call to simulateDelivery.

    truck1_return_time = minutesToTime(getDeliveryEndTime(truck1_route, '08:00 AM',end_time))                

    truck1_time = simulateDelivery(truck1_route, truck1_list,'08:00 AM',end_time)

    truck2_time = simulateDelivery(truck2_route,truck2_list,'09:05 AM',end_time)
    
    while truck1_return_time is None:
        pass

    truck3_time = simulateDelivery(truck3_route,truck3_list,truck1_return_time,end_time)

    total_distance = (((truck1_time + truck2_time + truck3_time) / 60.0) * 18.0)

    print("-----------------------------------------------------------")
    print("The total distance in miles traveled by all trucks was:", total_distance) 
    print("The package statuses at the specified time that was input are displayed below:")
    print("If the 'run' command was used, then it will show the final delivery time for all packages")
    print("-----------------------------------------------------------")
    displayPackageStatus()


# To run complete simulation, run simulateDelivery three times with each trucks route list and start & end times. (Use 5 PM for end times on complete simulation)
# This way, the simulate function will only "deliver" packages until the end_time and then report all package statuses at this time to 
# display all the current package statuses.  The time complexity is O(N^2) and the space complexity is O(1).
def simulateDelivery(route_list,truck_list,start_time,end_time):

    currentTime = timeToMinutes(start_time)
    endTime = timeToMinutes(end_time)

    # This variable is created to hold the first address in the route list.
    # Later we want to start on the next address within the loop, so we remove the first address as well from the route list.
    last_visited_address = [route_list[0]]
    route_list.pop(0)

    # Check if the current time is already greater than or equal to the specified ending time at the start of the simulation.  If it is
    # then just return the total time taken.
    if currentTime >= endTime:
        return (endTime - timeToMinutes(start_time))
    else:
        # Iterate through packages and check if the package ID exists in the truck_list that was passed to the simulate function.
        # If it is, update the packages location information to show that it is en route since when the simulation begins, 
        # the trucks are "leaving" the hub.
        for package in package_list:
            if int(package[0]) in truck_list:
                packages[int(package[0])].packageLocation = 'En route'

        # Here we iterate through the number of items in the route list.
        # We calculate the distance between each address and then convert the distance into a time and add it to the current time.
        # We check to see if the current time is greater than or equal to the given end time.  If it is, then time is up.
        # We return the total time taken up until the given ending time.  If it is not, then we iterate through each package in the package_list
        # and check to see if the current address is in the package.  If it is, then we check if that package is in the trucks package list.
        # If it is in the package list, then we update the packages delivery time and location to the current time.
        # Finally, we cehck to make sure that last visited address does not have teh same address already in it.  If it does not, then
        # we add the current address being iterated over to last_visited_address so that it is correct upon the next iteration.
        for i in range(len(route_list)):
            distance_between = float(distance_table[dist_map[last_visited_address[-1]]][dist_map[route_list[i]]])
            currentTime += math.floor(((distance_between/18.0)*60))
            # Check to see if the currentTime after going to the next address is greater than or equal to the specified end time.
            # If it is greater, then this is where the route ends and the time traveled is the end time minus the start time.
            if currentTime >= endTime:
                return (endTime - timeToMinutes(start_time))
            else:
                for package in package_list:
                    if route_list[i] in package:
                        if int(package[0]) in truck_list:
                            packages[int(package[0])].deliveryTime = minutesToTime(currentTime)
                            packages[int(package[0])].packageLocation = 'Delivered'
                            # Append the last address so that on the next iteration around the last visited address is updated
                            if route_list[i] not in last_visited_address:
                                last_visited_address.append(route_list[i])
    # Returns the amount of time in minutes the truck took to complete the delivery with the given end time.
    return(currentTime - timeToMinutes(start_time))

# Method to see how far a truck gets with a given start & end time.  Does not have any effect on the packages
# just tracks how long it would take to deliver.  This is used to find out how long truck 1's route will take so that truck 3 can leave at right when truck1 returns 
# to the Hub and the driver switches to truck 3.  It has a time complexity of O(N) and a space complexity of O(1).
def getDeliveryEndTime(route_list,start_time,end_time):
    currentTime = timeToMinutes(start_time)
    endTime = timeToMinutes(end_time)

    # Check if the current time is already greater than or equal to the specified ending time at the start of the simulation.  If it is
    # then just return the ending time.
    if currentTime >= endTime:
        return endTime
    else:
        # Iterate through packages and check if the package ID exists in the truck_list that was passed to the simulate function.
        # Continue iterating until the currentTime meets or exceeds the specified end time.  Finally, return the final ending time (Simulating when the 
        # truck would have retuned to the Hub again.)
        for i in range(len(route_list)):
            if (i != len(route_list)-1):
                distance_between = float(distance_table[dist_map[route_list[i]]][dist_map[route_list[i+1]]])
                currentTime += math.floor(((distance_between/18.0)*60))
                if currentTime >= endTime:
                    return endTime
                    
    return currentTime

# Method to display current status of all packages in the package hash table.
# After printing the package statuses, it then re-writes the package hash table so that the next time a user 
# issues a command, such as time and enters a time, it will not show the package statuses from the a prior command such as run that already
# delivered all packages.  It has a time complexity of O(N) and a space complexity of O(N).
def displayPackageStatus():
    index = 1
    while index < 41:
        print(packages[index])
        index += 1

    for item in package_list:
        package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        package.packageLocation = 'At the hub'
        package.deliveryTime = None          
        packages.insert(package['packageId'], package)
