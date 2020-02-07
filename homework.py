#Question_link: https://toph.co/p/homework?statement=bn_bd

t = int(input())
i=0
while t > i:
	a=int(input())
    b=0
	while int(a**0.5)!=(a**0.5):
		if a == 0:
			break
		else:
			a = int(a/10)
            b=b+1
	print(b)
	i=i+1

# result: still working...........
