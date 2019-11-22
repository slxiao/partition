from partition import kk

def test_kk(numbers):
    groups = kk.kk(numbers) 
    assert(min([sum(i) for i in groups])) == 14
    assert(max([sum(i) for i in groups])) == 16