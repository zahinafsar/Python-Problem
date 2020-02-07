# Question_link:  https://toph.co/p/victory-robot?statement=bn_bd



                                    # mathod 1

                                    
t = int(input())
i=0
a=[]
while t > i:
	a.append(int(input()))
	i=i+1
for x in range(t):
	if (a[x])%2 == 0:
		print('bangla')
	else:
		if (a[x]) == 1971:
			print('Joy Bangla')
		else:
			print('joy')

# result: wrong answer


                                     # mathod 2



t = int(input())
i=0
while t > i:
	a=int(input())
	if a%2 == 0:
		print('bangla')
	else:
		if a == 1971:
			print('Joy Bangla')
		else:
			print('joy')
	i=i+1
# result: wrong answer
