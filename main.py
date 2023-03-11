def isValid(password: str) -> bool:
    """This function checks the validity of `password`."""

    if len(password) == 0:
        print("Your password is empty :(")
        return False

    elif len(password) < 8:
        print("You password is most of 8 :(")
        return False
        
    if password.isnumeric():
        print("Password must have a minimum of 8 characters.")
        return False

    if password.isalpha(): 
        print("Password must have minimum 1 number.")
        return False
    
    return True
   
logged_in = False
    
while not logged_in:
    password = input('Password: ')
    
    if isValid(password):
        print("Logged in successfuly.")
        logged_in = True
