import csv
       
class Astronaut:
    def __init__(self, name, flightHours, flightUnits, status):
        self.name = name
        self.flightHours = flightHours
        self.flightUnits = flightUnits
        self.status = status
        
    def __str__(self, name, status):
        return self.name, self.status
        
    def __gt__(self, other):
        print('__gt__ called - self: %s, other: %s' % (self,other))
        if self.flightUnits == other.flightUnits:
            return self.flightHours > other.flightHours
        else:
            return False
    
    def __eq__(self, other):
        ('__eq__ called')
        if self.flightUnits == other.flightUnits:
            return self.flightHours == other.flightHours
        else:
            return False
        
    def __ge__(self, other):
        ('__ge__ called')
        if self.flightUnits == other.flightUnits:
            return self.flightHours >= other.flightHours
        else:
            return False
        
findings = []
with open("astronauts.csv","r") as csvfile:
    astronautReader = csv.DictReader(csvfile)
    for row in astronautReader:
        finding = (row['Name'],row['Year'],row['Group'],row['Status'],row['Birth Date'],row['Birth Place'],row['Gender'],row['Alma Mater'],row['Undergraduate Major'],row['Graduate Major'],row['Military Rank'], row['Military Branch']),row['Space Flights'],row['Space Flight (hr)'],row['Space Walks'],row['Space Walks (hr)'],row['Missions'],row['Death Date'], row['Death Mission']
        findings.append(finding)
        
print findings[0]