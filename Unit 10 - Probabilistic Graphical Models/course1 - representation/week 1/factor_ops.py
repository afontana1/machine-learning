
def reduce_factor(factor, variable, value):
    reduced = []
    for row in factor:
        if row[variable] == value:
            r = row.copy()
            del r[variable]
            reduced.append(r)
    return reduced


def marginalize_factor(factor, variable):
    result = {}

    for row in factor:
        key = tuple(
            (k, v)
            for k, v in row.items()
            if k not in (variable, "value")
        )
        result[key] = result.get(key, 0) + row["value"]

    output = []
    for key, value in result.items():
        r = dict(key)
        r["value"] = value
        output.append(r)

    return output
