# Using range() and a loop, print out the song.

bottles = range(99, 1, -1)
for bottle in bottles:
	print "{0} bottles of beer on the wall, {0} bottles of beer...".format(bottle)
	print "If one of those bottles should happen to fall, {0} bottles of beer on the wall.".format(bottle-1)
	print "\n"
