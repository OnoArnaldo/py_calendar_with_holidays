import datetime as dt
import holidays_calendar


def test_format_day():
    cal = holidays_calendar.HTMLCalendar(holidays=sorted([dt.date(2021, 1, 1), dt.date(2021, 12, 25), dt.date(2021, 6, 30)]))
    cal.current_year = 2021
    cal.current_month = 1

    assert cal.formatday(1, dt.date(2021, 1, 1).weekday()) == '<td class="fri holiday">1</td>'
    assert cal.formatday(2, dt.date(2021, 2, 1).weekday()) == '<td class="mon">2</td>'


def test_custom_HTMLCalendar():
    class CustomHTMLCalendar(holidays_calendar.HTMLCalendar):
        cssclass_holiday = 'hol'

    cal = CustomHTMLCalendar(holidays=sorted([dt.date(2021, 1, 1), dt.date(2021, 12, 25), dt.date(2021, 6, 30)]))
    cal.current_year = 2021
    cal.current_month = 1

    assert cal.formatday(1, dt.date(2021, 1, 1).weekday()) == '<td class="fri hol">1</td>'
