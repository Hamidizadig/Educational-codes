d={'UPPER_CASE':0,'LOWER_CASE':0}
s=input('Enter string : ')
for c in s :
    if c.isupper():
        d['UPPER_CASE']+=1
    elif c.islower():
        d['LOWER_CASE']+=1
    else:
        pass
print('No Upper case : ',d['UPPER_CASE'])
print('No Lower case : ',d['LOWER_CASE'])