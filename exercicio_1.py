import unittest
import datetime

class TestDate(unittest.TestCase):
    # datetime.date
    def test_date_is_valid(self):
        # Fixture Setup
        # Exercise SUT
        date = datetime.date(2026, 1, 1)
        # Verify Result
        self.assertEqual(date.year, 2026)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)
        # Fixture Teardown

    def test_date_is_invalid(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            date = datetime.date(2026, 1, 32)
        # Fixture Teardown

    def test_date_toordinal(self):
        # Fixture Setup
        date = datetime.date(1, 1, 1)  # primeiro dia do calendário
        # Exercise SUT
        ordinal = date.toordinal()
        # Verify Result
        self.assertEqual(ordinal, 1)
        # Fixture Teardown

    def test_date_toordinal_known_date(self):
        # Fixture Setup
        date = datetime.date(2026, 3, 17) 
        # Exercise SUT
        ordinal = date.toordinal()
        # Verify Result
        self.assertEqual(ordinal, 739692)
        # Fixture Teardown

    def test_date_fromordinal_to_known_date(self):
        # Fixture Setup
        known_date = datetime.date(2026, 3, 17) 
        # Exercise SUT
        date = datetime.date.fromordinal(739692)
        # Verify Result
        self.assertEqual(known_date, date)
        # Fixture Teardown

    def test_date_weekday_monday(self):
        # Fixture Setup
        date = datetime.date(2026, 3, 16)
        # Exercise SUT
        weekday = date.weekday()
        # Verify Result
        self.assertEqual(weekday, 0)
        # Fixture Teardown

    def test_date_weekday_sunday(self):
        # Fixture Setup
        date = datetime.date(2026, 3, 22)
        # Exercise SUT
        weekday = date.weekday()
        # Verify Result
        self.assertEqual(weekday, 6)
        # Fixture Teardown

    # datetime.time
    def test_time_is_valid(self):
        # Fixture Setup
        # Exercise SUT
        time = datetime.time(12, 0, 0)
        # Verify Result
        self.assertEqual(time.hour, 12)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)
        # Fixture Teardown

    def test_time_is_invalid_with_hour_greater_than_23(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            time = datetime.time(24, 0, 0)
        # Fixture Teardown

    def test_time_is_invalid_with_minute_greater_than_59(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            time = datetime.time(12, 60, 0)
        # Fixture Teardown

    def test_time_is_invalid_with_seconds_greater_than_59(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            time = datetime.time(12, 0, 60)
        # Fixture Teardown

    def test_time_is_invalid_with_negative_hour(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            time = datetime.time(-1, 0, 0)
        # Fixture Teardown

    def test_time_is_invalid_with_negative_minute(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            time = datetime.time(12, -1, 0)
        # Fixture Teardown

    def test_time_is_invalid_with_negative_seconds(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            time = datetime.time(12, 0, -1)
        # Fixture Teardown

    def test_time_isoformat(self):
        # Fixture Setup
        time = datetime.time(14, 30, 45)
        # Exercise SUT
        iso = time.isoformat()
        # Verify Result
        self.assertEqual(iso, "14:30:45")
        # Fixture Teardown

    def test_time_optional_arguments(self):
        # Fixture Setup
        # Exercise SUT
        time = datetime.time(12)
        # Verify Result
        self.assertEqual(time.hour, 12)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)
        # Fixture Teardown

    def test_time_comparison(self):
        # Fixture Setup
        morning = datetime.time(8, 0, 0)
        afternoon = datetime.time(14, 0, 0)
        # Exercise SUT
        result = morning < afternoon
        # Verify Result
        self.assertTrue(result)
        # Fixture Teardown
    
    def test_time_replace_hour(self):
        # Fixture Setup
        original = datetime.time(10, 30, 0)
        # Exercise SUT
        modified = original.replace(hour=15)
        # Verify Result
        self.assertEqual(modified.hour, 15)
        self.assertEqual(modified.minute, 30)
        self.assertEqual(original.hour, 10)
        # Fixture Teardown

    # datetime.datetime
    def test_datetime_minimum_valid(self):
        # Fixture Setup
        # Exercise SUT 
        dt = datetime.datetime(1, 1, 1, 0, 0, 0) 
        # Verify Result
        self.assertEqual(dt.year, 1)
        self.assertEqual(dt.month, 1)
        self.assertEqual(dt.day, 1)
        self.assertEqual(dt.hour, 0)
        self.assertEqual(dt.minute, 0)
        self.assertEqual(dt.second, 0)
        # Fixture Teardown

    def test_datetime_is_invalid_with_day_greater_than_31(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            dt = datetime.datetime(2026, 1, 32, 12, 0, 0)
        # Fixture Teardown

    def test_datetime_is_invalid_with_month_greater_than_13(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            dt = datetime.datetime(2026, 13, 1, 12, 0, 0)
        # Fixture Teardown

    def test_datetime_is_invalid_with_hour_greater_than_23(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            dt = datetime.datetime(2026, 1, 1, 24, 0, 0)
        # Fixture Teardown

    def test_datetime_is_invalid_with_minute_greater_than_59(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            dt = datetime.datetime(2026, 1, 1, 12, 60, 0)
        # Fixture Teardown

    def test_datetime_is_invalid_with_seconds_greater_than_59(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            dt = datetime.datetime(2026, 1, 1, 12, 0, 60)
        # Fixture Teardown

    def test_datetime_is_invalid_with_negative_hour(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            dt = datetime.datetime(2026, 1, 1, -1, 0, 0)
        # Fixture Teardown

    def test_datetime_is_invalid_with_negative_minute(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            dt = datetime.datetime(2026, 1, 1, 12, -1, 0)
        # Fixture Teardown

    def test_datetime_is_invalid_with_negative_seconds(self):
        # Fixture Setup
        # Exercise SUT and Verify Result
        with self.assertRaises(ValueError):
            dt = datetime.datetime(2026, 1, 1, 12, 0, -1)
        # Fixture Teardown

    # datetime.timedelta
    def test_timedelta_days_is_valid(self):
        # Fixture Setup
        td = datetime.timedelta(days=1)
        # Exercise SUT
        days = td.days
        # Verify Result
        self.assertEqual(days, 1)
        # Fixture Teardown

    def test_timedelta_seconds_is_valid(self):
        # Fixture Setup
        td = datetime.timedelta(seconds=7384)
        # Exercise SUT
        seconds = td.seconds
        # Verify Result
        self.assertEqual(seconds, 7384)
        # Fixture Teardown

    def test_timedelta_total_seconds(self):
        # Fixture Setup
        td = datetime.timedelta(days=1, hours=0, minutes=0, seconds=0)
        # Exercise SUT
        total_seconds = td.total_seconds()
        # Verify Result
        self.assertEqual(total_seconds, 86400)
        # Fixture Teardown

if __name__ == "__main__":
    unittest.main()
