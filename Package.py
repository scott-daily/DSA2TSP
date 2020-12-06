class Package:
    def __init__(self, address, city, state, zip_code, delivery_deadline, mass_kg):
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zip_code
        self.deadline = delivery_deadline
        self.mass = mass_kg
        self.packageLocation = "At the hub"
        self.pickupTime = None

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zipCode

    def getDeadline(self):
        return self.deadline

    def getMass(self):
        return self.mass

    def getLocation(self):
        return self.packageLocation

    def getPickupTime(self):
        return self.pickupTime

    




    