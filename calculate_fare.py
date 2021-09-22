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
        c = CappingLimit()
        self.out['total'] = 0
        for journey in self.journey_details:
            day = journey[0]
            util = Utility()
            week = util.get_week_num(day)
            util.check_zone_validity(journey[2])
            util.check_zone_validity(journey[3])

            f = FareStrategy(*journey)
            journey_fare = f.get_fare()
            gw = GenerateWeekly(self.out, week, day, journey_fare)
            gw.generate_data()
            updated_fare = c.apply_capping(self.out, week, day, self.zones_travelled, journey, journey_fare)
            self.out['total'] += updated_fare
            gd = GenerateDaily(self.daily_data, day, updated_fare)
            gd.generate_data()

        return self.out, self.zones_travelled, self.daily_data
