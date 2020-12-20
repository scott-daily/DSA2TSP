import math
from data import import_packages, import_distances
from hashtable import HashTable
from truck import Truck
from package import Package
from routebuilder import buildRoute, routeDistance

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
    package.deliveryTime = None          # <--- FIGURE OUT HOW TO ADD INITIAL PACKAGE LOCATION & DELIVERY TIME DURING PACK CREATION SO 
    packages.insert(package['packageId'], package)  # INDEX ACESSING WORKS LATER ON!!
    #print(package['packageLocation'])
    #packages[1]['packageId'] = 373
    #print(packages[1]['deliveryTime'])

#print(packages[15].packageView())

#packages[2].deliveryTime = '8:45 AM'
#print(packages[2]['deliveryTime'])
#print(packages[3])

# Initiate custom hash table with 41 slots
#print(package_list)
truck1_list = [15,16,14,20,21,31,40,29,13,12,22,26,27,19,23,34]
truck2_list = [25,6,1,4,8,7,3,28,30,33,35,36,37,38,39,18] #truck2 cannot leave depot until 9:05 am due to delayed packages
truck3_list = [10,5,9,32,11,24,17,2]

truck1 = Truck()
# Iterate through the package numbers in the truck list and add them to the Truck objects list.  Must use 'package_number-1' since the index
# of the package list begins at 0 for package #1.  O(N)
for package_number in truck1_list:
    packages[package_number].packageLocation = 'At the hub'
    truck1.loadPackage(package_list[package_number-1])

#print(packages[15].packageView())

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
#truck2_route = buildRoute(truck2)
#truck3_route = buildRoute(truck3)

routeDistance(truck1_route)

# MUST BE ABLE TO SEE ALL PACKAGE STATUSES AT ANY GIVEN TIME!  locationStatus = 'At the hub, 'En route', 'Delivered'
# SET all packages packageLocation to 'En route' when truck leaves hub at specified time.  
# When package is dropped off, set packageLocation to Delivered and deliveryTime to the time upon delivery

# USE SOMETHING LIKE: for package_number in truck1_list:
#                       packages[package_number].packageLocation = 'En route'

# Trucks go 18 MPH
# Trucks cannot leave before 8:00 AM
# Only time spent driving matters.  Only have to calculate where truck would be in it's route 

# Within simulate, could use buildRoute method with each truck loaded within simulate as well.  
# Would build a route for truck1, and truck2.  Since truck1 leaves first, it will return for the remaining packages to load and then deliver them.
# Allowed to load truck3 and have driver of truck1 switch at HUB to pre-loaded truck3 for final delivery route.

# The user should be able to look up package #19 at 10:43 am and check the info and status. 
# Having the user provide a time and printing the info and status of all the packages will meet this requirement.

# Time entered as: 11:35 am  OR 2:40 pm
# 8 AM = 480 minutes after midnight.  

# TODO: Create time converting functions

def timeToMinutes(time):
    hours = int(time.split(':')[0])
    minutes = int(time.split(':')[1].split()[0])
    meridiem = time.split(':')[1].split()[1]

    if meridiem == 'PM':
        hours += 12

    return (hours*60) + minutes

def minutesToTime(minutes):
    if minutes > 60:
        hours = math.floor(minutes / 60)
        minutes = minutes % 60
        merediem = " AM"

        if hours < 10:
            if minutes < 10:
                return "0" + str(hours) + ":0" + str(minutes) + merediem
            else:
                return "0" + str(hours) + ":" + str(minutes) + merediem
        elif hours >= 10 and hours < 12:
            if minutes < 10:
                return str(hours) + ":0" + str(minutes) + merediem
            else:
                return str(hours) + ":" + str(minutes) + merediem
        elif hours >= 12:
            merediem = " PM"
            if hours == 12:
                if minutes < 10:
                    return str(hours) + ":0" + str(minutes) + merediem
                else:
                    return str(hours) + ":" + str(minutes) + merediem
            elif hours > 12:
                hours -= 12
                if hours < 10:
                    if minutes < 10:
                        return "0" + str(hours) + ":0" + str(minutes) + merediem
                    else:
                        return "0" + str(hours) + ":" + str(minutes) + merediem
                else:
                    if minutes < 10:
                        return str(hours) + ":0" + str(minutes) + merediem
                    else:
                        return str(hours) + ":" + str(minutes) + merediem
    else:
        if minutes < 10:
            return "00:0" + str(minutes) + " AM"
        else:
            return "00:" + str(minutes) + " AM"

print(minutesToTime(620))
print(minutesToTime(timeToMinutes('11:15 AM')))

# To run complete simulation, run simulate three times with each trucks route list and start & end times. (Use 5 or 6 PM for end times on full simulation)
# For function so that someone can enter a time and see all package data, use the time they want to see data for as the end time.  
# This way, the simulate function will only "deliver" packages until the end_time and then we will report all package statuses at this time to 
# show all the package statuses or a specific packages status.

def simulateDelivery(route_list,truck_list,start_time,end_time):
    # Iterate through each address in the route list and then 
    # check if any of the packages are in the package list.
    # if they are print the packages ID

    # Check if this parameter is T or F to add time for truck returning to Hub at the end of route.
    # If distance between two points is 1.7, then take 2.7 / 18.0 = .15.  Multiply .15 * 60 to 
    # see .15 is 9 minutes.  Add 9 minutes to the start_time.  Check if the start_time is currently
    # less than the end_time after calculating distance to the next address. If it is 
    # then the program must terminate so that the status of the packages at the specified
    # time can be displayed.

    currentTime = timeToMinutes(start_time)
    endTime = timeToMinutes(end_time)

    print(route_list)

    # Iterate through packages and check if the package ID exists in the truck_list that was passed to the simulate function.
    # If it is, update the packages location information to show that it is en route since when the simulation begins, 
    # the trucks leave the hub.
    for package in package_list:
        if int(package[0]) in truck_list:
            packages[int(package[0])].packageLocation = 'En route'

    for i in range(len(route_list)):
        if (i != len(route_list)-1):
            distance_between = float(distance_table[dist_map[route_list[i]]][dist_map[route_list[i+1]]])
            print("Distance between ", route_list[i]," and ", route_list[i+1]," is ", distance_between)
            currentTime += math.floor(((distance_between/18.0)*60))
            for package in package_list:
                    if route_list[i] in package:
                        if int(package[0]) in truck_list:
                            packages[int(package[0])].deliveryTime = minutesToTime(currentTime)
                            packages[int(package[0])].packageLocation = 'Delivered'
                            #print("deliveryTime: ",packages[int(package[0])]['deliveryTime'])
                            #print("packageLocation: ",packages[int(package[0])]['packageLocation'])

    
simulateDelivery(truck1_route, truck1_list,'08:00 AM','08:00 PM')

index = 1
while index < 41:
    print(packages[index])
    index += 1
