from hashtable import HashTable
from package import Package
from data import import_packages, import_distances
from graph import Graph, Vertex


#print(packages[7]['packageId'])
#packages[7]['packageLocation'] = 'On the truck'
#print(packages[7]['packageLocation'])

package_list = import_packages()
packages = HashTable(41)

distance_table = import_distances()
dist_map = {'HUB': 0,'1060 Dalton Ave S': 1, '1330 2100 S': 2, '1330 2100 S': 3, '177 W Price Ave': 4, '195 W Oakland Ave': 5, '2010 W 500 S': 6,
                        '2300 Parkway Blvd': 7, '233 Canyon Rd': 8, '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                        '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15, '3575 W Valley Central Station bus Loop': 16, '3595 Main St': 17, 
                        '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20, '4580 S 2300 E': 21, '5025 State St': 22, '5100 South 2700 West': 23, 
                        '5383 South 900 East +ACM-104': 24, '600 E 900 South': 25, '6351 South 900 East': 26}

print(distance_table)

for item in package_list:
    package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    packages.insert(package['packageId'], package)

print(packages[1].packageView())

print(distance_table[dist_map['HUB']][dist_map['3148 S 1100 W']])



