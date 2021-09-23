import csv
from calculate_fare import FareCalculator

c = list()
with open('input_file.csv', 'r') as cf:
    csv_reader = csv.reader(cf, delimiter=',')
    fields = next(csv_reader)
    for row in csv_reader:
        c.append(row)

calculate = FareCalculator(c)
total = calculate.calculate_fare()

print(f"\nTotal fare for the input journey: {total}")

# Below code is for details

zones = calculate.get_zones_travelled()
print("\nZones travelled by the passenger ::")
for week in zones:
    print(f'Week number: {week} -> {zones[week]["week"]}')
    for day in zones[week]:
        if day == 'week':
            continue
        print(f'\t{day}: {zones[week][day]}')

daily_data = calculate.get_daily_data()
print(daily_data)
print("\nFares per day per journey ::")
for date in daily_data:
    print(f'{date}=>', end='')
    i = 1
    for journey in daily_data[date]:
        print(f'\tJourney_{i}: {journey}', end='')
        i += 1
    print()

data = calculate.get_weekly_data()
print("\nWeekly summary ::")
for d in data:
    print(f'Week number: {d}')
    print(f"\tTotal: {data[d]['total']}")
    for daily in data[d]:
        if daily == 'total':
            continue
        print(f'\t{daily}: {data[d][daily]}')
