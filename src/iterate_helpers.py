import itertools

def aggregate_values(kv_map):
    map_keys = kv_map.keys()
    map_values = kv_map.values()

    all_matches = list(itertools.product(*map_values))
    return list(
        map(
            lambda vals: dict(zip(map_keys, vals)),
            all_matches
        )
    )
