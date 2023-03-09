def passvalid(pas = "45781545"):
    if len(pas) == 0 :
        print('Your password is empty :(')
    elif len(pas) < 8 :
        print('Your password is most of 8 :(')
    elif pas.isnumeric():
        print('Your password is not have one letter :(')
    elif pas.isalpha():
        print('Your password is not have one number :(')
    else :
        print('Your password is valid login was seccsesful')
        return True

while True :
    password = input('Enter Password : ')
    value = passvalid(password)
    if(value):
        break
