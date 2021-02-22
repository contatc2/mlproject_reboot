from mlproject.distance import haversine

def test_type_of_result():
    assert isinstance(haversine(48.865070, 2.380009, 48.235070, 2.393409), float)


def test_result_accuracy():
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) == 70.00789153218594

