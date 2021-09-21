from fare_strategy import FareStrategy
from cap import CappedLimit


class DailyFareCalculator:
    def __init__(self, journey_details):
        self.journey_details = journey_details

    def calculate_fare(self):
        daily_fares = dict()
        for journey in self.journey_details:
            f = FareStrategy(*journey)
            if journey[0] in daily_fares:
                daily_fares[journey[0]] += f.get_fare()
            else:
                daily_fares[journey[0]] = f.get_fare()

        return daily_fares

    def calculate_capped_fare(self):
        daily_capped_fare = dict()
        fares = self.calculate_fare()
        for f in fares:
            limit = CappedLimit()
            capped_limit, zones = limit.get_daily_limit(f, self.journey_details)
            if fares[f] > capped_limit:
                daily_capped_fare[f] = (capped_limit, zones)
            else:
                daily_capped_fare[f] = (fares[f], zones)

        return daily_capped_fare



