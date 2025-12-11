#Reverse a given number (input: 12345 → 5 4 3 2 1).
num=12345
x=str(num)
for i in range(len(x)):
    digit=num%10
    print(digit,end=" ")
    num//=10
