#Name - Salvi C Patel
#Name - Soham M Patel
#Project name - Lab1_Group11
#Program name - Random password generator
#Date - May 20, 2023
#Description - This program will create a random password for the user as per their input.



import random

#variables
length = 0
letter_password = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit_password = 0
digits = "0123456789"
special_char_password = 0
specials = "!@#$%^&*()"
generated_password = ""
password_options = ""
create_password = 0


#prompt the user to enter a number greater or equals to 8 to generate the password.
length = int(input("To create a password, please enter a number which is greater than or equals to 8: "))

#checking the length is the user enter less than 8 give a error message.
if length < 8:
    print("Error: Length should be greater than or equal to 8.")
else:
    #ask the user that how many letters they want in their password
    letter_password = int(input("Please enter a number of letters you would like to have in your password: "))
    #ask the user that how many digits they want in their password
    digit_password = int(input("Please enter a number of digits you would like to have in your password: "))
    #ask the user that how many special characters they want in their password
    special_char_password = int(input("Please enter a number of special characters you would like to have in your password: "))
    #check is the input (digits) is within the range or not.
    if digit_password < 0 or digit_password > length:
        print("The input should be between 0 and", length)
    #check is the input (letters) are within the range or not.
    elif letter_password < 0 or letter_password > length:
        print("The input should be between 0 and", length)
    #check is the input (special characters) are within the range or not.
    elif special_char_password < 0 or special_char_password > length:
        print("The input should be between 0 and", length)
    else:
        #generate letters for the password
        for create_password in range(letter_password):
            generated_password += random.choice(letters)
        #generate digits for the password
        for create_password in range(digit_password):
            generated_password += random.choice(digits)
        #generate special characters for the password
        for create_password in range(special_char_password):
            generated_password += random.choice(specials)

        #shuffle the input and make a list
        password_options = list(generated_password)
        random.shuffle(password_options)
        #making a string of the shuffled password
        generated_password = "".join(password_options)

        #Printing the final output as per the input
        print("Your auto-generated password is:", generated_password)