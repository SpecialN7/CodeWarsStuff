#In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.
#The string has the following conditions to be alphanumeric:
#At least one character ("" is not valid)
#Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
#No whitespaces / underscore
def alphanumeric(password):
    numeritos = ["1","2","3","4","5","6","7","8","9","0"]
    from string import ascii_letters
    if password == "":
        return False
    for digit in password:
        if digit not in ascii_letters and digit not in numeritos:
            return False
    else:
        return True
    pass
