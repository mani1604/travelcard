from abc import ABC, abstractmethod


class Generate(ABC):
    @abstractmethod
    def generate_data(self, data, day, fare):
        pass


class GenerateWeekly(Generate):
    def __init__(self, week):
        self.week = week

    def generate_data(self, data, day, fare):
        if self.week in data:
            if day in data[self.week]:
                data[self.week][day] += fare
            else:
                data[self.week][day] = fare

            if 'total' in data[self.week]:
                data[self.week]['total'] += fare
            else:
                data[self.week]['total'] = fare
        else:
            data[self.week] = {}
            data[self.week][day] = fare
            data[self.week]['total'] = fare


class GenerateDaily(Generate):
    def generate_data(self, data, day, fare):
        if day in data:
            data[day].append(fare)
        else:
            data[day] = [fare]
