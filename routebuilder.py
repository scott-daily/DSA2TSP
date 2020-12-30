import time
from data import import_packages, import_distances
from hashtable import HashTable
from truck import Truck
from package import Package

# distance_table is initialized with the result of the import_distances function.  This iterates through and adds all the distances from the distance data csv file
# into a list of lists containing all the distance data.
distance_table = import_distances()
# package_list is initialized with the result of the import_packages function.  This iterates through the package csv file and adds each row as a list of package data.
package_list = import_packages()
# packages is initalized as an empty Hash Table object with an initial capacity of 41. This is done in O(1) time complexity and O(1) space complexity.
packages = HashTable(41)

# This is a python dictionary used to hold a mapping of addresses to indexes for readability.  It is initialized in O(1) time complexity.  It has O(1) space complexity.
dist_map = {'HUB': 0,'1060 Dalton Ave S': 1, '1330 2100 S': 2, '1488 4800 S': 3, '177 W Price Ave': 4, '195 W Oakland Ave': 5, '2010 W 500 S': 6,
                        '2300 Parkway Blvd': 7, '233 Canyon Rd': 8, '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                        '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15, '3575 W Valley Central Station bus Loop': 16, '3595 Main St': 17, 
                        '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20, '4580 S 2300 E': 21, '5025 State St': 22, '5100 South 2700 West': 23, 
                        '5383 South 900 East +ACM-104': 24, '600 E 900 South': 25, '6351 South 900 East': 26}

# This for loop goes over each line in the package's list and creates a new Package object with the attributes and then inserts this Package
# object into the custom Hash Table "packages".  This has a run time of O(N).  It's space complexity is O(N).
for item in package_list:
    package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    packages.insert(package['packageId'], package)

# This method is used to build the route for the Truck object that the function is called with.  
# The algorithm's steps are explained in-depth within the written rubric report in section B1.
# The Big O running time for this function is O(N^4 * log N).  The space complexity is O(N).
def buildRoute(truck):
    #Start route_list with the HUB because the truck always has to start from the HUB address
    route_list = ['HUB']
    # Make a copy in order to not modify as a side effect the truck instance's internal package list
    package_list = truck.packageList.copy()
    # priority_package tracks the package with the closest deadline in the package_list
    priority_packages = []
    no_deadline_packages = []
    priority_package_address_list = []
    no_deadline_package_address_list = []

    for package in package_list:
        if (package[5] != 'EOD'): # Check to make sure another package with the same address is not already in the list
            if (package[1] not in priority_package_address_list):
                priority_package_address_list.append(package[1])
                priority_packages.append(package)
        else: # This if statement makes sure that delivery deadline packages are not counted if the truck is already visiting a priority pack with the same address
            if (package[1] not in no_deadline_package_address_list and package[1] not in priority_package_address_list):
                no_deadline_package_address_list.append(package[1])
                no_deadline_packages.append(package)

    while (len(priority_packages) >= 1):
        if (len(priority_packages) == 1):
                route_list.append(priority_packages[0][1])
                priority_packages.clear()
        else:
            sorted_priority_packages = sorted(priority_packages, key=lambda package: time.strptime(package[5], "%I:%M %p"))

            # Set the first package in the sorted list as the highest priority since it will have the earliest delivery time after sorting 
            # and check to see if next package is a later time or not
            highest_priority = sorted_priority_packages[0]
            # Iterate through the priority_package list and if any package has a lesser time than the next, add it to the route list.
            for package in priority_packages:
                # Use strptime to convert the string formatted time of the Package object into a Python Time 
                # object so that the deadlines can be compared using comparison operators.
                if time.strptime(package[5], "%I:%M %p") > time.strptime(highest_priority[5], "%I:%M %p"):
                    if (highest_priority[1] not in route_list):
                        route_list.append(highest_priority[1])
                        highest_priority = package

                # This else block will execute when the time's for two consecutive packages are equal
                else:
                    current_least_distance = float(distance_table[dist_map[route_list[-1]]][dist_map[priority_packages[1][1]]])
                    next_address = priority_packages[0][1]
                    prior_address = route_list[-1]
                    
                    for package in priority_packages:
                        if (package[1] != next_address):
                            distance_between = float(distance_table[dist_map[prior_address]][dist_map[package[1]]])
                            if (distance_between < current_least_distance):
                                current_least_distance = distance_between
                                next_address = package[1]

                    if next_address not in route_list:
                        route_list.append(next_address)
                        for package in priority_packages:
                            if package[1] == next_address:
                                priority_packages.remove(package)

    # Check to see if no deadline packages has 1 or more packages within it.  
    # If it does, then will iterate through as done in the previous section with the priority
    # packages and compare the distance of package to others to find the nearest neighbor.  
    duplicate_addresses = []
    for i in range(len(no_deadline_packages)):
            if no_deadline_packages[i][1] in route_list:
                duplicate_addresses.append(no_deadline_packages[i])
    
    if (len(duplicate_addresses) >= 1):
        for address in duplicate_addresses:
            no_deadline_packages.remove(address)

    while (len(no_deadline_packages) >= 1):
        if (len(no_deadline_packages) == 1):
            route_list.append(no_deadline_packages[0][1])
            no_deadline_packages.clear()
        else:
            current_least_distance = float(distance_table[dist_map[route_list[-1]]][dist_map[no_deadline_packages[0][1]]])
            next_address = no_deadline_packages[0][1]
            prior_address = route_list[-1]

            for package in no_deadline_packages:
                if (package[1] != next_address):
                    distance_between = float(distance_table[dist_map[prior_address]][dist_map[package[1]]])
                    if (distance_between <= current_least_distance):
                        current_least_distance = distance_between
                        next_address = package[1]

            if next_address not in route_list:
                route_list.append(next_address)
                for package in no_deadline_packages:
                    if package[1] == next_address:
                        no_deadline_packages.remove(package)

    return route_list


        