import math
from data import import_distances, import_packages
from package import Package
from hashtable import HashTable

distance_table = import_distances()
package_list = import_packages()
packages = HashTable(41)
print("instantiating hash table in simulator.py")

dist_map = {'HUB': 0,'1060 Dalton Ave S': 1, '1330 2100 S': 2, '1488 4800 S': 3, '177 W Price Ave': 4, '195 W Oakland Ave': 5, '2010 W 500 S': 6,
                        '2300 Parkway Blvd': 7, '233 Canyon Rd': 8, '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                        '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15, '3575 W Valley Central Station bus Loop': 16, '3595 Main St': 17, 
                        '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20, '4580 S 2300 E': 21, '5025 State St': 22, '5100 South 2700 West': 23, 
                        '5383 South 900 East +ACM-104': 24, '600 E 900 South': 25, '6351 South 900 East': 26}

for item in package_list:
        package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        package.packageLocation = 'At the hub'
        package.deliveryTime = None          
        packages.insert(package['packageId'], package)

# Time entered as: 11:35 am  OR 2:40 pm
# 8 AM = 480 minutes after midnight.  

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

    last_visited_address = [route_list[0]]
    route_list.pop(0)

    # Check if the current time is already greater than or equal to the specified ending time at the start of the simulation.  If it is
    # then just return the ending time.
    if currentTime >= endTime:
        return endTime
    else:
        # Iterate through packages and check if the package ID exists in the truck_list that was passed to the simulate function.
        # If it is, update the packages location information to show that it is en route since when the simulation begins, 
        # the trucks leave the hub.
        for package in package_list:
            if int(package[0]) in truck_list:
                packages[int(package[0])].packageLocation = 'En route'

        for i in range(len(route_list)):
            distance_between = float(distance_table[dist_map[last_visited_address[-1]]][dist_map[route_list[i]]])
            currentTime += math.floor(((distance_between/18.0)*60))
            # Check to see if the currentTime after going to the next address is greater than or equal to the specified end time.
            # If it is greater, then this is where the route ends and the final time is the end time.
            if currentTime >= endTime:
                return endTime
            else:
                for package in package_list:
                    if route_list[i] in package:
                        if int(package[0]) in truck_list:
                            packages[int(package[0])].deliveryTime = minutesToTime(currentTime)
                            packages[int(package[0])].packageLocation = 'Delivered'
                            # Append the last address so that on the next iteration around the last visited address is updated
                            if route_list[i] not in last_visited_address:
                                last_visited_address.append(route_list[i])

# Method to display current status of all packages in the package hash table
def displayPackageStatus():
    index = 1
    while index < 41:
        print(packages[index])
        index += 1

# Method to see how far a truck gets with a start & end time.  Does not have any effect on the package
# just tracks how long it takes for it 
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

