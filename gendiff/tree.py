from collections import OrderedDict


def get_diff(old, new):  # noqa: C901

    res = {}
    old_keys = set(old.keys()) - set(new.keys())
    for key in old_keys:
        res[key] = {'type': 'removed', 'value': old[key]}

    new_keys = set(new.keys()) - set(old.keys())
    for key in new_keys:
        res[key] = {'type': 'added', 'value': new[key]}

    for key in old.keys() & new.keys():
        old_val = old[key]
        new_val = new[key]
        if isinstance(old[key], dict) and isinstance(new[key], dict):
            res[key] = \
                {'type': 'nested', 'value':
                    get_diff(old_val, new_val)}
        elif old_val == new_val:
            res[key] = \
                {'type': 'unchanged', 'value': old_val}
        elif old_val != new_val:
            res[key] = \
                {'type': 'changed', 'old_value':
                    old_val, 'new_value': new_val}
    return OrderedDict(sorted(res.items()))
