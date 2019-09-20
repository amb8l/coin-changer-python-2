from context import changer

def test_passing_0_returns_an_empty_list():
    assert changer.calculate(0) == []

def test_passing_1_returns_a_single_penny():
    assert changer.calculate(1) == [1]

def test_passing_2_returns_2p():
    assert changer.calculate(2) == [2]

def test_passing_5_returns_5p():
    assert changer.calculate(5) == [5]

def test_passing_10_returns_10p():
    assert changer.calculate(10) == [10]

def test_passing_20_returns_20p():
    assert changer.calculate(20) == [20]