import datetime as dt
class Calculator:
    date_format = '%d.%m.%Y'
    records = []

    def __init__(self, limit):
        self.limit = limit

    def add_record(self, amount, comment, date: str = dt.date.today()):
        if type(date) == str:
            date = dt.datetime.strptime(date, self.date_format)
            date = date.date()
        self.records.append(Record(amount, comment, date))

    def get_today_stats(self):
        stats = 0
        day = dt.date.today()
        for i in self.records:
            if i.date == day:
                stats += i.amount
        return stats


    def get_week_stats(self):
        week_delta = dt.date.today() - dt.timedelta(days=7)
        stats = 0
        for i in self.records:
            if i.date >= week_delta:
                stats += i.amount
        return stats


class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
        stats = self.get_today_stats()
        return self.limit - stats


class CaloriesCalculator(Calculator):
    def get_today_calories_remained(self, currency):
        pass


class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.date = date
        self.comment = comment


obj = CashCalculator(1000)

obj.add_record(500, 'Тест1', '18.11.2023')
obj.add_record(500, 'Тест2', '19.11.2023')
obj.add_record(100, 'Тест3', '27.11.2023')

print(obj.get_week_stats())
print(obj.get_today_stats())
print()

print(obj.get_today_cash_remained('rub'))