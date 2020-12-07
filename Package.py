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
        self.pickupTime = None

    def packageView(self):
        return {'packageId': self.packageId, 'address': self.address, 'city': self.city, 'state': self.state, 'zipcode': self.zipCode, 'deadline': self.deadline, 'mass': self.mass,
        'packageLocation': self.packageLocation,'pickupTime': self.pickupTime}

    def get(self, attribute):
        return getattr(self, attribute)

    def __getitem__(self, attribute):
        return getattr(self, attribute)

    def __setitem__(self, attribute, newValue):
        return setattr(self, attribute, newValue)

    




    