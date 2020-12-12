import time

from data import import_packages, import_distances
from hashtable import HashTable
from truck import Truck
from package import Package


distance_table = import_distances()
package_list = import_packages()
packages = HashTable(41)

dist_map = {'HUB': 0,'1060 Dalton Ave S': 1, '1330 2100 S': 2, '1330 2100 S': 3, '177 W Price Ave': 4, '195 W Oakland Ave': 5, '2010 W 500 S': 6,
                        '2300 Parkway Blvd': 7, '233 Canyon Rd': 8, '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                        '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15, '3575 W Valley Central Station bus Loop': 16, '3595 Main St': 17, 
                        '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20, '4580 S 2300 E': 21, '5025 State St': 22, '5100 South 2700 West': 23, 
                        '5383 South 900 East +ACM-104': 24, '600 E 900 South': 25, '6351 South 900 East': 26}

#print(distance_table[dist_map['4300 S 1300 E']][dist_map['6351 South 900 East']]) <-- Returns distance between two addresses

for item in package_list:
    package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    packages.insert(package['packageId'], package)

def buildRoute(truck, dist_table):
    route_list = []
    package_list = truck.packageList.copy()
    priority_packages = []

    #If len is 0 then start address is Hub
    if (len(route_list) == 0):
            #priority_package tracks the package with the closest deadline in the package_list
            for package in package_list:
                if (package[5] != 'EOD'):
                    priority_packages.append(package)

            if (len(priority_packages) > 1):


# time1 = time.strptime("7:40 AM", "%I:%M %p")
# time2 = time.strptime("6:38 AM", "%I:%M %p")
# print(time1 > time2)


    #After adding the 1st package
    for package in package_list:







 #print(package[1])

 # if len is 0, starting location is Hub, so find the package within the packageList that 
 # has the closest deadline and then add that packages address to the route_list.  Remove it from the trucks
 # packageList.

        