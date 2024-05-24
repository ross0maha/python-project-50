import pytest
from gendiff.scripts.gendiff import generate_diff


json_1 = "tests/fixtures/file1.json"
json_2 = "tests/fixtures/file2.json"
json_3 = "tests/fixtures/file3.json"
json_4 = "tests/fixtures/file4.json"
yaml_1 = "tests/fixtures/file1.yaml"
yaml_2 = "tests/fixtures/file2.yaml"


res_stylish_1 = "tests/fixtures/res_stylish_1.txt"
res_stylish_2 = "tests/fixtures/res_stylish_2.txt"
res_plain_1 = "tests/fixtures/res_plain_1.txt"
res_plain_2 = "tests/fixtures/res_plain_2.txt"
res_json_1 = "tests/fixtures/res_json_1.txt"
res_json_2 = "tests/fixtures/res_json_2.txt"


@pytest.mark.parametrize(
    "first_file, second_file, format_name, expected_file",
    [
        (json_1, json_2, "stylish", res_stylish_1),
        (json_1, json_2, "plain", res_plain_1),
        (json_1, json_2, "json", res_json_1),
        (json_3, json_4, "stylish", res_stylish_2),
        (json_3, json_4, "plain", res_plain_2),
        (json_3, json_4, "json", res_json_2),
        (yaml_1, yaml_2, "stylish", res_stylish_1),
        (yaml_1, yaml_2, "plain", res_plain_1),
        (yaml_1, yaml_2, "json", res_json_1),
    ],
)
def test_generate_diff(first_file, second_file, format_name, expected_file):
    with open(expected_file, "r") as expected:
        assert generate_diff(first_file, second_file, format_name) == expected.read() # noqa
