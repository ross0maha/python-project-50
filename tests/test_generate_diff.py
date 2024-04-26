from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2.json'
    true_diff = open('tests/fixtures/result.txt', 'r')
    diff = generate_diff(first_file, second_file)
    assert diff == true_diff.read()
    true_diff.close()
