def emailValidator(email):
    if email[0].isdigit():
        raise RuntimeError("Email start by Number ")
    elif '@' not in email:
        raise RuntimeError("Email Format invalid ")
    elif 'yahoo.com' not in email and 'gmail.com' not in email:
        raise RuntimeError("Server is invalid ")
    return email


def mobileValidator(mobile):
    if not mobile[0].isdigit() or len(mobile)!=11 or mobile[:2]!='09':
        raise RuntimeError("Mobile format invalid ")
    return mobile


email=input('Please enter email : ')
try:
    emailValidator(email)
    print(email)
except RuntimeError as error:
    print(error)
    