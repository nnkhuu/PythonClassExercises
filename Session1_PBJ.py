bread = 11
pb = 3
j =2

if bread >=2 and pb >0 and j >	0:
	print "You can make a PBJ sandwich!"

	
	if bread/2 >=2 and pb >=(bread/2) and j>=(bread/2):
		sandwich = (bread/2)
		print "You can make {0} sandwiches!".format(sandwich)

	elif bread/2 >=2 and pb < (bread/2) or j < (bread/2):
		print "There is not enough pb or not enough j."

		
		if bread%2>0 and pb >0 and j>0:
			print "You can make at least {0} open face sandwiches.".format(min(bread, pb, j))

		
			if pb<(bread%2>0)+(bread/2):
				print "You need more peanut butter."
			
				if j<=(bread%2>0)+(bread/2):
					print "You need more jelly."
					
					
					if bread>=pb>j:
						sandwich=bread/2
						peanut_butter=pb-j
						print "You can make {0} PBJ sandwiches and {1} peanut butter sandwich but you should take a hard, honest look at your life.".format(sandwich, peanut_butter)
