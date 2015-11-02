# Random Walk Loop erasure
x0, y0, pos = None, None, 0
while pos < len(trajectory):
	x, y = trajectory[pos]
	if lattice[x][y] > 1 and (not x0):
		x0, y0 = x, y
		pos0 = pos
		# print("First repeated element ", pos0, x0, y0)
	elif (x == x0) and (y == y0) and (lattice[x][y] == 1):
		# print("Deleting from ", pos0, " to ", pos)
		del trajectory[pos0:pos]
		x0, y0 = None, None
		pos = pos0
	lattice[x][y] -= 1
	pos += 1w
