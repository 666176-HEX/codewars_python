"""
1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681. The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

Example:
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".

Note
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
"""
def divisors(n):
    large_divisors = []
    for i in range(1, int((n ** (0.5)) + 1)):
        if n % i == 0:
            large_divisors.append(i)
            if i*i != n:
                large_divisors.append(n / i)
                print(i*i,n, n / i)
    return large_divisors
        
def list_squared(m, n):
    res = [[1,1]] if m == 1 else []
    summ = 0
    for y in range(m,n+1):
        summ = sum([x*x for x in divisors(y)])
        if summ ** (0.5) % 2 == 0: 
            res.append([y,summ])
    return res

print(list_squared(1,250))