from avgspeed import averagespeed

def test_averagespeed():
    assert averagespeed([0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0],2)==1.9749999999999999

from mean import mean 
def test_mean():
    assert mean([1,2,3,4,8,9])==4

from missno import missno
def test_missno():
    assert missno([5,6,7,8],[5,7,8])==[6]

from oddout import oddout
def test_oddout():
    assert oddout([5,5,5,8,5,5])==8

from diffbetlow import diffbetlow
def test_diffbetlow():
    assert diffbetlow([1,3,5,7,9])==2

from closest import closest
def test_closest():
    assert closest([1, 2, 3, 4, 5], 2.8)==3
    