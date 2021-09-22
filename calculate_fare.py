from fare_strategy import FareStrategy
from capping import CappingLimit
from utility import Utility
from zone import Zone
from tigercard_execption import InvalidZone


class FareCalculator:
    def __init__(self, journey_details):
        self.journey_details = journey_details

    def calculate_fare(self):
        out = dict()
        daily_data = dict()
        zones_travelled = dict()
        for journey in self.journey_details:
            day = journey[0]
            util = Utility()
            week = util.get_week_num(day)

            z = Zone()
            if not util.is_valid_zone(journey[2]):
                raise InvalidZone(journey[2])

            if not util.is_valid_zone(journey[3]):
                raise InvalidZone(journey[3])

            zones_travelled = z.get_zones_travelled(zones_travelled, week, day, journey)

            f = FareStrategy(*journey)
            journey_fare = f.get_fare()

            if week in out:
                if day in out[week]:
                    out[week][day] += journey_fare
                else:
                    out[week][day] = journey_fare

                if 'total' in out[week]:
                    out[week]['total'] += journey_fare
                else:
                    out[week]['total'] = journey_fare

                c = CappingLimit()
                updated_fare = c.put_capping(out, week, day, zones_travelled, journey_fare)
            else:
                out[week] = {}
                out[week][day] = journey_fare
                out[week]['total'] = journey_fare
                updated_fare = journey_fare

            daily_data = FareCalculator.get_daily_data(daily_data, day, updated_fare)

        return out, zones_travelled, daily_data

    @staticmethod
    def get_daily_data(data, day, fare):
        if day in data:
            data[day].append(fare)
        else:
            data[day] = [fare]

        return data


