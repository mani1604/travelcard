from fare_strategy import FareStrategy


class FareCalculator:
    def __init__(self, journey_details):
        self.journey_details = journey_details

    def calculate_daily_fare(self):
        daily_dict = dict()
        for journey in self.journey_details:
            journey_fare = list()
            uncapped_fare = list()
            f = FareStrategy(*journey)
            fare = f.get_fare()
            journey_fare.append(fare)
            uncapped_fare.append(fare)
            if journey[0] in daily_dict:
                daily_dict[journey[0]]["actual_fares"] += uncapped_fare
                journey_fare = self.check_daily_cap(daily_dict[journey[0]]["calculated_fares"], journey_fare[0])
                daily_dict[journey[0]]["calculated_fares"] += journey_fare
                daily_dict[journey[0]]["zones_travelled"] += [journey[2], journey[3]]
            else:
                daily_dict[journey[0]] = {"calculated_fares": []}
                daily_dict[journey[0]] = {"actual_fares": []}
                daily_dict[journey[0]] = {"zones_travelled": []}
                daily_dict[journey[0]]["calculated_fares"] = journey_fare
                daily_dict[journey[0]]["actual_fares"] = uncapped_fare
                daily_dict[journey[0]]["zones_travelled"] = [journey[2], journey[3]]

        for i in daily_dict:
            out = sum(daily_dict[i]["calculated_fares"])
            daily_dict[i].update({"total_fare": out})
            unique_zones = list(set(daily_dict[i]["zones_travelled"]))
            daily_dict[i].update({"zones_travelled": unique_zones})

        return daily_dict

    def check_daily_cap(self, fare_list, latest_fair):
        daily_limit = 120
        if sum(fare_list) + latest_fair > daily_limit:
            new_last_fare = daily_limit - sum(fare_list)
            return [new_last_fare]
        else:
            return [latest_fair]

    def get_daily_limit(self):
        pass
