# Program to check the strength of the password
password = input("Enter new password: ")
result = {}
if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False
digit = False
for i in password:
    if i.isdigit():
        digit = True

result['digit'] = digit
uppercase = False
for j in password:
    if j.isupper():
        uppercase = True

result['uppercase'] = uppercase

if result['length'] == True and result['digit'] == True and result['uppercase'] == True:
#if result['length'] is True and result['digit'] is True and result['uppercase'] is True:
#if all(result.values()):
    print('Strong Password')
else:
    print("Weak Password")
