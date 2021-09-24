import csv
import argparse
import sys
from calculate_fare import FareCalculator
from tigercard_execption import TigerCardException


def execute(file_name):
    c = list()
    try:
        with open(file_name, 'r') as cf:
            csv_reader = csv.reader(cf, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                c.append(row)
    except FileNotFoundError as error:
        print(error)
        sys.exit(1)

    calculate = FareCalculator(c)
    total = calculate.calculate_fare()
    print(f"\nTotal fare for the input journey: {total}")

    # Below code is just for details
    choice = input("\nDo you want to see the details?(y/n): ")
    if choice.lower() != 'y':
        sys.exit(0)

    zones = calculate.get_zones_travelled()
    print("\nZones travelled by the passenger ::")
    for week in zones:
        print(f'Week number: {week} -> {zones[week]["week"]}')
        for day in zones[week]:
            if day == 'week':
                continue
            print(f'\t{day}: {zones[week][day]}')

    daily_data = calculate.get_daily_data()
    print("\nFares per day per journey(capped) ::")
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find the total fare for the journeys by a commuter')
    parser.add_argument('-f', action='store', dest='input_file', required=True,
                        help='CSV file containing the journey details')
    args = parser.parse_args()
    input_file = args.input_file

    try:
        execute(input_file)
    except TigerCardException as err:
        print(err)
        sys.exit(1)
    except Exception as err:
        print(err)
        sys.exit(1)
    else:
        print('Completed')
