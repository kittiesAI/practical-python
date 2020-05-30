# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
first_year = 1
months = 0

extra_payment_start_month = 5*12
extra_payment_end_month = extra_payment_start_month + 4*12
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months + 1
    
    if months >= extra_payment_start_month and months <= extra_payment_end_month:  
        principal = principal - extra_payment
        first_year = first_year + 1 
        total_paid = total_paid + extra_payment

    if principal<0:
        total_paid = total_paid - principal
        principal = 0
        
    # print(months, total_paid, principal)
    print(f'${months} \t {round(total_paid,2)}   out of \t ${round(principal,2)}')
    
print('Total months:', months, '\nTotal paid:', total_paid)  

print(f'${round(total_paid,2)} paid in {months} months')