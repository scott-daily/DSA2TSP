class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, mass_kg):
        self.packageId = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zip_code
        self.deadline = delivery_deadline
        self.mass = mass_kg
        self.packageLocation = "At the hub"
        self.deliveryTime = None
        #if packageLocation is == 'Delivered', when user checks packages at a time, then return the delivered at: + self.deliveryTime.  
        # update self.deliveryTime when package is delivered during simulation

    def packageView(self):
        return {'packageId': self.packageId, 'address': self.address, 'city': self.city, 'state': self.state, 'zipcode': self.zipCode, 'deadline': self.deadline, 'mass': self.mass,
        'packageLocation': self.packageLocation,'pickupTime': self.pickupTime}

    def get(self, attribute):
        return getattr(self, attribute)

    def __getitem__(self, attribute):
        return getattr(self, attribute)

    def __setitem__(self, attribute, newValue):
        return setattr(self, attribute, newValue)

    
'''Per requirement F and G, the user should be able to check the status (at the hub, en route, or delivered at time X)
 of all the packages at any given time. For example, the user should be able to 
 provide the time 10:47 and see a printout of every packages’ status and info (listed in part F). 
 Using this functionality, the evaluator can verify that your delivery solution is valid. 
'''

