from gendiff.formatters import stylish_format, plain_format

FORMATTERS = {
    'stylish': stylish_format,
    'plain': plain_format}
# 'json': json_format}


def formatting(tree, format):
    if format not in FORMATTERS:
        raise ValueError('Wrong format. Use next formats: {}'
                         .format(FORMATTERS.keys()))
    return FORMATTERS[format].format(tree)
