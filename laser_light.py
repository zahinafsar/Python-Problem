# Question_link:  https://toph.co/p/laser-light?statement=bn_bd


i=int(input())
list1=[]
list2=[]
while i>0:
	x,y=map(int,input().split())
	list1.append(x)
	list2.append(y)
	i-=1
result = []
item = len(list1)
for i in range(item):
    result.append(list1[i]/list2[i])
rset=list(set(result))
for ext in rset:
	result.remove(ext)
print(len(result)+1)

# result: runtime error