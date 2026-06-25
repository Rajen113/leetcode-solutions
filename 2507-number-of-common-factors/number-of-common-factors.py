from math import sqrt

class Solution:
    def factors(self, n):
        result = []

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                result.append(i)

                if n // i != i:
                    result.append(n // i)

        return result


    def commonFactors(self, a, b):
        result_a = self.factors(a)
        result_b = self.factors(b)

        common = set(result_a) & set(result_b)

        return len(common)