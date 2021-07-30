import datetime as dt
import holidays_calendar


def test_is_holiday_empty_list():
    cal = holidays_calendar.HTMLCalendar(holidays=[])

    assert not cal.is_holiday(2021, 1, 1)
    assert not cal.is_holiday(2021, 12, 25)


def test_is_holiday_one_item():
    cal = holidays_calendar.HTMLCalendar(holidays=[dt.date(2021, 1, 1)])

    assert cal.is_holiday(2021, 1, 1)
    assert not cal.is_holiday(2020, 1, 1)


def test_is_holiday_multi_items():
    cal = holidays_calendar.HTMLCalendar(holidays=sorted([dt.date(2021, 1, 1), dt.date(2021, 12, 25), dt.date(2021, 6, 30)]))

    assert cal.is_holiday(2021, 1, 1)
    assert not cal.is_holiday(2021, 1, 13)
    assert cal.is_holiday(2021, 12, 25)
    assert cal.is_holiday(2021, 6, 30)
