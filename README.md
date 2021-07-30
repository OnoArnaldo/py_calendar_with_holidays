# holidays_calendar

This is a simple modification to [calendar.HTMLCalendar](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar)
to allow holidays configuration.

> The only change is the holiday usage, everything else 
> can be checked in [python documentation](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar)

## Instalation

```shell
python3.9 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install git+https://github.com/OnoArnaldo/py_calendar_with_holidays.git
```

## Usage with list

```python
import datetime as dt
import holidays_calendar as calendar

cal = calendar.HTMLCalendar(holidays=[
    dt.date(2021, 1, 1), 
    dt.date(2021, 2, 1)
])

cal.formatyearpage(2021)
```

## Usage with function

```python
import holidays_calendar as calendar

def is_holiday(year, month, day):
    return (1, 1) == (month, day)


cal = calendar.HTMLCalendar(holiday_func=is_holiday)
cal.formatyearpage(2021)
```

## Custom classes

```python
import holidays_calendar as calendar


class CustomCalendar(calendar.HTMLCalendar):
    cssclass_holiday = 'is-holiday'


cal = CustomCalendar(holiday_func=is_holiday)
cal.formatyearpage(2021)
```
