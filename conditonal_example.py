# Here we have the example of the use of the conditonal stmts

print(" Hello there!!  Please enter the salary you get so that we can calculate the tax :")
salary = int(input())

if salary >= 300000:
    tax_amount = salary * 0.12
else:
    tax_amount = salary * 0.9

print(" Your tax to be paid is  :",tax_amount)