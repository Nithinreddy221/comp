import sys


def pattern_string(pln):
	#taking the pattern as input
	pst = raw_input("Enter the pattern: ")
	#checking the conditions
	if len(pst) == pln:
		#retuning the string
		return pst
	else:
		print "number must contain {0} digits".format(pln)
		#if condition returns false recalling the pattern
		return pattern_string(pln)


def pattern_length():
	#taking input as pattern length
	pln = int(raw_input("Enter the pattern length: "))
	#checking the pattern limits
	if pln >= 3 and pln <= 100:
		#calling the pattern_string for input pattern and plm as perameter
		pstr = pattern_string(pln)
		return pstr
	else:
		print "Pattern range should be in range between 3 to 100"
		#if condition is false recalling pattern_length fuction
		return pattern_length()

				
def temple_land(num_of_cases):
	# verifies the test case limits
	if num_of_cases >= 1 and num_of_cases <= 100:
		list_paterns = []
		i = 1
		#loop will repeate until copmletation of testcases
		while (i <= num_of_cases):
			#calling the functionton to verify the 
			plen = pattern_length()
			#adding the input patterns to the list_paterns
			list_paterns.append(plen)
			i += 1
			
	else:
		print "Sorry cases should be in between 1 to 100"
		#if we select out of the range it will terminate the program
		sys.exit()
	
	
	for dt in list_paterns:
		#converting string into list
		dt1 = list(dt)
		#checking the length of the pattern wether it is even or not
		if len(dt1)%2 == 0:
			#if it is even directly i am printing it as NO
			print "NO"
		else:
			#converting every element in list as integer
			dt1 = map(int, dt1)
			#picking the middel element index
			mid = len(dt1)/2
			#framing the original left side pattern from middel
			li = range(1, dt1[mid])
			#framing the right side pattern from the middel
			li2 = list(reversed(range(1, dt1[mid])))
			#adding all together to frame right pattern
			main_li = li + [dt1[mid]] + li2
			#comparing the right pattern with input pattern
			if main_li == dt1:
				#if condition is true printing yes
				print "YES"
			else:
				#if condition is false printing no
				print "NO"
					

if __name__=="__main__":
	# Number  of test cases taken as input
    num_of_cases = int(raw_input("Enter Number of Test Cases in between 1 to 100: "))
    temple_land(num_of_cases)
