"""
compare followers and following
"""
def main():
	ers_path = 'followers.txt'
	ing_path = 'following.txt'

	with open(ers_path, 'r') as file:
		ers = file.readlines()
	file.close()

	with open(ing_path, 'r') as file:
		ing = file.readlines()
	file.close()

	for i in ers:
		if i[0].isupper():
			ers.remove(i)
	
	for i in ing:
		if i[0].isupper():
			ing.remove(i)


	in_ers = list(set(ers) - set(ing))
	in_ing = list(set(ing) - set(ers))

	not_in_both = in_ers + in_ing

	print("following but not a follower: ", in_ing)

	#print("not mutual followers: ", not_in_both)

main()
