from matrix import matrix_multiply
import pytest

class Test_Matrix_test:
    def test_one(self): 
        A = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        B = [
            [7, 8],
            [9, 10],
            [11, 12],
        ]
        expected_result = [
            [58, 64],
            [139, 154],
        ]
        assert matrix_multiply(A, B) == expected_result

    def test_two(self):
        # Test case 2: Incorrect dimensions, should raise a ValueError
        C = [
            [1, 2],
            [3, 4],
        ]
        D = [
            [1, 2],
        ]
        print("Error with incorrect dimensions.")