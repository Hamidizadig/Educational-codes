from unittest.mock import seal

class MyE(Exception):
    def __init__(self,message):
        super().__init__(self,message)
        self.message = message
        self.num=1000
        
    pass


def emailValidator(email):
    if email[0].isdigit():
        raise RuntimeError("Email start by Number ")
    elif '@' not in email:
        raise RuntimeError("Email Format invalid ")
    elif 'yahoo.com' not in email and 'gmail.com' not in email:
        raise RuntimeError("Server is invalid ")
    return email


def mobileValidator(mobile):
    if not mobile.isdigit() or len(mobile)!=11 or mobile[:2]!='09':
        raise RuntimeError("Mobile format invalid ")
    return mobile


email=input('Please enter email : ')
mobileNumber=input('Please enter Phone Nomber : ')
try:
    emailValidator(email)
    mobileValidator(mobileNumber)
    print(f"email : {email}")
    print(f"Mobile : {mobileNumber}")
    
except RuntimeError as error:
    print(error)
    