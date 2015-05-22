#! usr/bin/python
#Author : Sharique Zia
#Date : 21 May 2015
#Usage : A game of guessing the number

import sys

exiter = 'y'
while exiter == 'y' or exiter == 'Y':
		print "\nYou have 3 chances.You have to guess my number.\n"
		choice = raw_input("Do you wish to continue? (Y/N) : ")
		if choice == 'N' or choice == 'n':
				sys.exit(0)

		my_number =  7
		count = 0

		for value in range(3) :
				my_guess = int(raw_input("Please enter the number : "))
				if my_guess == my_number:
						print "\n\nCongratulations!! You guessed it right"
						break

				elif my_guess > my_number:
						print "The number you guessed is slightly larger."
						count = count+1

				elif my_guess < my_number:
						print "The number you guessed is slightly smaller."
						count = count + 1
        
		if count == 3:
						print "\n\nSorry you have exceeded your chance limit . "
						exiter = raw_input("Do you want to try again?(Y/N)")
		else:
						break				

print "Thankyou for playing the game."                
