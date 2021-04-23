for i in range(100,1000):
		s=[]
		for j in range(100,1000):
			a=i*j
			s=int(str(a)[0:2])
			b=int(str(a)[-1::-2])
			if s==b:
				print(a ,end=" ")
			else:
				print("No")
