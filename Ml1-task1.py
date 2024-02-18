# string=input()
# for str in string:
#     count=0
#     for str2 in string:
#         if str == str2:
#             count+=1
#     print(str,count)

chars=input()
checked=""
for i in(range(len(chars))):
    count=0
    flag=1
    if(chars[i] in checked):
        flag=0
        continue
    else:
        for j in (range(len(chars))):
            if chars[i]==chars[j]:
                checked+=chars[i]
                count+=1
    if flag == 1:
        print(chars[i],count)