#! usr/bin/python
#Author : Sharique Zia
#Date : 21 May 2015
#Usage : Convert binary to decimal.

binary_no = int(raw_input("Enter any binary number : "))
pw = 0                  #power
deci = 0                #decimal no. variable

while binary_no > 0:
		rem = binary_no % 10
		deci = deci + (2**pw * rem)
		pw = pw + 1
		binary_no = binary_no/10
		
print deci		
