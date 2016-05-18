#!/usr/bin/env python
#encoding=utf-8

import math

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append()
 
    return result_list
 
# 或者更好一些的...
 
def get_primes(input_list):
    return (element for element in input_list if is_prime(element))
 
# 下面是 is_prime 的一种实现...
 
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1 # <<<<<<<<<<

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

def test_yield(number):
	#number = yield number
	data = yield
	

if __name__ == "__main__":
	#solve_number_10()
	gg = test_yield(1)
	d = gg.send(None)
