#!/usr/bin/env python3

import pyinputplus as pyip

print("\n*** Yearly compound interest calculator ***\n")

print("Initial investment:",end=" ")
initialInvestment = pyip.inputNum()

print("Monthly Contribution:",end=" ")
monthlyContribution = pyip.inputNum()

monthlyContribution *= 12
n = 1

print("Length of Time in Years:",end=" ")
lengthOfTime = pyip.inputNum()

print("Estimated Interest Rate:",end=" ")
interestRate = pyip.inputNum()


yearlyCompound = initialInvestment*((1+((interestRate/100)/n))**(n*lengthOfTime))
recurringPayment = monthlyContribution*(((1+(interestRate/100))**(n*lengthOfTime)-1)/(interestRate/100))
finalAmount = yearlyCompound + recurringPayment


print(f"Final amount: ${round(finalAmount,2)}");


