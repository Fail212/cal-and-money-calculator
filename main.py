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

    def get_today_cash_remained(self, currency):
        pass

    def get_today_calories_remained(self, currency):
        pass

    def get_week_stats(self):
        pass


class CaloriesCalculator(Calculator):
    pass


class CashCalculator(Calculator):
    pass


class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.date = date
        self.comment = comment


obj = CaloriesCalculator(100)

obj.add_record(100, 'Тест1', '12.2.1999')
obj.add_record(200, 'Тест2')
obj.add_record(2300, 'Тест2')

print(obj.get_today_stats())


