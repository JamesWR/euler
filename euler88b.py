from math import ceil
finallist = []
maxsize = 100
for i in range(maxsize):
	finallist.append([])
	finallist[0].append(i)




for length in range(len(finallist)):
	print(length)
	length_list = finallist[length]
	for solution in length_list:
		if solution > 1:
			for i in range(1,ceil(maxsize/(solution-1))+1):
				# print('solution:', solution, 'gives:', solution*i, 'to:', (solution-1)*(i-1)+length)
				try:
					if solution*i not in finallist[(solution-1)*(i-1)+length]:
						finallist[(solution-1)*(i-1)+length].append(solution*i)
				except:
					pass
print(finallist[-1])
total = 0
for i in range(1, maxsize):
	total += max(finallist[i])
print(total)
# print(finallist[1199])

