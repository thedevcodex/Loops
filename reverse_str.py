#Reverse a string using a loop (don’t use slicing).
word="Hello"
reverse=""
for i in word:
    reverse=i+reverse
print(reverse)
