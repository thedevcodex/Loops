#Count how many even numbers are between 1 to 50.
total=0
for i in range(1,51):
    if i % 2==0:
        total+=1
print("No of Even Numbers:",total)
