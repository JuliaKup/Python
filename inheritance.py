n = int(input())
classes = {}
for i in range(n):
	s = input().split()
	classes[s[0]] = s[2:]

q = int(input())
for i in range(q):
	s = input().split()
	if s[0] == s[1]:
		print('Yes')
	else:
		ancestors = [s[1]]
		flag = True
		while ancestors:
			if ancestors[0] in classes:
				if s[0] in classes[ancestors[0]]:
					flag = False
					print('Yes')
					break
				else:
					ancestors.extend(classes[ancestors[0]])
			ancestors.pop(0)

		if flag:
			print('No')