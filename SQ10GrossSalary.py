

def get_gross_salary(basic_salary):
	#calculating the gross for the employes who hale less than 1500
    if basic_salary<1500:
    	#calculating HRA as 10% of basic
        HRA = round(basic_salary*10/float(100),2)
        #calculating DA as 90% of basic
        DA = round(basic_salary*90/float(100),2)
    #calculating the gross for the employes who hale less than 1500    
    elif (basic_salary>=1500):
        HRA = 500
        #calculating DA as 98% of basic
        DA = round(basic_salary*98/float(100),2)
    #retuning the gross salary
    return basic_salary+HRA+DA


def num_of_employees(employees) :
	#checking the condition 1>=employees<=1000
    if employees>=1 and employees<=1000:
        print "Please enter the Salary of {0} Employee(s)".format(employees)
        #creating empty list
        lst_emp_sal = []
        i = 1
        #iterating the while loop until it equals the count of employes
        while(i<=employees):
        	#taking input as employe base salary as input
            salary = long(raw_input())
            #checking the condition 1<=salary<=100000
            if salary>=1 and salary<=100000:
            	#appending to the lst_emp_sal list     
                lst_emp_sal.append(salary)
            else :
                print "The salary must be in the range of 1 to 100000"
                i = i-1
            i=i+1
        #iterating the lst_emp_sal
        for sal in lst_emp_sal :
        	#calling get_gross_salary function to evalute the gross salary with perameter as base salary
            Gross_salary = get_gross_salary(sal)
            print  "Gross Salary is :" + str(Gross_salary)
    else :
        print "Number of Employee should be from 1 to 1000"
        #if it is not in the range calling the the function again with employes 
        employees = int(raw_input("No. of Employees: "))
        num_of_employees(employees)

if __name__=="__main__":
	#Number of employes are taking as input
    employees = int(raw_input("No. of Employees: ")) 
    #calling num_of_employees function with argument employes count
    num_of_employees(employees)





        
    


    






