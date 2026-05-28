'''Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%
'''
user_CTC = float(input('Enter the annual ctc in lakhs '))
HRA = 0.10 * (user_CTC*100000)
DA = .05 * (user_CTC*100000)
PF = 0.03 * (user_CTC*100000)
total_Allowance = HRA+DA+PF
if user_CTC < 5 :
    tax = 0.0
elif user_CTC >= 5 and user_CTC <= 10 :
    tax = 0.10 * (user_CTC*100000)
elif user_CTC > 10 and user_CTC <= 20 :
    tax = .20 * (100000*user_CTC)
else :
    tax = 0.30 * (100000 * user_CTC)

annual_salary = (user_CTC * 100000) - tax - total_Allowance 
monthly_salary = annual_salary /12
print('in_hand monthly salary is :,' , monthly_salary)