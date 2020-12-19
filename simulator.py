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

print(packages[15].packageView())

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
    packages[package_number].packageLocation = 'On the truck'
    truck1.loadPackage(package_list[package_number-1])

print(packages[15].packageView())

truck2 = Truck()
for package_number in truck2_list:
    packages[package_number].packageLocation = 'On the truck'
    truck2.loadPackage(package_list[package_number-1])

truck3 = Truck()

for package_number in truck3_list:
    packages[package_number].packageLocation = 'On the truck'
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

# TODO: Create converTime function or manage the times
def convertTime(time):
    hours = time.split(':')[0]
    minutes = time.split(':')[1].split()[0]
    meridiem = time.split(':')[1].split()[1]
    print(hours)
    print(minutes)
    print(meridiem)
    hours_to_minutes = int(hours)*60
    print(hours_to_minutes)


convertTime('8:30 AM')


#def simulate(route_list,start_time,end_time):

    

