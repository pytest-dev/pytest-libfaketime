import datetime

from libfaketime import fake_time


def test_faketime_1():
    with fake_time("2016-05-05 00:00:00"):
        assert datetime.datetime.now() == datetime.datetime(2016, 5, 5, 0, 0, 0)


def test_faketime_2():
    with fake_time("2016-05-05 00:00:00"):
        assert datetime.datetime.now() == datetime.datetime(2016, 5, 5, 0, 0, 0)


def test_faketime_3():
    with fake_time("2016-05-05 00:00:00"):
        assert datetime.datetime.now() == datetime.datetime(2016, 5, 5, 0, 0, 0)


def test_faketime_4():
    with fake_time("2016-05-05 00:00:00"):
        assert datetime.datetime.now() == datetime.datetime(2016, 5, 5, 0, 0, 0)
