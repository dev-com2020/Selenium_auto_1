import csv
import pytest

@pytest.fixture
def series():
    with open("series.csv", "r", newline="") as file:
        return list(csv.reader(file))

GENRE = 4

@pytest.fixture
def comedy_series(series):
    return [x for x in series if x[GENRE] == 'comedy']

def test_comedy_series(comedy_series):
    assert all(series[GENRE] == 'comedy' for series in comedy_series)
