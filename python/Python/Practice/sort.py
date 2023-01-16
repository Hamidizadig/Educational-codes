from re import L


def mySort(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(0, i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


l = [594, 595, 5, 56, 26, 265, 2, 589, 489, .484, 652, 65, 25, 59, 894,
     89, 44, 89, 48, 94, 5.4, 8, 848, 89, 5, 895, 98, 652, 3, 265, 54]
list2 = mySort(l)
print(list2)
