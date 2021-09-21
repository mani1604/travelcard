from utility import Utility
from cap import CappedLimit


class WeeklyFareCalculator:
    def __init__(self, daily_fare_details):
        self.daily_fare_details = daily_fare_details

    def calculate_fare(self):
        weekly_fares = dict()
        for day in self.daily_fare_details:
            util = Utility()
            week = util.get_week_num(day)
            if week in weekly_fares:
                weekly_fares[week] += self.daily_fare_details[day][0]
            else:
                weekly_fares[week] = self.daily_fare_details[day][0]

        return weekly_fares

    def calculate_capped_fare(self):
        daily_capped_fare = dict()
        fares = self.calculate_fare()
        for f in fares:
            limit = CappedLimit()
            capped_limit = limit.get_weekly_limit(f, self.daily_fare_details)
            if fares[f] > capped_limit:
                daily_capped_fare[f] = capped_limit
            else:
                daily_capped_fare[f] = fares[f]

        return daily_capped_fare

