from gendiff.formatters.normalize import normalize_values


def stringify(data):
    if isinstance(data, (set, tuple, list, dict)):
        return '[complex value]'
    elif data in ('null', 'true', 'false') or isinstance(data, (int, float)):
        return data
    else:
        return f"'{data}'"


msg = {
    'unchanged': '',
    'removed': "Property '{path}' was removed",
    'added': "Property '{path}' was added with value: {val}",
    'changed': "Property '{path}' was updated. From {old_val} to {new_val}"
}


def gen_plain_diff(diff, keys=None):
    if keys is None:
        keys = []
    lines = []
    for k, v in diff.items():
        status = v['type']
        keys.append(str(k))
        path = '.'.join(keys)
        if status == 'nested':
            lines.extend(gen_plain_diff(v['value'], keys))
            keys = keys[:-1]
        else:
            val = stringify(v.get('value'))
            old_val = stringify(v.get('old_value'))
            new_val = stringify(v.get('new_value'))
            lines.append(msg.get(status).format(
                path=path,
                val=val,
                old_val=old_val,
                new_val=new_val))
        keys = keys[:-1]
    return lines


def format(diff):
    diff = normalize_values(diff)
    diff = gen_plain_diff(diff)
    return '\n'.join(filter(lambda _: _ != '', diff))
