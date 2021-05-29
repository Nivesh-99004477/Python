from shuffling import shuffling

def test_shuffling():
    assert shuffling(56321)==65321


from isogram import solve
def test_solve():
    assert solve("LTTS")== True

from ipaddress import ip

def test_ipaddress():
    assert ip('4.5.6.7')==67438087