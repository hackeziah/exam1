import pytest
from main import Solution

@pytest.fixture
def solution_instance():
    return Solution()

def test_missing_int_in_array(solution_instance):
    assert solution_instance.missing_int([1, 3, 6, 4, 1, 2]) == 5
    assert solution_instance.missing_int([1, 2, 3]) == 4
    assert solution_instance.missing_int([-1, -1, -1, -5]) == 1
    assert solution_instance.missing_int([1, 3, 6, 4, 1, 7, 8, 10]) == 2

def test_find_divisible(solution_instance):
    assert solution_instance.find_divisible(6,11,2) == 3
    assert solution_instance.find_divisible(0, 11, 2) == 6

def test_rotate(solution_instance):
    assert solution_instance.rotate([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution_instance.rotate([0, 0, 0], 1) ==  [0, 0, 0]
    assert solution_instance.rotate([1, 2, 3, 4], 4) == [1, 2, 3, 4]
