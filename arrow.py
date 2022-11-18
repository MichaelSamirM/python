import os
import time

#this function to print the upper arrow
#
def arrow_up(n,x):#n the width , x is the length
	#this loop to create the upper pyramid of arrow
	for i in range(n):
		print("\t\t\t\t\t\n",end="")
	k = 0
	for i in range(1, n):
		for space in range(-(n*3)+1,(n+1-i)+1):
			print(end="  ")
		while k!=(2*i-1):
			print("* ", end="")
			k += 1
	
		k = 0
		print()
	# this for loop to create tail of upper arrow and x is length of it	
	for i in range(x):
		print("\t\t\t\t\t*")
	print(" ")
	time.sleep(0.5)
	os.system('cls')

arrow_up(5,3) #to configure the tallest and length

def arrow_left(n):
	for i in range(n*2):
		print("\t\t\t\t\t\n",end="")
	for i in range(n):
		print("\t\t\t ",end="")
		for j in range(n - i ):
			print(' ', end='')
		for k in range(i + 1):
			print('*', end='')
		print()
	print("\t\t\t",end="")
	for i in range(n*2+7):
		print("*",end="")
	print(" ")

	for i in range(n):
		print("\t\t\t  ",end="")
		for j in range(i + 1):
			print(' ', end='')
		for k in range(n - i):
			print('*', end='')
		print()
	time.sleep(0.5)
	os.system('cls')

arrow_left(5)

def arrow_down (n,x):
	for i in range(n*3):
		print("\t\t\t\t\t\n",end="")
	for i in range(x):
		print("\t\t\t\t\t*")
	for i in range(n, 1, -1):
		print("\t\t\t\t  ",end="")
		for space in range(0, n-i):
			print("  ", end="")
		for j in range(i, 2*i-1):
			print("* ", end="")
		for j in range(1, i-1):
			print("* ", end="")
		print()
	time.sleep(.5)
	os.system('cls')
arrow_down(5,3)

def arrow_right(n):
	for i in range(n*2):
		print("\t\t\t\t\t\n",end="")
	for i in range(n):
		print("\t\t\t\t\t\t",end="")
		for k in range (i+1):
			print("*",end="")
		print("")
	print("\t\t\t\t\t",end="")
	for i in range(n*2+2):
		print("*",end="")
	print("")	
	for i in range(n, 0, -1):
		print("\t\t\t\t\t\t",end="")
		for j in range(0, i):
			print("*", end="")
		print("")
	time.sleep(.5)
	os.system('cls')
arrow_right(5)

	

	
		
		   