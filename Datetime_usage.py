# Here we will be working in dates.
# For implementing anf working in date functions we need to use libray -> datetime


from datetime import datetime,timedelta

today_date = datetime.now()    #  TO display the current date.
print("Today's date is :" + str(today_date))
print()
print("Today date : ",today_date)

print("*************************************************************")
print()
###############################################################

# timedelta : this function is usage to define a period of days or month or years1
# For this function also, we need to import it from package

one_day = timedelta(days=1)
# one_month = timedelta(monthd = 1)     -> Wrong, for month change there is no 'month' assocoiated in datetime delta
# For implementing 1 month change you have set the suitable number of days i.e 30 or 31 etc                                      

one_month = timedelta(days  = 30)
one_year = timedelta(days = 365)
yesterday = today_date - one_day
last_month = today_date - one_month
last_year = today_date - one_year

print("The last year's date is :",last_year)
print("Yesterday's date is  : ",yesterday)
print("The last month date is  :",last_month)

print("*************************************************************")
print()
###########################################################################

# Now we will format and redesgin the view of the date

print("Today's day is :",today_date.day)
print("Today's month is :",today_date.month)
print("This year is :",today_date.year)

print("*************************************************************")
print()

########################################################################

# Now there the user wants to enter the date input. But python takes default input value as string.
# Hence we need to reformat the string date into date type and for that we use the function strptime

user_date = input("Hello There !!!  Please enter your birthdate in 'dd/mm/yyyy' format")
birthday = datetime.strptime(user_date,'%d/%m/%Y')   #  Format for taking the user's input date with 4 digit year
print("Youar date entered is :",birthday)
print()
print()
user_date = input("Hello There !!!  Please enter your birthdate in 'dd/mm/yy' format")
birthday = datetime.strptime(user_date,'%d/%m/%y')   #  Format for taking the user's input date with 2 digit year
print("Youar date entered is :",birthday)