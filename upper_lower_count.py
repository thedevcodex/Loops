#Count the number of uppercase and lowercase letters in a string.

var=input("Enter :")
total_upper=0
total_lower=0
for i in var:
    if i.isupper():
        total_upper+=1
    else:
        total_lower+=1
print("Total Upper:",total_upper)
print("Total Lower:",total_lower)
