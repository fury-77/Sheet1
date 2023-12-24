Vowels = ['a','e','i','o','u']

user_input = input("Enter a character => ").lower()

if user_input in Vowels:
    print(f"{user_input} is a vowel")
else:
    print(f"{user_input} is not a vowel")