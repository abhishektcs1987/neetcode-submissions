class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            count = 0
            while i:
                count += i & 1
                i = i >> 1
            print(i , count)
            arr.append(count)
        return arr