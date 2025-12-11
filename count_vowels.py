#Count the number of vowels in a string.
word="Hello,Python!"
total=0
vowels="aeiouAEIOU"
for ch in word:
    if ch in vowels:
        total+=1
print(total)
