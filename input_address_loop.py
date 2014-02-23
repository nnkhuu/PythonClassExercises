address_NW = []
address_NE =[]
address_SW =[]
address_SE = []

for number in range(3):
	address=raw_input("What is your address?")

#if the address contains a quadrant (NW, NE, SE, SW), then add it to that quadrant's list
#allow user to enter 3 address; after three, print the length and contents of each list

	if "NW" in address:
		address_NW.extend([address])
		print "List of addresses in NW{0}".format(address_NW)
	
	if "NE" in address:
		address_NE.extend([address])
		print "List of addresses in NE{0}".format(address_NE)

	if "SW" in address:
		address_SW.extend([address])
		print "List of addresses in SW{0}".format(address_SW)

	if "SE" in address:
		address_SE.extend([address])
		print "List of addresses in SE{0}".format(address_SE)
