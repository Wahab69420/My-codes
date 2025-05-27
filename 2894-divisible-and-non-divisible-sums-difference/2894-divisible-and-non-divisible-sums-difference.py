class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2

        count_div = n // m
        last_div = count_div * m
        sum_div = (count_div * (m + last_div)) // 2

        return total_sum - 2 * sum_div
