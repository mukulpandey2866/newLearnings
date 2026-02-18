ch ='q'
if ch in "aeiouAEIOU":
    print(f"{ch} is a Vowel")
else :
    print("Consonant")



st = input("Enter a string: ")
ch = input("Enter a character to check: ")

if ch in st:
    print(f"{ch} is present in the string.")
else:
    print(f"{ch} is not present in the string.")
