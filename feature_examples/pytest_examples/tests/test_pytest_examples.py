from pytest_examples import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_passing():
    assert (1,2,3) == (1,2,3)

def test_failing():
    assert (1,2,3) == (3,2,1)

