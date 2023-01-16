def ageValidate(age):
    if not isinstance(age,int):
        raise RuntimeError("Not valid Type")
    if age<1 or 120>age :
        raise RuntimeError("out of Range")
    return age
try:
    age=ageValidate("-  203")
    print(f"age is : {age}")
except RuntimeError as Error:
    print("Error")