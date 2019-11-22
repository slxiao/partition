from partition import greedy

def test_greedy(numbers):
    groups = greedy.greedy(numbers) 
    assert(min([sum(i) for i in groups])) == 13
    assert(max([sum(i) for i in groups])) == 17