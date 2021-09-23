from fare_strategy import FareStrategy
from capping import CappingLimit
from utility import Utility
from generate_data import GenerateDaily, GenerateWeekly


class FareCalculator:
    def __init__(self, journey_details):
        self.journey_details = journey_details
        self._zones_travelled = dict()
        self._daily_data = dict()
        self._weekly_data = dict()
        self.total = 0

    def calculate_fare(self):
        cap = CappingLimit()
        for journey in self.journey_details:
            day = journey[0]
            util = Utility()
            week = util.get_week_num(day)
            util.check_zone_validity(journey[2])
            util.check_zone_validity(journey[3])

            fare = FareStrategy(*journey)
            journey_fare = fare.get_fare()

            weekly = GenerateWeekly(week)
            weekly.generate_data(self._weekly_data, day, journey_fare)

            updated_fare = cap.apply_capping(self._weekly_data, week, day, self._zones_travelled, journey, journey_fare)
            self.total += updated_fare

            daily = GenerateDaily()
            daily.generate_data(self._daily_data, day, updated_fare)

        return self.total

    def get_weekly_data(self):
        return self._weekly_data

    def get_daily_data(self):
        return self._daily_data

    def get_zones_travelled(self):
        return self._zones_travelled
