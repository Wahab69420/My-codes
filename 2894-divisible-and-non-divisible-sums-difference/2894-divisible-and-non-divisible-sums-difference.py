class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = []  # Stores numbers NOT divisible by m
        num2 = []  

        for i in range(1, n + 1):  # Loop from 1 to n
            if i % m == 0:
                num2.append(i)  # Divisible by m
            else:
                num1.append(i)  # Not divisible by m

        return sum(num1) - sum(num2)
