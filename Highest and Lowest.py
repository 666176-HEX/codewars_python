"""
In this little assignment you are given a string of space 
separated numbers, and have to return the highest and lowest number.
"""

def high_and_low(numbers):
    num_list = list(map(int,numbers.split(' ')))
    return f'{max(num_list)} {min(num_list)}'

print(high_and_low("1 -2 3 4 5"))  