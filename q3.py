a = input()
b =  list(map(str,input().split()))
c = len(a)
d = []
for i in b:
	if a == i[0:c]:
		d.append(i)
print(d)