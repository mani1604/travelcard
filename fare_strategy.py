from peak import Peak
from utility import Utility


class FareStrategy:
    def __init__(self, date, start_time, start_zone, end_zone):
        self.date = date
        self.start_time = start_time
        self.start_zone = str(start_zone)
        self.end_zone = str(end_zone)

    def get_fare(self):
        util = Utility()
        data = util.load_config()
        peak = Peak(self.date, self.start_time)
        peak_off_peak = peak.get_peak_or_off_peak()
        fare = data["fares"][self.start_zone][self.end_zone][peak_off_peak]

        return fare
