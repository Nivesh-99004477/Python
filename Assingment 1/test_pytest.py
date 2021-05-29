from arithmetic import arith
def test_arith():
    assert arith(2,8,4) == 4

from armstrong import armstr

def test_armstr():
    assert armstr(9474) == True

from biggestof import biggest

def test_biggest():
    assert biggest(9,8,7) == 9

from combi import combination

def test_combination():
    assert combination(4,2)== 6


from digiroot import digiRoot

def test_digiRoot():
    assert digiRoot("400") == 4

from factorial import fact

def test_fact():
    assert fact(8) == 40320

from fibonacci import fibo

def test_fibo():
    assert fibo(10) == 55

from HCF import hcf

def test_hcf():
    assert hcf(64,44) == 4

from LCM import lcm

def test_LCM():
    assert lcm(24,52) == 312


from leapyear import leap

def test_leap():
    assert leap(2002) == False

from prime import primeno

def test_primeno():
    assert primeno(13)== True

from quadratic import quad

def test_quadratic():
    assert quad(1,9,4)==[(-0.46887112585072543+0j), (-8.531128874149275+0j)]

from sumoffactors import sumfact

def test_sumfact():
    assert sumfact(6) == 12

from traingularsum import trisum

def test_trisum():
    assert trisum(4)==20

from tribonacci import tribo

def test_tribonacci():
    assert tribo(3)==1

from vowel import check

def test_check():
    assert check('c')==False

from reverse import rev

def test_reverse():
    assert rev(54321)==12345






























  


