# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11 
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
month = 0

while principal > 0:
    month = month + 1
    if month == extra_payment_start_month:
        payment = payment + extra_payment
    if month == extra_payment_end_month + 1:
        payment = payment - extra_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if principal <= 0:
        total_paid = total_paid + principal
        principal = 0      
    print(f'{month} {total_paid:.2f} {principal:.2f}')

print(f'Total paid {total_paid:0.2f}\nMonths {month}')
