class MyExeption(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return "Error is : "+self.message+"..."


def avgValidate(avg):
    if not isinstance(avg, float):
        raise MyExeption("Not Valid Type")
    if avg < 0 or 20 < avg:
        raise MyExeption("Out of range")
    return avg


try:
    avg = avgValidate(13)
    print(f"Avg : {avg}")
except MyExeption as error:
    print("error")
else:
    print("ok")
finally:
    print("End")
