d = {
    "a": {},
    "b": 6,
    "c": {
        "f": 9,
        "g": {
            "m": 17,
            "n": 3
        }
    }
}

def flatten(d: dict):
    res_dict = dict()
    for key in d:
        if type(d[key]) != dict:
           res_dict[key] = d[key]
        else:
            if len(d[key]) == 0:
                res_dict[key] = None
            new_res_dict = flatten(d[key])
            for new_key in new_res_dict:
                res_dict[f"{key}.{new_key}"] = new_res_dict[new_key]
    return res_dict

print(flatten(d))