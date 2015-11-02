# Random Walk Generation
while True:
 s += 1
 if (bool(random.getrandbits(1))):
   if (bool(random.getrandbits(1))):
     x += 1
   else:
     x -= 1
 else:
   if (bool(random.getrandbits(1))):
     y += 1
   else:
     y -= 1

 if (x >= Length):
   break
 elif (x < 0):
   x = 0
 if (y >= Circ):
   y -= Circ
 elif (y < 0):
   y += Circ
 lattice[x][y] += 1
 trajectory.append((x, y))
