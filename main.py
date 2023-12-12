from typing import List

class Solution:

    def missing_int(self, A: List[int]) -> int:
        positive_int = 1
        converted_set = set(A)
        while True:
            if positive_int not in converted_set:
                return positive_int
            positive_int+=1

    def find_divisible(self, a: int, b: int, k: int) -> int:
        counter = 0
        for item in list(range(a,b)):
            if (item % k == 0):
                counter +=1
        return  counter
    
    def rotate(self, A: List[int], k: int) -> List[int]:
        for _ in range(k):
            top = A.pop(-1)
            A.insert(0, top)
        return A