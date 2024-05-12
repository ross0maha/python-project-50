from gendiff.scripts.gendiff import generate_diff


json_1 = 'tests/fixtures/file1.json'
json_2 = 'tests/fixtures/file2.json'
json_3 = 'tests/fixtures/file3.json'
json_4 = 'tests/fixtures/file4.json'
yaml_1 = 'tests/fixtures/file1.yaml'
yaml_2 = 'tests/fixtures/file2.yaml'

result_1 = 'tests/fixtures/result_1.txt'
result_2 = 'tests/fixtures/result_2.txt'


def test_generate_diff_json():
    result = open(result_1, 'r')
    diff = generate_diff(json_1, json_2)
    assert diff == result.read()
    result.close()


def test_generate_diff_json_2():
    result = open(result_2, 'r')
    diff = generate_diff(json_3, json_4)
    assert diff == result.read()
    result.close()


def test_generate_diff_yaml():
    result = open(result_1, 'r')
    diff = generate_diff(yaml_1, yaml_2)
    assert diff == result.read()
    result.close()
