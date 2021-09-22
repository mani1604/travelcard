from abc import ABC, abstractmethod


class Generate(ABC):
    @abstractmethod
    def generate_data(self):
        pass


class GenerateWeekly(Generate):
    def __init__(self, weekly_data, week, day, journey_fare):
        self.weekly_data = weekly_data
        self.week = week
        self.day = day
        self.journey_fare = journey_fare

    def generate_data(self):
        if self.week in self.weekly_data:
            if self.day in self.weekly_data[self.week]:
                self.weekly_data[self.week][self.day] += self.journey_fare
            else:
                self.weekly_data[self.week][self.day] = self.journey_fare

            if 'total' in self.weekly_data[self.week]:
                self.weekly_data[self.week]['total'] += self.journey_fare
            else:
                self.weekly_data[self.week]['total'] = self.journey_fare
        else:
            self.weekly_data[self.week] = {}
            self.weekly_data[self.week][self.day] = self.journey_fare
            self.weekly_data[self.week]['total'] = self.journey_fare


class GenerateDaily(Generate):
    def __init__(self, daily_data, day, fare):
        self.daily_data = daily_data
        self.day = day
        self.fare = fare

    def generate_data(self):
        if self.day in self.daily_data:
            self.daily_data[self.day].append(self.fare)
        else:
            self.daily_data[self.day] = [self.fare]
