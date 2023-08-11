from random import *
# Task 1
# x=[0]*10
# for i in range(10):
#     x[i]=randint(20,50)
# print(x)


# Task 2
# x=[0]*10
# sum=0
# for i in range(10):
#     x[i]=randint(20,50)
#     sum+=x[i]
# print(x)
# print(sum)


# Task3
# x=[0]*10
# for i in range(10):
#     x[i]=randint(20,50)
# print(x)
# li=[x[i] for i in range(10)]
# print(li)



# Task 4
# li1=[0]*5
# li2=[0]*5
# li3=[]
# for i in range(5):
#     li1[i]=randint(20,50)
#     li2[i]=randint(20,50)
# for i in range(5):
#     for j in range(4):
#         if li1[j]>li1[j+1]:
#             li1[j],li1[j+1]=li1[j+1],li1[j]
#         if li2[j]>li2[j+1]:
#             li2[j],li2[j+1]=li2[j+1],li2[j]
# print(f'sorted list1 : {li1}')
# print(f'sorted list 2 : {li2}')
# for i in range(5):
#     li3.append(li2[i])
# for i in range(5):
#     li3.append(li1[i])
# print(li3)
# for j in range(10):
#     for i in range(9):
#         if li3[i]>li3[i+1]:
#             li3[i],li3[i+1]=li3[i+1],li3[i]
# print(li3)


# task 5
# odd=[]
# even=[]
# count_even=count_odd=0
# x=[0]*10
# for i in range(10):
#     x[i]=randint(20,50)
# print(x)
# for i in range(10):
#     if x[i]%2==0:
#         count_even+=1
#         even.append(x[i])
#     else:
#         count_odd+=1
#         odd.append(x[i])
# print(odd, even)

# if count_even < count_odd:
#     for i in range(10):
#         if x[i]%2 ==0:
#             x[i]+=1
# elif count_even > count_odd:
#     for i in range(10):
#         if x[i]%2 !=0:
#             x[i]-=1
# print(count_odd,count_even)
# print(x)


#Task 6
# arr=[]
# while True:
#     num=randint(1,15)
#     if num not in arr:
#         arr.append(num)
#     if len(arr)==10:
#         break
# print(arr)

# #task 7
# arr=[0]*10
# for i in range(10):
#     arr[i]=randint(1,5)
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             print(i,j)
# print(arr)


# Task 8 
li=[0]*20
for i in range(20):
    li[i]=randint(20,80)
for i in range(len(li)):
    for j in range(len(li)-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)
for i in range(len(li)-1):
    for j in range(li[i]+1,li[i+1]):
        print(j,end=' ')


# task 9
# li=[0]*20
# li2=[]
# for i in range(20):
#     li[i]=randint(0,9)
# li2.append(li[0])
# li2.append(li[1])
# for i in range(2,len(li)-2):
#     avg=(li[i-1]+li[i-2]+li[i+1]+li[i+2])//4
#     li2.append(avg)
# li2.append(li[18])
# li2.append(li[19])
# print(li)
# print(li2)


# # Task 10 
# li=[0]*10
# for i in range(10):
#     li[i]=randint(3,7)
# for i in range(len(li)):
#     for j in range(li[i]):
#         print(f'*',end=' ')
#     print()