from zone import Zone


class CappingLimit:
    @staticmethod
    def get_daily_limit(zones):
        if zones == {'1', '2'} or zones == {'2', '1'}:
            return 120
        elif zones == {'1'}:
            return 100
        elif zones == {'2'}:
            return 80
        else:
            raise Exception

    @staticmethod
    def get_weekly_limit(zones):
        if zones == {'1', '2'} or zones == {'2', '1'}:
            return 600
        elif zones == {'1'}:
            return 500
        elif zones == {'2'}:
            return 400
        else:
            raise Exception

    @staticmethod
    def is_weekly_cap_reached(total, zones):
        limit = CappingLimit.get_weekly_limit(zones)
        if total >= limit:
            return True, limit
        return False, None

    @staticmethod
    def is_daily_cap_reached(total, zones):
        limit = CappingLimit.get_daily_limit(zones)
        if total >= limit:
            return True, limit
        return False, None

    @staticmethod
    def apply_capping(travel_data, week, day, zones_travelled, journey, journey_fare):
        extra_fare = 0
        zone = Zone()
        zones_travelled = zone.get_zones_travelled(zones_travelled, week, day, journey)
        week_cap_reached, weekly_cap = CappingLimit.is_weekly_cap_reached(travel_data[week]['total'],
                                                                          zones_travelled[week]['week'])
        if week_cap_reached:
            extra_fare = travel_data[week]['total'] - weekly_cap
            travel_data[week][day] -= extra_fare
            travel_data[week]['total'] -= extra_fare

        daily_cap_reached, daily_cap = CappingLimit.is_daily_cap_reached(travel_data[week][day],
                                                                         zones_travelled[week][day])
        if daily_cap_reached:
            extra_fare = travel_data[week][day] - daily_cap
            travel_data[week][day] -= extra_fare
            travel_data[week]['total'] -= extra_fare

        return journey_fare - extra_fare
