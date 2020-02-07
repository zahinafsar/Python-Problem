# Question_link:  https://toph.co/p/sudoku?statement=bn_bd

a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
g=input()
h=input()
i=input()
game1=[[],
	  [],
	  [],
	  [],
      [],
	  [],
	  [],
	  [],
	  []]
game2=[[],
	  [],
	  [],
	  [],
      [],
	  [],
	  [],
	  [],
	  []]
game3=[[],
	  [],
	  [],
	  [],
      [],
	  [],
	  [],
	  [],
	  []]
game1[0]=a
game1[1]=b
game1[2]=c
game1[3]=d
game1[4]=e
game1[5]=f
game1[6]=g
game1[7]=h
game1[8]=i

game2[0]=a[0]+b[0]+c[0]+d[0]+e[0]+f[0]+g[0]+h[0]+i[0]
game2[1]=a[1]+b[1]+c[1]+d[1]+e[1]+f[1]+g[1]+h[1]+i[1]
game2[2]=a[2]+b[2]+c[2]+d[2]+e[2]+f[2]+g[2]+h[2]+i[2]
game2[3]=a[3]+b[3]+c[3]+d[3]+e[3]+f[3]+g[3]+h[3]+i[3]
game2[4]=a[4]+b[4]+c[4]+d[4]+e[4]+f[4]+g[4]+h[4]+i[4]
game2[5]=a[5]+b[5]+c[5]+d[5]+e[5]+f[5]+g[5]+h[5]+i[5]
game2[6]=a[6]+b[6]+c[6]+d[6]+e[6]+f[6]+g[6]+h[6]+i[6]
game2[7]=a[7]+b[7]+c[7]+d[7]+e[7]+f[7]+g[7]+h[7]+i[7]
game2[8]=a[8]+b[8]+c[8]+d[8]+e[8]+f[8]+g[8]+h[8]+i[8]

game3[0]=a[0]+a[1]+a[2]+b[0]+b[1]+b[2]+c[0]+c[1]+c[2]
game3[1]=a[3]+a[4]+a[5]+b[3]+b[4]+b[5]+c[3]+c[4]+c[5]
game3[2]=a[6]+a[7]+a[8]+b[6]+b[7]+b[8]+c[6]+c[7]+c[8]
game3[3]=d[0]+d[1]+d[2]+e[0]+e[1]+e[2]+f[0]+f[1]+f[2]
game3[4]=d[3]+d[4]+d[5]+e[3]+e[4]+e[5]+f[3]+f[4]+f[5]
game3[5]=d[6]+d[7]+d[8]+e[6]+e[7]+e[8]+f[6]+f[7]+f[8]
game3[6]=g[0]+g[1]+g[2]+h[0]+h[1]+h[2]+i[0]+i[1]+i[2]
game3[7]=g[3]+g[4]+g[5]+h[3]+h[4]+h[5]+i[3]+i[4]+i[5]
game3[8]=g[6]+g[7]+g[8]+h[6]+h[7]+h[8]+i[6]+i[7]+i[8]

for n in range(8):
	if sorted(list(map(int,game1[n]))) == list(set(map(int,game1[n]))):
		if sorted(list(map(int,game2[n]))) == list(set(map(int,game2[n]))):
			if sorted(list(map(int,game3[n]))) == list(set(map(int,game3[n]))):
				print('Congratulations!')
				break
			else:
				print('Oh No!')
				break	
		else:
			print('Oh No!')
			break
	else:
		print('Oh No!')
		break
		
# result: Accepted
