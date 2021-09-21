from utility import Utility
from constants import *


class Peak:
    def __init__(self, date, start_time):
        self.start_time = start_time
        self.date = date

    def get_peak_or_off_peak(self):
        util = Utility()
        time = datetime.datetime.strptime(self.start_time, '%H:%M').time()
        if util.is_weekend(self.date):
            if (nine_am <= time <= eleven_am) or (six_pm <= time <= ten_pm):
                return "peak"
        else:
            if (seven_am <= time <= ten_thirty_am) or (five_pm <= time <= eight_pm):
                return "peak"

        return "off-peak"
