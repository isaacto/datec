import datetime
import unittest

import datec


class DatecTest(unittest.TestCase):
    def test_period(self):
        dt = datetime.datetime(2019, 5, 15)
        self.assertEqual(dt + datec.Period(1, 'month'),
                         datetime.datetime(2019, 6, 15))
        self.assertEqual(dt + datec.parse('+1.5second'),
                         datetime.datetime(2019, 5, 15, 0, 0, 1, 500000))
        with self.assertRaises(datec.ParseError):
            datec.Period.parse('+1mon')

    def test_weekday(self):
        dt = datetime.datetime(2019, 5, 15)
        self.assertEqual(dt + datec.Weekday(1, datec.MON),
                         datetime.datetime(2019, 5, 20))
        self.assertEqual(dt + datec.Weekday.parse('+2mon'),
                         datetime.datetime(2019, 5, 27))
        self.assertEqual(dt + datec.Weekday.parse('-2WED'),
                         datetime.datetime(2019, 5, 1))
        self.assertEqual(dt + datec.parse('MON'),
                         datetime.datetime(2019, 5, 13))
        self.assertEqual(dt + datec.Weekday(0, datec.FRI),
                         datetime.datetime(2019, 5, 17))
        with self.assertRaises(datec.ParseError):
            datec.Weekday.parse('MO')

    def test_partialdate_simple(self):
        dt = datetime.datetime(2019, 5, 15, 8, 15)
        self.assertEqual(dt + datec.PartialDate(1),
                         datetime.datetime(2019, 5, 15, 8, 15))
        self.assertEqual(dt + datec.PartialDate(0, minute=7, second=16),
                         datetime.datetime(2019, 5, 15, 8, 7, 16))
        self.assertEqual(dt + datec.PartialDate(1, minute=7, second=16),
                         datetime.datetime(2019, 5, 15, 9, 7, 16))
        self.assertEqual(dt + datec.PartialDate(1, minute=17, second=16),
                         datetime.datetime(2019, 5, 15, 8, 17, 16))
        self.assertEqual(dt + datec.PartialDate(2, minute=7, second=16),
                         datetime.datetime(2019, 5, 15, 10, 7, 16))
        self.assertEqual(dt + datec.PartialDate.parse(':7:16'),
                         datetime.datetime(2019, 5, 15, 8, 7, 16))
        self.assertEqual(dt + datec.PartialDate.parse('-1x:7:16'),
                         datetime.datetime(2019, 5, 15, 8, 7, 16))
        self.assertEqual(dt + datec.PartialDate.parse('-1x:17:16'),
                         datetime.datetime(2019, 5, 15, 7, 17, 16))
        self.assertEqual(dt + datec.parse('-1x:17:16.2'),
                         datetime.datetime(2019, 5, 15, 7, 17, 16, 200000))
        with self.assertRaises(datec.ParseError):
            datec.PartialDate.parse('---')

    def test_partialdate_monthshift(self):
        dt = datetime.datetime(2019, 5, 15)
        self.assertEqual(dt + datec.PartialDate(1, month=2),
                         datetime.datetime(2020, 2, 15))
        self.assertEqual(dt + datec.PartialDate(-1, month=2),
                         datetime.datetime(2019, 2, 15))
        dt = datetime.datetime(2019, 5, 15)
        self.assertEqual(dt + datec.PartialDate.parse('+1x-2-'),
                         datetime.datetime(2020, 2, 15))
        dt = datetime.datetime(2019, 5, 30)
        self.assertEqual(dt + datec.PartialDate(1, month=2),
                         datetime.datetime(2020, 2, 29))

    def test_partialdate_dayshift(self):
        dt = datetime.datetime(2019, 5, 30)
        self.assertEqual(dt + datec.PartialDate(1, month=5, day=30),
                         datetime.datetime(2020, 5, 30))
        self.assertEqual(dt + datec.PartialDate(1, day=31),
                         datetime.datetime(2019, 5, 31))
        self.assertEqual(dt + datec.PartialDate(2, day=31),
                         datetime.datetime(2019, 7, 31))
        self.assertEqual(dt + datec.PartialDate(-1, day=31),
                         datetime.datetime(2019, 3, 31))
        dt = datetime.datetime(2019, 2, 15)
        self.assertEqual(dt + datec.PartialDate(1, day=30),
                         datetime.datetime(2019, 3, 30))
        with self.assertRaises(ValueError):
            dt + datec.PartialDate(1, month=2, day=30)
