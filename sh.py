# def a(b=[0,1,1,2,3,5,]):
#     i=0
#     c=[]
#     while i<len(b):
#         c.append(b[i]**3)
#         i=i+1
#     print(c)
# a()


# x=lambda a:a**3
# print(x(2))



# a=[10,20,30,40]
# b=[100,200,300,400]
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         print(a[i],b[-j])
#         j=j+1
#         i=i+1

    
# a= [1,"f",2,"b",3,4,"h","j",6,9,0,"k"]
# i=0
# c=[]
# d=[]
# while i<len(a):
#     if type (a[i])==str:
#         print(a[i],"alp")
#         c.append(a[i])
#     else:
#         print(a[i],"num")
#         d.append(a[i])
#     i=i+1
# print(c)
# print(d)




# def num(a):
#     i=1
#     while i<=a:
#         print(i)
#         i=i+1
# a=int(input("enter the number :"))
# num(a)


# c=[]
# i=0
# while i<3:
#     a=int(input("enter the number :"))
#     c.append(a)
#     i=i+1
# print(c)
# j=0
# while j<len(c):
#     print(c[0],c[1],c[2])
#     print(c[1],c[2],c[0])
#     print(c[2],c[0],c[1])
#     print(c[1],c[0],c[2])
#     print(c[0],c[2],c[1])
#     print(c[2],c[1],c[0])
#     j=j+1

# n=(input("enter"))
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         k=0
#         while k<len(n):
#             if (i!=j and j!=k and i!=k):
#                 print(n[i],n[j],n[k])
#             k+=1
#         j+=1
#     i+=1





# a=[[1,2],[3,2],[5,6],[3,4],[89,80]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i+=1
# print(sum)


# a=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# i=0
# sum=0
# b=0
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         if a[i][j]>b:
#             b=a[j][j]
#             c.append(b)
#         j=j+1
#     i+=1
# print(c)
# print(sum)



a=[1,342,75,23,98]
b=[75,23,98,12,78,10,1]
i=0
c=[]
while i<len(a):
    if a[i] in b:
        c.append(a[i])
    i=i+1
print(c)




# a=[1,342,75,23,98]
# b=[75,23,98,12,78,10,1]
# i=0
# c=[]# a=[1,342,75,23,98]
# b=[75,23,98,12,78,10,1]
# i=0
# c=[]
# while i<len(a):
#     if a[i] in b:
#         c.append(a[i])
#     i=i+1
# print(c)

# while i<len(a):
#     if a[i] in b:
#         c.append(a[i])
#     i=i+1
# print(c)
