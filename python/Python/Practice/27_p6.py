### Dictionary

def getStudentAvg(list_dictionary):
    tempList=[]
    for student in list_dictionary:
        for key,value in student.items():
            avg=sum(value)/len(value)
            tempList.append({key:avg})
    return tempList
    
    
    
list_dictionary=[
    {"asa":[13.4,59,45,3,95]},
    {"simaxus":[14,25,45]},
    {"sonia":[44.2,55,12,9]}
     ]
    
print(getStudentAvg(list_dictionary))