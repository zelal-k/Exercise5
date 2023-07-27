# pe5.py
import pytest

# Code from PE2 to generate the multiplication table
multi_table = [['X'] + list(range(1, 13))] + [[i] + [j * i for j in range(1, 13)] for i in range(1, 13)]

# Test 1: Plain test - check if the multiplication table has the correct number of rows and columns

def test_table_dimensions():
    assert len(multi_table) == 13
    assert all(len(row) == 13 for row in multi_table)

# Test 2: Plain test - check if the first row and column have the correct values

def test_table_header():
    assert multi_table[0] == ['X'] + list(range(1, 13))
    assert all(multi_table[i][0] == i for i in range(1, 13))

# Test 3: Marked to expect failure - intentionally failing test
@pytest.mark.xfail
def test_fail_case():
    assert False, "This test is expected to fail."

# Test 4: Test for IndexError if a row or column index exceeding 12 is specified
def test_index_error():
    with pytest.raises(IndexError):
        # Accessing index 13, which is out of range
        value = multi_table[13][0]

    with pytest.raises(IndexError):
        # Accessing index 13, which is out of range
        value = multi_table[0][13]

# Test 5: Parametrized test with input-output combinations
@pytest.mark.parametrize("input_row, expected_output", [
    (1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    (2, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]),
    (5, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]),
    (10, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]),
])
def test_parametrized_table_rows(input_row, expected_output):
    assert multi_table[input_row][1:] == expected_output
