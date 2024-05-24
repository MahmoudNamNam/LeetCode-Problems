
# Fibonacci Solutions

## Solution #1: Recursive Approach

For \( n > 1 \), \( F(n) \) should return \( F(n-1) + F(n-2) \).

- **Time Complexity**: \( O(2^n) \)

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)
```

## Solution #2: Dynamic Programming Approach

We are computing the already computed values of Fibonacci numbers. Since there are overlapping subproblems, we can create and store the Fibonacci values in an array.

- **Time Complexity**: \( O(n) \) (Linear complexity)
- **Space Complexity**: \( O(n) \) since we store the Fibonacci values in an array.

```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range 2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

## Solution #3: O(1) Solution Using Math

When we take any two successive Fibonacci numbers, their ratio is very close to the Golden Ratio $\phi$, which is approximately 1.618034...

### Mathematical Basis

The Fibonacci sequence can be approximated using Binet's formula:
 $$
 F(n) = \frac{{\phi^n - (1 - \phi)^n}}{\sqrt{5}}
 $$
where  $\phi$ (the Golden Ratio) is:
$\phi = \frac{{1 + \sqrt{5}}}{2} $

For large values of  n ,  $(1 - \phi)^n $ becomes very small (since $(1 - \phi) $ is approximately -0.618) and can be ignored in the integer approximation. Therefore, the $n$ th Fibonacci number can be approximated as:
 $F(n) \approx \frac{{\phi^n}}{\sqrt{5}}$

```python
class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** n + 1) / 5 ** 0.5)
```
