import datetime as dt


class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.date = date
        self.comment = comment


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
    courses = {'rub': [1, '₽'], 'eur': [100, '€'], 'usd': [90, '$']}

    def get_today_cash_remained(self, currency):
        stats = self.get_today_stats()
        balance: float = self.limit - stats

        if 0 < balance < self.limit:
            return f'На сегодня осталось {round(balance / self.courses[currency][0], 2)} {self.courses[currency][1]}'
        elif balance == 0:
            return 'Денег нет, держись'
        elif balance < 0:
            return f'Денег нет, держись: твой долг {round(balance / self.courses[currency][0], 2)} {self.courses[currency][1]}'


class CaloriesCalculator(Calculator):
    def get_today_calories_remained(self, currency):
        pass




obj = CashCalculator(1000)

obj.add_record(500, 'Тест1', '18.11.2023')
obj.add_record(500, 'Тест2', '19.11.2023')
obj.add_record(1235.9, 'Тест3', '27.11.2023')



print(obj.get_today_cash_remained('eur'))
print(obj.get_today_cash_remained('usd'))




