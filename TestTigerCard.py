import unittest
from fare_strategy import FareStrategy
from peak import Peak
from utility import Utility
from zone import Zone
from calculate_fare import FareCalculator
from capping import CappingLimit
from generate_data import GenerateDaily, GenerateWeekly


class TestCases(unittest.TestCase):
    def test_get_fare(self):
        strategy = FareStrategy('12-09-2021', '19:00', '2', '2')
        fare = strategy.get_fare()
        self.assertEqual(fare, 25)

    def test_get_peak_or_off_peak(self):
        peak = Peak('13-09-2021', '19:00')
        peak_or_not = peak.get_peak_or_off_peak()
        self.assertEqual(peak_or_not, 'peak')

        peak1 = Peak('14-09-2021', '16:00')
        peak_or_not1 = peak1.get_peak_or_off_peak()
        self.assertEqual(peak_or_not1, 'off-peak')

    def test_is_weekend(self):
        util = Utility()
        weekend1 = util.is_weekend('19-09-2021')
        self.assertEqual(weekend1, True)

        weekend2 = util.is_weekend('17-09-2021')
        self.assertEqual(weekend2, False)

    def test_get_week_num(self):
        util = Utility()
        week_num = util.get_week_num('19-09-2021')
        self.assertEqual(week_num, 37)

        week_num1 = util.get_week_num('05-01-2021')
        self.assertEqual(week_num1, 1)

    def test_check_zone_validity(self):
        util = Utility()
        self.assertRaises(Exception, util.check_zone_validity, '3')

        valid = util.check_zone_validity('1')
        self.assertEqual(True, valid)

    def test_load_config(self):
        util = Utility()
        data1 = util.load_config('a.json')
        self.assertEqual(data1, False)

        data2 = util.load_config('fare_config.json')
        fare1 = data2["fares"]["1"]["1"]["peak"]
        self.assertEqual(fare1, 30)

    def test_get_zones_travelled(self):
        zone = Zone()
        previous_zones_travelled = {37: {'19-09-2021': {'1'}, 'week': {'1'}}}
        journey = ('19-09-2021', '19:00', '2', '2')
        day = journey[0]
        util = Utility()
        week_num = util.get_week_num(day)
        zones_travelled = zone.get_zones_travelled(previous_zones_travelled, week_num, day, journey)
        expected = {37: {'19-09-2021': {'1', '2'}, 'week': {'1', '2'}}}
        self.assertEqual(zones_travelled, expected)

    def test_calculate_fare(self):
        journey_details = [('13-09-2021', '10:00', '2', '1'), ('13-09-2021', '19:00', '1', '2')]
        calculator = FareCalculator(journey_details)
        total = calculator.calculate_fare()
        self.assertEqual(total, 70)

    def test_get_limit(self):
        cap = CappingLimit()
        limit1 = cap.get_limit({'1'}, 'day')
        self.assertEqual(limit1, 100)

        self.assertRaises(Exception, cap.get_limit, {'1'}, 'wrong_key')

    def test_is_cap_reached(self):
        cap = CappingLimit()
        cap_reached1, limit1 = cap.is_cap_reached(550, {'1', '2'}, 'week')
        self.assertEqual(cap_reached1, False)
        self.assertEqual(limit1, None)

        cap_reached2, limit2 = cap.is_cap_reached(610, {'1', '2'}, 'week')
        self.assertEqual(cap_reached2, True)
        self.assertEqual(limit2, 600)

        cap_reached2, limit2 = cap.is_cap_reached(135, {'1', '2'}, 'day')
        self.assertEqual(cap_reached2, True)
        self.assertEqual(limit2, 120)

    def test_apply_capping(self):
        cap = CappingLimit()
        data = {37: {'13-09-2021': 145, 'total': 145}}
        journey = ('13-09-2021', '19:00', '2', '2')
        zones = {37: {'13-09-2021': {'1', '2'}, 'week': {'1', '2'}}}
        new_fare = cap.apply_capping(data, 37, '13-09-2021', zones, journey, 30)
        self.assertEqual(new_fare, 5)

        data1 = {37: {'13-09-2021': 90, 'total': 145}}
        journey1 = ('13-09-2021', '19:00', '2', '2')
        zones1 = {37: {'13-09-2021': {'1', '2'}, 'week': {'1', '2'}}}
        new_fare = cap.apply_capping(data1, 37, '13-09-2021', zones1, journey1, 30)
        self.assertEqual(new_fare, 30)

    def test_generate_data_daily(self):
        gen = GenerateDaily()
        daily_data1 = {'13-09-2021': [35, 25, 25, 30]}
        updated_data1 = gen.generate_data(daily_data1, '14-09-2021', 25)
        expected_data1 = {'13-09-2021': [35, 25, 25, 30], '14-09-2021': [25]}
        self.assertEqual(updated_data1, expected_data1)

        daily_data2 = {'13-09-2021': [35, 25, 25, 30]}
        updated_data2 = gen.generate_data(daily_data2, '13-09-2021', 5)
        expected_data2 = {'13-09-2021': [35, 25, 25, 30, 5]}
        self.assertEqual(updated_data2, expected_data2)

    def test_generate_data_weekly(self):
        gen = GenerateWeekly(38)
        weekly_data1 = {37: {'13-09-2021': 120, 'total': 120}}
        updated_data1 = gen.generate_data(weekly_data1, '14-09-2021', 25)
        expected_data1 = {37: {'13-09-2021': 120, 'total': 120}, 38: {'14-09-2021': 25, 'total': 25}}
        self.assertEqual(updated_data1, expected_data1)
