#/usr/bin/env python
# adjust total and yearly interest to see different effects

#values
total = raw_input("Tell me the amount with which you open the account.\n")
yearly_addition = raw_input("How much will you add per year?\n")
interest = raw_input("What % interest will there be?  Decimals are fine.\n")
years_saved = raw_input("And how many years will you save?\n")

total = float(total)
first_total = total
yearly_addition = float(yearly_addition)
interest = float(interest)
years_saved = int(years_saved)
if(years_saved < 1):
    print("don't make a fuck out of me.\nConverting years_saved to 10.")
    years_saved = 10

#talk to me
print("Okay, we start with $" + str(total) + ".")
print("Add $" + str(yearly_addition) + " every year.")
print("With " + str(interest) + "% interest...")
print("If you save " + str(years_saved) + " years,\n")

#the calculation
counter = 0
total = total * (1+interest/100)
counter = counter+1
while(counter!=years_saved): #while counter is not equal to years saved
    total = total * (1+interest/100)
    total = total + yearly_addition
    counter = counter+1  #increment the counter

#announce the result
print("Your final savings will be $" + str(total) + ".\n")
print("Your total interest was $" + str(total - (first_total + yearly_addition*(years_saved-1))) + ".\n")
