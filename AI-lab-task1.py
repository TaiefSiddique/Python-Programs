# import sys
# x=int(input())
# y=int(input())
# z=int(input())
# max=-sys.maxsize - 1
# i=0
# if(max<x):
#     max=x
# if(max<y):
#     max=y
# if(max<z):
#     max=z
# print(max)

import sys
arr=[]
for i in range(3):
    elem=int(input())
    arr.append(elem)
max=-sys.maxsize - 1
for i in range(3):
    if(arr[i]>max):
        max=arr[i]
print("Maximum Value is ",max)