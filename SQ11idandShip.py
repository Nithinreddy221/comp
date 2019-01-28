
def get_ship_det(num_of_cases):
	#framing the dict with ids as keys and ships as values
    ship_det_dict = {'B':'BattleShip','C':'Cruiser','D':'Destroyer','F':'Frigate'}
    #checking the condition 1<=num_of_cases<=1000
    if num_of_cases>=1 and num_of_cases<=1000:
    	#creating empty list
        cases = []
        print 'Please Enter the Id(s)'
        #iterating in the range of test cases
        for i in range(0,num_of_cases):
        	#taking the id as input
            char = raw_input()
            #appending to the list
            cases.append(char)
        #iterating the cases list
        for c in cases:
        	#writing eception
            try:
            	#converting the ids to upper case
                temp = c.upper()
                #getting value from dict ship_det_dict and printing it
                print   ship_det_dict[temp]
            #if any error occurs it reaches this block
            except Exception as e :
                print 'Ship description not found for Id :' + c

    else :
    	#if condition is not satsafied it prints this warning line
        print 'Number of Test Cases must be in the range of 1 to 1000'
        #calling get_ship_det wit perameter of ships count
        num_of_cases = raw_input()
        #calling the function get_ship_det
        get_ship_det(num_of_cases)
    return 0
if __name__=="__main__":
	#taking as input of ships count(cases)
    num_of_cases = int(raw_input("Enter Number of Test Cases "))
    #calling get_ship_det wit perameter of ships count
    get_ship_det(num_of_cases)

