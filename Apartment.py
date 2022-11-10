#Apartment.py
class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.rent, self.metersFromUCSB, self.condition)

    def __gt__(self, other):
        cond = ["excellent", "average", "bad" ]
        if self.rent > other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB > other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                return cond.index(self.condition) > cond.index(other.condition)              
        return False

    def __lt__(self, other):
        cond = ["excellent", "average", "bad" ]
        if self.rent < other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                return cond.index(self.condition) < cond.index(other.condition) 
        return False

    def __eq__(self, other):
        if self.rent == other.rent and self.metersFromUCSB == other.metersFromUCSB and self.condition == other.condition:
            return True
        return False