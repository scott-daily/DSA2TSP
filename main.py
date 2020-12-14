import pprint
import time

from hashtable import HashTable
from package import Package
from data import import_packages, import_distances
from truck import Truck
from simulate import buildRoute


#print(packages[7]['packageId'])
#packages[7]['packageLocation'] = 'On the truck'
#print(packages[7]['packageLocation'])

# Use the import_packages function to transfer CSV package data into a python list.
package_list = import_packages()

# Initiate custom hash table with 41 slots
packages = HashTable(41)
#print(package_list)
truck1_list = [15,16,14,20,21,31,40,29,13,12,22,23,26,27,19,34]
truck2_list = [25,6,1,4,8,7,18,3,28,30,33,35,36,37,38,39] #truck2 cannot leave depot until 9:05 am due to delayed packages

truck1 = Truck()
for package in truck1_list:
    truck1.loadPackage(package_list[package-1])

truck2 = Truck()
for package in truck2_list:
    truck2.loadPackage(package_list[package-1])

#print(truck2)

buildRoute(truck1)
#buildRoute(truck2)


#print(truck1)

# Use the import_distances function to transfer CSV distance data into a list of list
distance_table = import_distances()

# Create a dictionary to map addresses to their indexes for readability
dist_map = {'HUB': 0,'1060 Dalton Ave S': 1, '1330 2100 S': 2, '1330 2100 S': 3, '177 W Price Ave': 4, '195 W Oakland Ave': 5, '2010 W 500 S': 6,
                        '2300 Parkway Blvd': 7, '233 Canyon Rd': 8, '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                        '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15, '3575 W Valley Central Station bus Loop': 16, '3595 Main St': 17, 
                        '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20, '4580 S 2300 E': 21, '5025 State St': 22, '5100 South 2700 West': 23, 
                        '5383 South 900 East +ACM-104': 24, '600 E 900 South': 25, '6351 South 900 East': 26}

#print(distance_table)

# Iterate through each list in the imported list of Packages.  
# Create a new package with the associated parameters and then insert that into the custom packages hash table.
for item in package_list:
    package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    packages.insert(package['packageId'], package)

#Use Package class method to view the package contents
#print(packages[1].packageView())

# Print out the distance between two addreses using the dist_map address keys rather than dealing with numbers
#print(distance_table[dist_map['4300 S 1300 E']][dist_map['6351 South 900 East']])


#Convert the keys in the dist_map into a list of addresses
address_list = list(dist_map.keys())

    
#city_graph.add_edge(address_list[i],address_list[j],distance_table[i + 1][j + 1])

#print(distance_table[25][26])

pretty_print = pprint.PrettyPrinter()

#pretty_print.pprint(city_graph)
