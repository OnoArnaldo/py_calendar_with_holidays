import holidays_calendar


def is_holiday(year, month, day):
    return (year, month, day) in [(2021, 1, 1), (2021, 12, 25)]


def test_is_holiday():
    cal = holidays_calendar.HTMLCalendar(holiday_func=is_holiday)

    assert cal.is_holiday(2021, 1, 1)
    assert not cal.is_holiday(2021, 6, 30)
    assert cal.is_holiday(2021, 12, 25)
