### Mathematical Approach

To reach `endPos` from `startPos` in exactly `k` steps, we need to satisfy two conditions:
1. The difference between `endPos` and `startPos` must be achievable within `k` steps.
2. The parity of the difference between `endPos` and `startPos` must match the parity of `k`.

### Steps and Parity
1. **Calculate the required moves**: The difference between `endPos` and `startPos` is given by `delta = abs(endPos - startPos)`.
2. **Check feasibility**:
   - If `delta > k`, it is impossible to reach `endPos` in `k` steps.
   - If `(k - delta) % 2 != 0`, the parities do not match, and it is also impossible to reach `endPos` in `k` steps.

### Combinatorial Count
If the above conditions are met, we need to determine the number of ways to distribute the `k` steps into moves to the right (`r`) and to the left (`l`), such that:
$$
 r + l = k 
$$

$$r - l = endPos - startPos$$
Solving these equations:
$$ r = \frac{k + (endPos - startPos)}{2} $$
$$ l = \frac{k - (endPos - startPos)}{2} $$

The number of ways to choose `r` right steps out of `k` total steps is given by the binomial coefficient:
$ C(k, r) = \frac{k!}{r!(k-r)!} $

### Implementation
Here is the implementation using the above combinatorial approach:

```python
def numberOfWays(startPos, endPos, k):
    MOD = 10**9 + 7

    # Calculate the necessary moves
    delta = abs(endPos - startPos)
    
    # If the required moves are greater than k or the parity doesn't match, return 0
    if delta > k or (k - delta) % 2 != 0:
        return 0
    
    # Calculate r
    r = (k + delta) // 2
    
    # Calculate the binomial coefficient C(k, r)
    def binomial_coefficient(n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        k = min(k, n - k)
        c = 1
        for i in range(k):
            c = c * (n - i) // (i + 1)
        return c
    
    return binomial_coefficient(k, r) % MOD

# Example 1
print(numberOfWays(1, 2, 3))  # Output: 3

# Example 2
print(numberOfWays(2, 5, 10))  # Output: 0
```

### Explanation:
1. **Feasibility Check**: First, we check if it is possible to reach `endPos` from `startPos` in exactly `k` steps based on the difference and parity.
2. **Binomial Coefficient Calculation**: If it is feasible, we calculate the number of ways to distribute the steps using the binomial coefficient formula.
3. **Modulo Operation**: Finally, we return the result modulo \(10^9 + 7\).

This approach uses combinatorial mathematics to efficiently count the number of ways to reach the desired position within the given constraints.