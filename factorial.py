#!/usr/bin/env python3

num = int(raw_input("enter no. for calculating its factorial: "))
def factorial(num):
	if num == 1:
		return 1
	else:
		return factorial(num-1)*num
print( "factorial is:",factorial(num))
