from collections import OrderedDict


def get_diff(old, new):  # noqa: C901

    res = {}
    old_keys = set(old.keys()) - set(new.keys())
    for key in old_keys:
        res[key] = {'status': 'removed', 'value': old[key]}

    new_keys = set(new.keys()) - set(old.keys())
    for key in new_keys:
        res[key] = {'status': 'added', 'value': new[key]}

    for key in old.keys() & new.keys():
        old_val = old[key]
        new_val = new[key]
        if isinstance(old[key], dict) and isinstance(new[key], dict):
            res[key] = \
                {'status': 'nested', 'value':
                    get_diff(old_val, new_val)}
        elif old_val == new_val:
            res[key] = \
                {'status': 'unchanged', 'value': old_val}
        elif old_val != new_val:
            res[key] = \
                {'status': 'changed', 'old_value':
                    old_val, 'new_value': new_val}
    return OrderedDict(sorted(res.items()))
