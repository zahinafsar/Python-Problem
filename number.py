#Question_link https://toph.co/arena?contest=scb-pa-iscpc-2019-chattogram-regional-r#!/p/board-of-numbers

ai=[int(i) for i in input().split()]
aj=[int(i) for i in input().split()]
result=[]
for x in ai:
	result.append(x)
for y in aj:
	result.append(y)
maxa=max(result)
result.remove(maxa)
maxb=max(result)
result.remove(maxb)
print(maxa*maxb)

#result: wrong answer at 5th try