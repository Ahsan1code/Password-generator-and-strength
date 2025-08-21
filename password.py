#Automic generated password

import string
import random
def choicefun ():
    ch=(input("Enter choice : "))
    return ch
while True :
    print("Enter 1-------to check the strength of password \nEnter 2-------to generate a password\nEnter 3-------for exit : ")
    choice=choicefun()
    if choice=="1":
        passw = input("Enter your password here to check its strength : ")
        has_upper = any(ch.isupper() for ch in passw)
        has_lower = any(ch.islower() for ch in passw)
        has_digit = any(ch.isdigit() for ch in passw)
        has_special = any(ch in string.punctuation for ch in passw)
        if len(passw)<4 and len(passw)>=2:
            print("-----Your password is too weak, make sure your password has atleast length of 4-----")
            strength=10
        elif len(passw)<2:
            print("-----Your password is too weak, make sure your password has atleast length of 4-----")
            strength=1
        elif has_upper and has_lower and has_digit and has_special:
            strength = 100
        elif (has_lower and has_upper and has_digit) or \
            (has_lower and has_upper and has_special) or \
            (has_lower and has_digit and has_special) or \
            (has_upper and has_digit and has_special):
            strength = 80
        elif (has_upper and has_digit) or (has_lower and has_digit)or (has_lower and has_special)or (has_upper and has_special) or (has_digit and has_special) or (has_lower and has_upper):
            strength = 40
        elif has_lower or has_upper or has_digit or has_special:
            strength = 20
        else:
            strength = 0
        print(f"\t\t\t\tYou password strength is {strength}% ")
    elif choice=="2":
        while True:
            try:
                length = int(input("Enter length of password : "))
                if length<4 :
                    print("Please enter length atleast 4")
                    continue
                break
            except ValueError:
                print("Please enter the numeric data")
        while True:
            character = ""
            password=[]
            print("\t\t\t\t\t\t:<Note:>\nRemember If you enter something other than (Yes , yes , y) it will consider as NO")
            uselowerrcase = input("Do you want lowercase letters ? enter yes or no : ").lower()
            useuppercase = input("Do you want uppercase letters ? enter yes or no : ").lower()
            usedigits = input("Do you want Digits ? enter yes or no : ").lower()
            usepuncuation = input("Do you want Punctuation enter yes or no : ").lower()
            if uselowerrcase =="yes" or uselowerrcase=="y":
                character+=string.ascii_lowercase
                password.append(random.choice(string.ascii_lowercase))
            if useuppercase =="yes" or useuppercase == 'y':
                character+=string.ascii_uppercase
                password.append(random.choice(string.ascii_uppercase))
            if usedigits =="yes" or usedigits == 'y':
                character+=string.digits
                password.append(random.choice(string.digits))
            if usepuncuation =="yes" or usepuncuation == 'y':
                character+=string.punctuation
                password.append(random.choice(string.punctuation))
            if not character:
                print("Please select atleast any one option ")
                continue
            else:
                while len(password)<length:
                    password.append(random.choice(character))
                random.shuffle(password)
                # print("\t\t\t\tyour password is : ", password)#This will give you the list as sit is created
                print("\t\t\t\tyour password is : ", "".join(password))
                break
    elif choice == "3" :
        print("--------------Thanks for using me-------------- ")
        exit()
    else:
        print("You have entered the wrong choice\nPlease enter choice 1,2,or 3 ")