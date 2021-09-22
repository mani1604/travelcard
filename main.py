import csv
from calculate_fare import FareCalculator

c = list()
with open('file.csv', 'r') as cf:
    csv_reader = csv.reader(cf, delimiter=',')
    for row in csv_reader:
        c.append(row)

fc = FareCalculator(c)
total = 0
data, zones, daily_data = fc.calculate_fare()
print(data)
print(zones)
print(daily_data)
for week in data:
    total += data[week]['total']

print(total)

