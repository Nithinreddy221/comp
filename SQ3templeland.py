import sys


def pattern_string(pln):
	pst = raw_input("Enter the pattern: ")
	if len(pst) == pln:
		return pst
	else:
		print "number must contain {0} digits".format(pln)
		pattern_string(pln)


def pattern_length():
	pln = int(raw_input("Enter the pattern length: "))
	if pln >= 3 and pln <= 100:
		pstr = pattern_string(pln)
		return pstr
	else:
		print "Pattern range should be in range between 3 to 100"
		pattern_length()

				
def temple_land(num_of_cases):
	if num_of_cases >= 1 and num_of_cases <= 100:
		list_paterns = []
		i = 1
		while (i <= num_of_cases):
			plen = pattern_length()
			list_paterns.append(plen)
			i += 1
	else:
		print "Sorry cases should be in between 1 to 100"
		sys.exit()
	
	
		
	for dt in list_paterns:
		dt1 = list(dt)
		main_li = []
		if len(dt1)%2 == 0:
			print "NO"
		else:
			dt1 = map(int, dt1)
			mid = len(dt1)/2
			li = range(1, dt1[mid])
			li2 = list(reversed(range(1, dt1[mid])))
			main_li.extend(li)
			main_li.append(dt1[mid])
			main_li.extend(li2)
			if main_li == dt1:
				print "YES"
			else:
				print "NO
					

if __name__=="__main__":
    num_of_cases = int(raw_input("Enter Number of Test Cases in between 1 to 100: "))
    temple_land(num_of_cases)
