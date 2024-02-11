#count occurance of vowels in a string entered by user
#approach 1
"""vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

sentance = input("Enter your sentance: ")
for ch in sentance:
    if ch in vowels:
        vowels[ch] += 1

print(vowels)
"""
#approach 2
"""sentance = input("Enter your sentance: ")
vowelsList = ["a", "e", "i", "o", "u"]
vowels = {}
for ch in sentance:
    if ch in vowelsList:
        if ch in vowels:
            vowels[ch] += 1
        else:
            vowels[ch] = 1

print(vowels)
"""
#approach 3
numcount = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
}

stringOfNumbers = input("Enter a number: ")
for ch in stringOfNumbers:
    if ch in numcount:
        numcount[ch] += 1

panagram = True

for num in numcount.values():
    if num == 0:
        panagram = False

if panagram == True:
    print("Congratulations! You have a panagram!")
else:
    print("The number you have entered is not a panagram.")