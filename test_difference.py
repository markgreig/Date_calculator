# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:08:45 2021

@author: mgreig
"""
from datecalc import duration, when
import datetime, pytest

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
    
def test_input_boundary():
    start_date = datetime.date(2021, 11, 10)
    days_between = -1
    newdate_neg = when(start_date, days_between)
    assert newdate_neg == datetime.date(2021,11,9)
    
def duration_boundary():
    start_date = datetime.date(2021,11,10)
    end_date = datetime.date(100000,11,9)
    difference = duration(start_date, end_date)
    return difference
def test_duration_boundary():
    with pytest.raises(Exception):
        duration_boundary()
    
