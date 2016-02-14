def echange(l,i,j):
	""" echange les indices i et j dans la liste l"""
	l[i], l[j] = l[j], l[i]

def permute(l,s):
	""" affiche toutes les permutations de la liste l[s:]"""
	if s == len(l):
		print (l)
	else :
		for i in range(s,len(l)) :
			echange(l,s,i)
			permute(l,s+1)
			echange(l,s,i)

permute([1,2,3,4],0)	