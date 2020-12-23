from data import import_packages, import_distances
from simulator import timeToMinutes, minutesToTime, simulateDelivery, getDeliveryEndTime, displayPackageStatus
from routebuilder import buildRoute, routeDistance
from hashtable import HashTable
from truck import Truck
from package import Package

def runDeliverySim(package_id, end_time):
    
    dist_map = {'HUB': 0,'1060 Dalton Ave S': 1, '1330 2100 S': 2, '1488 4800 S': 3, '177 W Price Ave': 4, '195 W Oakland Ave': 5, '2010 W 500 S': 6,
                        '2300 Parkway Blvd': 7, '233 Canyon Rd': 8, '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                        '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15, '3575 W Valley Central Station bus Loop': 16, '3595 Main St': 17, 
                        '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20, '4580 S 2300 E': 21, '5025 State St': 22, '5100 South 2700 West': 23, 
                        '5383 South 900 East +ACM-104': 24, '600 E 900 South': 25, '6351 South 900 East': 26}
    


    # Use the import_distances function to transfer CSV distance data into a python list.
    distance_table = import_distances()
    # Use the import_packages function to transfer CSV package data into a python list.
    package_list = import_packages()
    packages = HashTable(41)

    # Iterate through each list in the imported list of Packages.  
    # Create a new package with the associated parameters and then insert the newly created Package object into the custom hash table (packages).
    for item in package_list:
        package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        package.packageLocation = 'At the hub'
        package.deliveryTime = None          
        packages.insert(package['packageId'], package)

    # Initiate custom hash table with 41 slots
    truck1_list = [15,16,14,20,21,31,40,29,13,12,22,26,27,19,23,34]
    truck2_list = [25,6,1,4,8,7,3,28,30,33,35,36,37,38,39,18] 
    truck3_list = [10,5,9,32,11,24,17,2]

    
    # Iterate through the package numbers in the truck list and add them to the Truck objects list.  Must use 'package_number-1' since the index
    # of the package list begins at 0 for package #1.  O(N)
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

    simulateDelivery(truck1_route, truck1_list,'08:00 AM',end_time)
    simulateDelivery(truck2_route,truck2_list, '09:05 AM', end_time)

    while truck1_return_time is None:
        pass

    simulateDelivery(truck3_route,truck3_list,truck1_return_time,end_time)

    displayPackageStatus()
