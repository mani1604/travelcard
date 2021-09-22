from fare_strategy import FareStrategy
from capping import CappingLimit
from utility import Utility
from generate_data import GenerateDaily, GenerateWeekly


class FareCalculator:
    def __init__(self, journey_details):
        self.journey_details = journey_details
        self.zones_travelled = dict()
        self.daily_data = dict()
        self.out = dict()

    def calculate_fare(self):
        cap_limit = CappingLimit()
        self.out['total'] = 0
        for journey in self.journey_details:
            day = journey[0]
            util = Utility()
            week = util.get_week_num(day)
            util.check_zone_validity(journey[2])
            util.check_zone_validity(journey[3])

            fare = FareStrategy(*journey)
            journey_fare = fare.get_fare()
            generate_week = GenerateWeekly(self.out, week, day, journey_fare)
            generate_week.generate_data()
            updated_fare = cap_limit.apply_capping(self.out, week, day, self.zones_travelled, journey, journey_fare)
            self.out['total'] += updated_fare
            generate_daily = GenerateDaily(self.daily_data, day, updated_fare)
            generate_daily.generate_data()

        return self.out, self.zones_travelled, self.daily_data
