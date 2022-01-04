import csv
       

        
findings = []
with open("astronauts.csv","r") as csvfile:
    astronautReader = csv.DictReader(csvfile)
    for row in astronautReader:
        finding = (row['Name'],row['Year'],row['Group'],row['Status'],row['Birth Date'],row['Birth Place'],row['Gender'],row['Alma Mater'],row['Undergraduate Major'],row['Graduate Major'],row['Military Rank'], row['Military Branch']),row['Space Flights'],row['Space Flight (hr)'],row['Space Walks'],row['Space Walks (hr)'],row['Missions'],row['Death Date'], row['Death Mission']
        findings.append(finding)

print(findings[0])

print(findings[0] > findings[1])