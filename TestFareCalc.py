from old_fare import FareCalculator


def test_CanInstantiate():
    fare = FareCalculator()

def test_CanGetTime():
    fc = FareCalculator()
    fc.get_time()
