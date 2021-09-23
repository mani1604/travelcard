from zone import Zone
from tigercard_execption import TigerCardException
from utility import Utility


class CappingLimit:
    @staticmethod
    def get_limit(zones, cap_type):
        util = Utility()
        data = util.load_config()
        zones_str = ''
        try:
            for zone in zones:
                zones_str += zone
            return data["capping"][cap_type][zones_str]
        except Exception:
            raise TigerCardException

    def is_cap_reached(self, total, zones, cap_type):
        limit = self.get_limit(zones, cap_type)
        if total >= limit:
            return True, limit
        return False, None

    def apply_capping(self, travel_data, week, day, zones_travelled, journey, journey_fare):
        extra_fare = 0
        zone = Zone()
        zones_travelled = zone.get_zones_travelled(zones_travelled, week, day, journey)

        week_cap_reached, weekly_cap = self.is_cap_reached(travel_data[week]['total'], zones_travelled[week]['week'],
                                                           "week")
        if week_cap_reached:
            extra_fare = travel_data[week]['total'] - weekly_cap
            travel_data[week][day] -= extra_fare
            travel_data[week]['total'] -= extra_fare

        daily_cap_reached, daily_cap = self.is_cap_reached(travel_data[week][day], zones_travelled[week][day], "day")
        if daily_cap_reached:
            extra_fare = travel_data[week][day] - daily_cap
            travel_data[week][day] -= extra_fare
            travel_data[week]['total'] -= extra_fare

        return journey_fare - extra_fare
