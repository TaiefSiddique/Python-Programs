income=int(input())
if income <= 10000:
    taxAmount=income*0.05
elif income>10000 and income<=50000:
    taxAmount=income*0.1
elif income>50000 and income<=1000000:
    taxAmount=income*0.2
else:
    print("invalid amount")
print("Tax ammount: ", taxAmount)