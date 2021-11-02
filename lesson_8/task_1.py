from datetime import date as dt
import re


class Date:
    sdate = (1900, 1, 1)
    fdate = (dt.today().year, dt.today().month, dt.today().day)

    def __init__(self, date):
        if type(date) == str and re.search('^\d{1,2}-\d{1,2}-\d{4}$', date):
            date = self.split_date(date)
            if (self.validate(date, Date.sdate, Date.fdate) == True):
                self.date = date
            else:
                raise ValueError(self.validate(date, Date.sdate, Date.fdate))
        else:
            raise ValueError("argument must be a string of 'day-month-year' format")

    def __str__(self):
        return '-'.join(map(str, self.date))

    @classmethod
    def split_date(cls, date):
        return list(map(int, reversed(date.split('-'))))

    @staticmethod
    def validate(date, sdate, fdate):
        if date[0] * 10000 + date[1] * 100 + date[2] in range(sdate[0] * 10000 + sdate[1] * 100 + sdate[2],
                                                              fdate[0] * 10000 + fdate[1] * 100 + fdate[2]):
            dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if date[0] % 400 == 0 or (date[0] % 4 == 0 and date[0] % 100 != 0):
                dim[1] = 29
            if date[1] in range(1, 12 + 1) and date[2] in range(1, dim[date[1] - 1] + 1):
                return True
            return 'Invalid date'
        return 'Date out of range'


a = Date('29-2-1904')
print(a)
