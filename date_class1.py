class date():
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    def display(self):
        print(self.date,"-", self.month, "-", self.year)
        return self.date,self.month,self.year

    def __add__(self, days):
        self.date = self.date + days
        return self

today=date(12,9,2017)
today.display()
tomorrow=today + 1
tomorrow.display()
