class Zone:
    @staticmethod
    def get_travelled_zones_for_week(daily_zone_details, week, day, previous_zones=None):
        zones_travelled = set()
        weekly_zone_details = daily_zone_details[week]
        if previous_zones:
            zones_travelled = weekly_zone_details['week'].union(weekly_zone_details[day])
        else:
            zones_travelled = zones_travelled.union(weekly_zone_details[day])

        for day in weekly_zone_details:
            zones_travelled.union(weekly_zone_details[day])

        return zones_travelled

    @staticmethod
    def get_travelled_zones_for_journey(journey, previous_zones=None):
        zones_travelled = set()
        start_zone = str(journey[2])
        end_zone = str(journey[3])
        if previous_zones:
            zones_travelled = previous_zones.union(start_zone)
        else:
            zones_travelled = zones_travelled.union(start_zone)

        zones_travelled = zones_travelled.union(end_zone)

        return zones_travelled

    @staticmethod
    def get_zones_travelled(zones_travelled, week, day, journey):
        if week in zones_travelled:
            if day in zones_travelled[week]:
                zones_travelled[week][day] = Zone.get_travelled_zones_for_journey(journey, zones_travelled[week][day])
            else:
                zones_travelled[week][day] = Zone.get_travelled_zones_for_journey(journey)
        else:
            zones_travelled[week] = {}
            zones_travelled[week][day] = Zone.get_travelled_zones_for_journey(journey)

        if 'week' in zones_travelled[week]:
            zones_travelled[week]['week'] = Zone.get_travelled_zones_for_week(zones_travelled, week, day,
                                                                              zones_travelled[week]['week'])
        else:
            zones_travelled[week]['week'] = Zone.get_travelled_zones_for_week(zones_travelled, week, day)

        return zones_travelled
