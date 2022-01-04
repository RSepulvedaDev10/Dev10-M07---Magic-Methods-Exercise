import csv
       
class Astronaut:
    def __init__(self, name, flightHours, status):
        self.name = name
        self.flightHours = flightHours
        self.status = status
        
    def __str__(self):
        return self.name + ', ' + self.status
        
    def __gt__(self, other):
        print('__gt__ called - self: %s, other: %s' % (self,other))
        if self.flightHours > other.flightHours:
            print('True')
        else:
            print('False')
    
    def __eq__(self, other):
        ('__eq__ called')
        if self.flightHours == other.flightHours:
            print('True')
        else:
            print('False')
        
    def __ge__(self, other):
        ('__ge__ called')
        if self.flightHours >= other.flightHours:
            print('True')
        else:
            print('False')
        
findings = []
with open("astronauts.csv","r") as csvfile:
    astronautReader = csv.DictReader(csvfile)
    for row in astronautReader:
        findings.append(row)
        
findings = [Astronaut(astronaut['Name'], int(astronaut['Space Flight (hr)']), astronaut['Status']) for astronaut in findings]

print(findings[1])

findings[7] > findings[13]

findings[3] == findings[6]

findings[10] >= findings[35]