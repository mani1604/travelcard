import csv
from calculate_fare import FareCalculator

c = list()
with open('input_file.csv', 'r') as cf:
    csv_reader = csv.reader(cf, delimiter=',')
    fields = next(csv_reader)
    for row in csv_reader:
        c.append(row)

fc = FareCalculator(c)
data, zones, daily_data = fc.calculate_fare()

print(f"\nTotal fare for the input journey: {data['total']}")
del data['total']

print("\nZones travelled by the passenger ::")
for week in zones:
    print(f'Week number: {week} -> {zones[week]["week"]}')
    for day in zones[week]:
        if day == 'week':
            continue
        print(f'\t{day}: {zones[week][day]}')

print("\nFares per day per journey ::")
for date in daily_data:
    print(f'{date}=>', end='')
    i = 1
    for journey in daily_data[date]:
        print(f'\tJourney_{i}: {journey}', end='')
        i += 1
    print()

print("\nWeekly summary "
      "::")
for d in data:
    print(f'Week number: {d}')
    print(f"\tTotal: {data[d]['total']}")
    for daily in data[d]:
        if daily == 'total':
            continue
        print(f'\t{daily}: {data[d][daily]}')
