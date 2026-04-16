from cart import calculate_total

def test_total():
    assert calculate_total([10, 20]) == 30
