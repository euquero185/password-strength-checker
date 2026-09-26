import time

print("-" * 120)
print("Password Strengh Checker by Euquero185")
print("-" * 120)

def program():

    while True:

        user = input("Please insert your password >>> ")

        def checker():
            has_upper = False
            has_lower = False
            has_number = False
            has_less_than_8_letters = False
            has_more_than_8_letter = False
            has_more_than_16_letter = False
        
            for char in user:
                if char.isupper():
                    has_upper = True
                if char.islower():
                    has_lower = True
                if char.isdigit():
                    has_number = True

            #Check Lengh
            if len(user) >= 16:
                has_more_than_16_letter = True
            if len(user) >= 8:
                has_more_than_8_letter = True
            if len(user) < 8:
                has_less_than_8_letters = True

            # Final Verdict - ALL possible outcomes
            if has_upper and has_lower and has_number and has_more_than_16_letter:
                print("Calculating password strengh...")
                time.sleep(3)
                print("Your password is: very strong")
            elif has_upper and has_lower and has_number and has_more_than_8_letter:
                print("Calculating password strengh...")
                time.sleep(3)
                print("Your password is: strong")
            elif (has_upper and has_lower) or (has_upper and has_number) or (has_lower and has_number):
                print("Calculating password strengh...")
                time.sleep(3)
                if has_more_than_8_letter:
                    print("Your password is: medium")
                else:
                    print("Your password is: weak")
            else:
                print("Calculating password strengh...")
                time.sleep(3)
                print("Your password is: very weak")

        checker()

program()
