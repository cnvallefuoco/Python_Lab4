import math

print("This program will calculate for a single starting salary and a certain number of years at a job,"
      "\nwhat will be earned each year and over your working career, assuming a retirement age of 70"
      "\nand a yearly salary increase of 8%.")
print ("Please be sure to enter whole numbers excluding decimal values.")
print("")

# Prompt user for input values
user_name = input ("Please enter your name: ")
user_BY_str = input ("Please enter your birth year in numerical form: ")
salary_str = input ("Please enter your starting salary: ")
current_year_str = input ("Please enter the current year: ")

# Convert to integers
user_BY = int (user_BY_str)
salary = int (salary_str)
current_year = int (current_year_str)


# Calculate users age
age = current_year - user_BY

# Calulate working years
working_years = 70 - age

# Variable name for years worked
year_worked = 1

# Variable for total salary
total_salary = salary

print (user_name,"Here's what we calculated: ")

# Check age
if age < 14 :
    print (user_name , ", the age you entered is invalid")

# Use the while loop to add a 8% increase in salary to each year with a starting salary as the base.
# Then the sum of all of the yearly salaries combined to give an over sum of the user's working career.

else:
    print ("YEAR\t\tSALARY\t\t\t\t\t\t SUM")
    print (year_worked , "\t\t\t $" , round(salary) , "\t\t\t $" ,round(salary) )
    while year_worked < working_years :
        print("")
        salary_increase = salary * .08
        salary += salary_increase
        year_worked += 1
        total_salary += salary
        print (year_worked , "\t\t\t $" , round(salary) , "\t\t\t $" , round(total_salary) )
    print ("")
    # Once the length of their working career has reached its limit the while loop stops and
    # output the data and calculations it has acquired.
    print ("The total sum of your salary during your working career is $", round(total_salary))
    print (user_name, ", unfortunately your career length has reached its limit.")
