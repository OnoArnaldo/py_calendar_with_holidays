import calendar as _cal
import datetime as _dt


class HTMLCalendar(_cal.HTMLCalendar):
    cssclass_holiday = 'holiday'

    def __init__(self, firstweekday=0, holidays=None, holiday_func=None):
        """
        :param firstweekday: 0 = Monday, 6 = Sunday
        :param holidays: make sure the list is sorted
        """
        super(HTMLCalendar, self).__init__(firstweekday)

        if holidays is not None and holiday_func is not None:
            raise Exception('Only one of the parameters can be set (holidays, holiday_func)')

        self.holidays = holidays
        self.holiday_func = holiday_func
        self.current_year = 0
        self.current_month = 0

    def _is_holiday_from_list(self, theyear, themonth, theday, lower=None, higher=None):
        if lower is None:
            lower = 0
        if higher is None:
            higher = len(self.holidays) - 1

        if higher < lower:
            return False

        middle = (lower + higher) // 2
        thedate = _dt.date(theyear, themonth, theday)

        if self.holidays[middle] == thedate:
            return True
        elif self.holidays[middle] < thedate:
            return self._is_holiday_from_list(theyear, themonth, theday, middle + 1, higher)
        else:
            return self._is_holiday_from_list(theyear, themonth, theday, lower, middle - 1)

    def _is_holiday_from_func(self, theyear, themonth, theday):
        return self.holiday_func(theyear, themonth, theday)

    def is_holiday(self, theyear, themonth, theday):
        if self.holidays is not None:
            return self._is_holiday_from_list(theyear, themonth, theday)
        elif callable(self.holiday_func):
            return self._is_holiday_from_func(theyear, themonth, theday)

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        elif self.is_holiday(self.current_year, self.current_month, day):
            return '<td class="%s %s">%d</td>' % (self.cssclasses[weekday], self.cssclass_holiday, day)
        else:
            return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)

    def formatmonth(self, theyear, themonth, withyear=True):
        self.current_year = theyear
        self.current_month = themonth

        return super(HTMLCalendar, self).formatmonth(theyear, themonth, withyear)
