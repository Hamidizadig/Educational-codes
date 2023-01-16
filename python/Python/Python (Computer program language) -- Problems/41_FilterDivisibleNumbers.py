num_list=[45,55,60,37,100,105,220,660,876]
result=list(filter(lambda x: (x%15==0),num_list))
print('Numbers divisible by 15 are : ',result)