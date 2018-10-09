class YearQuarter():
    @staticmethod
    def fromDate(date=None):
        import datetime
        yearQuarter = YearQuarter(2017,1)
        if date is None:
            date = datetime.datetime.now()
        yearQuarter.year = date.year
        yearQuarter.quarter = (date.month - 1) // 3 + 1
        return yearQuarter

    def __init__(self,year,quarter):
        import datetime
        if year > datetime.datetime.now().year:
            self.year = datetime.datetime.now().year

        if quarter > 4:
            quarter = 4
        if quarter < 1:
            quarter = 1

        self.year = year
        self.quarter = quarter

    def __last__(self):
        if self.quarter <= 1:
            self.quarter = 4
            self.year = self.year - 1
        else:
            self.quarter = self.quarter - 1
        return self

    def __next__(self):
        if self.quarter >= 4:
            self.quarter = 1
            self.year = self.year + 1
        else:
            self.quarter = self.quarter + 1

        return self

    def __ge__(self, other):
        return self.year >= other.year and self.quarter >= other.quarter

    def __gt__(self, other):
        return (self.year > other.year) or (self.year == other.year and self.quarter > other.quarter)

    def __str__(self) -> str:
        return str({'year':self.year,'quarter':self.quarter})


class YearMonth():
    @staticmethod
    def fromDate(date=None):
        import datetime
        yearQuarter = YearQuarter(2017,1)
        if date is None:
            date = datetime.datetime.now()
        yearQuarter.year = date.year
        yearQuarter.month = date.month
        return yearQuarter

    def __init__(self,year,month):
        import datetime
        if year > datetime.datetime.now().year:
            self.year = datetime.datetime.now().year

        if month > 12:
            month = 12
        if month < 1:
            month = 1

        self.year = year
        self.month = month

    def __last__(self):
        if self.month <= 1:
            self.month = 12
            self.year = self.year - 1
        else:
            self.month = self.month - 1
        return self

    def __next__(self):
        if self.month >= 12:
            self.month = 1
            self.year = self.year + 1
        else:
            self.month = self.month + 1

        return self

    def __ge__(self, other):
        return self.year >= other.year and self.month >= other.quarter

    def __gt__(self, other):
        return (self.year > other.year) or (self.year == other.year and self.month > other.quarter)

    def __str__(self) -> str:
        return str({'year':self.year,'quarter':self.month})