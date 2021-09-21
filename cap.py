from zone import Zone


class CappedLimit:
    z = Zone()

    @classmethod
    def get_daily_limit(cls, date, journey_details):
        zones = cls.z.get_travelled_zones_for_day(journey_details)
        if zones[date] == {'1', '2'} or zones[date] == {'2', '1'}:
            return 120, zones[date]
        elif zones[date] == {'1'}:
            return 100, zones[date]
        elif zones[date] == {'2'}:
            return 80, zones[date]
        else:
            raise Exception

    @classmethod
    def get_weekly_limit(cls, week_num, daily_fare_details):
        zones = cls.z.get_travelled_zones_for_week(daily_fare_details)
        if zones[week_num] == {'1', '2'} or zones[week_num] == {'2', '1'}:
            return 600
        elif zones[week_num] == {'1'}:
            return 500
        elif zones[week_num] == {'2'}:
            return 400
        else:
            raise Exception
