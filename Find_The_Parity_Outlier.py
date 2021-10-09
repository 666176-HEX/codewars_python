"""
You are given an array (which will have a length of at least 3, but could be very large) 
containing integers. The array is either entirely comprised of odd integers or entirely 
comprised of even integers except for a single integer N. Write a method that takes the 
array as an argument and returns this "outlier" N."""

def find_outlier(integers):
    odd = sum(map(lambda x: x%2 != 0,integers[:3])) >= 2
    return list(filter(lambda x: x%2 != odd, integers))[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))