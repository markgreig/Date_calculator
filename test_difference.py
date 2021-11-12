# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:08:45 2021

@author: mgreig
"""
from datecalc import duration, when
import datetime

def test_difference():
    start_date = datetime.date(2021, 11, 10)
    end_date = datetime.date(2021, 11, 11)
    difference = duration(start_date, end_date)
    assert difference == 1
   
def test_newdate():
    start_date = datetime.date(2021, 11, 10)
    days_between = 2
    newdate = when(start_date, days_between)
    assert newdate == datetime.date(2021,11,12)
    