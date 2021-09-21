from utility import Utility


class Zone:
    @staticmethod
    def get_travelled_zones_for_day(journey_details):
        zones_travelled = dict()
        for journey in journey_details:
            start_zone = str(journey[2])
            end_zone = str(journey[3])
            if journey[0] in zones_travelled:
                zones_travelled[journey[0]].add(start_zone)
                zones_travelled[journey[0]].add(end_zone)
            else:
                zones_travelled[journey[0]] = {start_zone, end_zone}

        return zones_travelled

    @staticmethod
    def get_travelled_zones_for_week(daily_details):
        zones_travelled = dict()

        for daily in daily_details:
            util = Utility()
            week = util.get_week_num(daily)
            if week in zones_travelled:
                zones_travelled[week] = zones_travelled[week].union(daily_details[daily][1])
            else:
                zones_travelled[week] = daily_details[daily][1]

        return zones_travelled
