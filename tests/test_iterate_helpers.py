from src.iterate_helpers import aggregate_values

def test_aggregate_values():
    assert aggregate_values({
        'x': [1, 2],
        'y': [3, 4],
        'z': [5, 6]
    }) == [
        {'x': 1, 'y': 3, 'z': 5},
        {'x': 1, 'y': 3, 'z': 6},
        {'x': 1, 'y': 4, 'z': 5},
        {'x': 1, 'y': 4, 'z': 6},
        {'x': 2, 'y': 3, 'z': 5},
        {'x': 2, 'y': 3, 'z': 6},
        {'x': 2, 'y': 4, 'z': 5},
        {'x': 2, 'y': 4, 'z': 6}
    ]