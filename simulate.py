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

def buildRoute(truck):
    route_list = []
    # Make a copy in order to not modify as a side effect the truck instance's internal package list
    package_list = truck.packageList.copy()
    # priority_package tracks the package with the closest deadline in the package_list
    priority_packages = []
    no_deadline_packages = []

    # If len is 0 then starting address is the Hub
    if (len(route_list) == 0):
            for package in package_list:
                if (package[5] != 'EOD'):
                    priority_packages.append(package)
                else:
                    no_deadline_packages.append(package)

            ### READ ME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            ## When adding packages to the priority_packages list & no_deadline_list check to see if they are duplicate
            # addresses, if same deadline & address, only need one and can remove others.


            # Check that the priority packages list has more than one item, otherwise not necessary to sort
            if (len(priority_packages) > 1):
                sorted_priority_packages = sorted(priority_packages, key=lambda package: time.strptime(package[5], "%I:%M %p"))

                # Set the first package in the list as the highest priority and check to see if next package is a later deadline
                highest_priority = sorted_priority_packages[0]
                # Use strptime to convert the string formatted time of the Package object into a Time Python object so that the deadlines can be compared with comparison operators
                for package in priority_packages:
                    #print(highest_priority[5])
                    # See large comment block below if statement below for explanation
                    if (time.strptime(package[5], "%I:%M %p") > time.strptime(highest_priority[5], "%I:%M %p")):
                        route_list.append(highest_priority[1])
                        print(route_list)
                        priority_packages.remove(highest_priority)
                        print(priority_packages)   
                        highest_priority = package 
                    else:
                        # Make sure route_list contains a starting address.  If all deadlines are equal then the route_list will be empty when this else block is executed.
                        if (len(route_list) == 0):
                            route_list.append(priority_packages[0][1])
                            priority_packages.remove(priority_packages[0])

                        least_distance = 999.0
                        next_address = None
                        print(priority_packages)
                        for i in range(len(priority_packages)):
                            print(i)
                            print(priority_packages[i][1])
                            if (route_list[-1] != priority_packages[i][1]):
                                if (float(distance_table[dist_map[route_list[-1]]][dist_map[priority_packages[i][1]]]) < least_distance):
                                    print(route_list[-1])
                                    next_address = priority_packages[i][1]
                                    print(next_address)
                                    least_distance = float(distance_table[dist_map[route_list[-1]]][dist_map[priority_packages[i][1]]])
                                    print(distance_table[dist_map[route_list[-1]]][dist_map[priority_packages[i][1]]])
                                    #print(priority_packages[i][1])
                                    #print(priority_packages([i+1][1]))
                                    #print(next_address)
                                    #print(route_list)
                                


                        
                        # Check to see if next package in the list is a later time or not.  If it is later, then 
                        # the current highest_priority packages address should be added to the route list as the first address to visit
                        # Assign the curr package to the highest_priority variable and check if next pack is a later time.  If it is
                        # then repeat and add the current highest_priority (the prior pack) to the route list.  If the next pack has the same deadline
                        # then must check the address of the last item in the route list and track the lowest_distance variable 
                        # Must use the distance table to compare distance of last pack in route list address and remaining packs in the sorted package list
                        # Add packages according to nearest neighbor algorithm

                        # Now add the final highest_priority package to the route list as the first route.
                        # Next, (MAYBE LOOP THROUGH PRIORITY_PACKAGES AND SORT AND THEN ADD SORTED ADDRESSES TO ROUTE LIST)
                
                print(highest_priority)

# time1 = time.strptime("7:40 AM", "%I:%M %p")
# time2 = time.strptime("6:38 AM", "%I:%M %p")
# print(time1 > time2)


    #After adding the 1st package
    #for package in package_list:







 #print(package[1])

 # if len is 0, starting location is Hub, so find the package within the packageList that 
 # has the closest deadline and then add that packages address to the route_list.  Remove it from the trucks
 # packageList.

        