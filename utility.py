import json
import datetime


class Utility:
    zones = ['1', '2']

    @staticmethod
    def load_config():
        try:
            with open('fare_config.json', mode='r') as config_file:
                return json.loads(config_file.read())
        except FileNotFoundError:
            return False

    @staticmethod
    def is_weekend(date):
        day_num = datetime.datetime.strptime(date, '%d-%m-%Y').weekday()
        if day_num == 5 or day_num == 6:
            return True
        return False

    @staticmethod
    def get_week_num(date):
        y, m, d = date.split('-')[::-1]
        y = int(y)
        m = int(m)
        d = int(d)
        return datetime.date(y, m, d).isocalendar()[1]
