# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

bread = 14
pb = 10
jelly = 9
sandwich=1

while bread>=2 and pb>=1 and jelly>=1:
	print "I'm making sandwich #{0}".format(sandwich)
	bread=bread-2
	pb=pb-1
	jelly=jelly-1
	sandwich=sandwich+1

	print "\n"
	if bread<2 and pb>0 and jelly >0:
		none="bread"
		print "You are out of {0}.".format(none)		
		
		if pb<1 and bread>=2 and jelly>1:
			none="peanut butter"
			print "You are out of {0}.".format(none)	
			
			if jelly<1 and bread>=2 and pb>1:
				none="jelly"
			print "You are out of {0}.".format(none)

		print "\n"			
		print "All done; you only had enough ingredients for {0} sandwiches.".format(sandwich-1)
	
# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.


bread = 14
pb = 15
jelly = 5
sandwich=1

while bread>=2 and pb>=1 and jelly>=1:
	print "I'm making sandwich #{0}".format(sandwich)
	bread=bread-2
	pb=pb-1
	jelly=jelly-1
	sandwich=sandwich+1

	print "I now have enough bread for {0} more sandwiches, enough peanut butter for {1} more sandwiches, and enough jelly for {2} more sandwiches.".format(bread/2,pb,jelly)
	print "\n"
	
	if bread<2 and pb>0 and jelly>0:
		none="bread"
		print "I don't have enough {0} to make anymore sandwiches.".format(none)
	
	elif pb<1 and bread>=2 and jelly>1:
			none="peanute butter"
			print "I don't have enough {0} to make anymore sandwiches.".format(none)
		
	elif jelly<1 and bread>=2 and pb>1:
				none="jelly"
				print "I don't have enough {0} to make anymore sandwiches.".format(none)
