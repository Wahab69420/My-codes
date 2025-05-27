class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = 0  # Sum of numbers NOT divisible by m
        sum2 = 0  # Sum of numbers divisible by m

        for i in range(1, n + 1):
            if i % m == 0:
                sum2 += i
            else:
                sum1 += i

        return sum1 - sum2
